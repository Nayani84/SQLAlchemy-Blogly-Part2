"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from pdb import set_trace as bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abcde'
debug=DebugToolbarExtension(app)

app.app_context().push()
app.app_context()

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """home page."""
    return redirect('/users')

################################################ Users Route ################################################
@app.route('/users')
def show_users():
    """List users."""
    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/users/new", methods=["GET"])
def new_user_form():
    """show add user form."""

    return render_template("create_user.html")


@app.route("/users/new", methods=["POST"])
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or None
   

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)

    return render_template("user_detail.html", user=user )


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    """show edit form."""

    user = User.query.get_or_404(user_id)
    return render_template('user_edit.html' , user=user)


@app.route("/users/<int:user_id>/edit" , methods=["POST"])
def update_user(user_id):
    """update the user."""

    user = User.query.get_or_404(user_id)
    user.first_name=request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.commit()
    flash("user edited!!")
    return redirect('/users')


@app.route("/users/<int:user_id>/delete" , methods=["POST"])
def delete_user(user_id):
    """delete the user."""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("user deleted!!")
    return redirect('/users')

################################################ Posts Route ################################################
@app.route("/users/<int:user_id>/posts/new")
def new_post(user_id):
    """show new post form."""
    
    user = User.query.get_or_404(user_id)
    return render_template('create_post.html' , user=user)



@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):
    """Add post and redirect to user detail."""
   
    user = User.query.get_or_404(user_id)
    title = request.form['title']
    content = request.form['content']
  
    new_post = Post(title=title, content=content, users=user)
    
    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")



@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show info on a single post."""

    post = Post.query.get_or_404(post_id)

    return render_template("post_detail.html", post=post )



@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
    """show edit form."""

    post = Post.query.get_or_404(post_id)
    return render_template('post_edit.html' , post=post)


@app.route("/posts/<int:post_id>/edit" , methods=["POST"])
def update_post(post_id):
    """update the post."""

    post = Post.query.get_or_404(post_id)
    post.title=request.form['title']
    post.content = request.form['content']

    db.session.commit()
    flash("post edited!!")
    return redirect(f"/users/{post.user_id}")




@app.route("/posts/<int:post_id>/delete" , methods=["POST"])
def delete_post(post_id):
    """delete the post."""

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("post deleted!!")
    return redirect(f"/users/{post.user_id}")