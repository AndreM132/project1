from application import db

class Lists(db.Model):
    list_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    list_title = db.Column(db.String(30), nullable=False, unique=True)
    list_description = db.Column(db.String(100), nullable=False, unique=True)
    favourites = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, '\r\n', 'Last Name ', self.last_name, '\r\n',
            'Title: ', self.list_title,'\r\n', 'Description: ', self.list_description, '\r\n',
            'Favourites: ', self.favourites
        ])

