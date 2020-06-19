from application import db
from application.models import Lists


db.drop_all()
db.create_all()

