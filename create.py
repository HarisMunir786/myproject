from application import db
from application.models import BlogPost, User, Books

db.drop_all()
db.create_all()
