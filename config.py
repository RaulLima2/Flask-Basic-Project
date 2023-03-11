import os
basedir = os.path.abspath(
	os.path.dirname(__file__)
)

class Config:
	SECRET_KEY:str = os.environ.get('SECRET_KEY')
	SQLACHEMY_DATABASE_URI:str = os.environ.get('DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS:bool = False


