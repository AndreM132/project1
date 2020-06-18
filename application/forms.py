from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from application.models import Lists, Games

class ListForm(FlaskForm):
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    list_title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=30)
            ]
    )

    list_description = StringField('Description',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    favourites = StringField('Favourite Console',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
            ]
    )

    games_id = StringField('Games ID',
            validators = [
                DataRequired(),
                Length(min=1, max=4)
            ]
    )

    submit = SubmitField('Post List!')


class GCForm(FlaskForm):
    games_title = StringField('Games Title',
            validators = [
                DataRequired(),
                Length(min=4, max=50)
            ]
    )

    age_rating = StringField('Age Rating',
            validators = [
                DataRequired(),
                Length(min=1, max=10)
            ]
    )

    games_price = StringField('Games Price',
            validators = [
                DataRequired(),
                Length(min=1, max=10)
            ]
    )

    games_description = StringField('Games Description',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    console_title = StringField('Console Title(s)',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
            ]
    )

    submit = SubmitField('Add Game!')

