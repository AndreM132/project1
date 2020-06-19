from application import db

class Lists(db.Model):
    list_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    list_title = db.Column(db.String(30), nullable=False, unique=True)
    list_description = db.Column(db.String(100), nullable=False, unique=True)
    favourites = db.Column(db.String(30), nullable=False)
    games_id = db.Column(db.Integer, db.ForeignKey('games.games_id'), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'List ID: ', self.list_id, '\r\n',
            'First Name: ', self.first_name, '\r\n', 'Last Name ', self.last_name, '\r\n',
            'Title: ', self.list_title,'\r\n'
        ])


class Games(db.Model):
    games_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    games_title = db.Column(db.String(30), nullable=False)
    age_rating = db.Column(db.Integer, nullable=False)
    games_price = db.Column(db.Integer, nullable=False)
    games_description = db.Column(db.String(100), nullable=False, unique=True)
    console_title = db.Column(db.String(30), nullable=False)
    lists = db.relationship('Lists', backref=db.backref('gamesref'), lazy=True)

    def __repr__(self):
        return ''.join([
            'Games ID: ', self.games_id, '\r\n', 'Games Title: ', self.games_title, '\r\n'
            ,'Console Title:: ', self.console_title,'\r\n'
        ])

