import config
from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import create_session, sessionmaker, scoped_session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ffxicywfezkmnz:9aca639ea1aa0c11d83c348d6dddfe0b11c824e90b7e8f92aa6003a0369da3e7@ec2-23-20-168-40.compute-1.amazonaws.com:5432/d7kr0qdacisf7m'
engine = create_engine('postgres://ffxicywfezkmnz:9aca639ea1aa0c11d83c348d6dddfe0b11c824e90b7e8f92aa6003a0369da3e7@ec2-23-20-168-40.compute-1.amazonaws.com:5432/d7kr0qdacisf7m')
db1 = scoped_session(sessionmaker(bind=engine))
db = SQLAlchemy(app)

import routes

if __name__ == "__main__":
    app.run()