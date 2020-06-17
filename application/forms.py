from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from application.models import Lists

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

    favourites = StringField('Favourites',
            validators = [
                DataRequired(),
                Length(min=3, max=30)
            ]
    )

    submit = SubmitField('Post List!')
