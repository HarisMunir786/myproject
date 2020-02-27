from flask import render_template, request, redirect, url_for
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Comment, User, Book
from application.forms import PostForm, LoginForm, RegistrationForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/books')
def books():
	return render_template('books.html', title='Books')

@app.route('/register', methods = ['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data('utf-8'))
		user = User(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			email = form.email.data,
			password = hash_pw
    		)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form = form)

@app.route('/login', methods = ['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)

@app.route('/myaccount')
@login_required
def myaccount():
	form = UpdateAccountForm()
	posts = Posts.query.filter_by(user_id=current_user.id).all()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('myaccount.html', title='Account', form=form, posts=posts)

@app.route('/myaccount/comments', methods=['GET', 'POST'])
@login_required
def comments():
	form = CommentsForm()
	if form.validate_on_submit():
		postData = Comment(
			title = form.title.data,
			content = form.content.data,
			author = current_user
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('posts.html', title = 'Post', form=form)

@app.route('/comment/delete/<int:id>')
@login_required
def delete(id):
	comment = Comment.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()
	return redirect('/myaccount')

@app.route('comments/edit/<int:id>', methods=['GET','POST'])
def edit(id):
	post = BlogPost.query.get_or_404(id)
	if request.method == 'POST':
		post.title = request.form['title']
		post.author = request.form['author']
		post.content = request.form['content']
		db.session.commit()
		return redirect('/myaccount')
	else:
		return render_template('edit.html', post=post)

@app.route('/myaccount/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
