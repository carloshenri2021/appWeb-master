from sqlalchemy import Column, String, Integer
from app import Base
import pymysql


class User(Base):
	con = pymysql.connect(host='localhost', user='root', passwd='6485@Mg81Sp38')
	cursor = con.cursor()
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True, nullable=False)
	hashed = Column(String(50), nullable=False)
	salt = Column(String(50), nullable=False)

	def __init__(self, username, hashed, salt):
		self.username = username
		self.hashed = hashed
		self.salt = salt

	def __repr__(self):
		return '<User: %s>' % self.username
