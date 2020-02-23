from flask import render_template, request, redirect
from application import app, db
from application.models import BlogPost, Users, Books
from application.forms import PostForm, LoginForm, UpdateAccountForm, RegistrationForm

@app.route('/')
@app.route('/home')
def home():
     return render_template('home.html', title='Home')

@app.route('/books')
def books():
     return render_template('books.html', title='Books')

@app.route('/register', methods = ['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		register_data = Users(
			first_name = form.first_name.data,
			last_name = form.last_name.data,
			email = form.email.data,
			password = form.password.data
    		)
		db.session.add(register_data)
		db.session.commit()
	return render_template('register.html', title='Register', form = form)

@app.route('/login', methods = ['GET','POST'])
def login():
     form = LoginForm()
     return render_template('login.html', title='Login', form = form)

@app.route('/login/myaccount')
def myaccount():
     return render_template('myaccount.html', title='My Account')

@app.route('/login/myaccount/logout')
def logout():
     return render_template('logout.html', title='Logout')

@app.route('/login/myaccount/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/login/myaccount/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('/login/myaccount/posts', all_posts=BlogPost)

@app.route('/login/myaccount/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/login/myaccount.html')

@app.route('/login/myaccount/posts/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST': 
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=BlogPost)

@app.route('/login/myaccount/admin', methods=['GET','POST'])
def bookentry(id):
    form = BookEntryForm()
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST': 
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
