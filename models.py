from app import app, engine, db, db1


class ParsedNews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000))
    description = db.Column(db.String(2000))
    link = db.Column(db.String(300))
    img = db.Column(db.String(1000))
    

    def __repr__(self):
        return f"ParsedNews('{self.title}', '{self.description}', '{self.link}', '{self.img}')"


# create db in models
db.create_all()
db.session.commit()