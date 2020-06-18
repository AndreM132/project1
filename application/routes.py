from application import app, db
from flask import render_template, redirect, url_for
from application.forms import ListForm, GCForm
from application.models import Lists, Games


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='about')
	
@app.route('/gamesconsoles', methods=['GET', 'POST'])
def gamesconsoles():
    GamesData = Games.query.all()
    form = GCForm()
    if form.validate_on_submit():
            GamesData = Games(
                    games_title=form.games_title.data,
                    age_rating=form.age_rating.data,
                    games_price=form.games_price.data,
                    games_description=form.games_description.data,
                    console_title=form.console_title.data
            )
            db.session.add(GamesData)
            db.session.commit()
            return redirect(url_for('gamesconsoles'))

    else:
            print(form.errors)
    return render_template('gamesconsoles.html', title='Games', form=form, games=GamesData)


@app.route('/lists', methods=['GET', 'POST'])
def lists():
    listData = Lists.query.all()
    form = ListForm()
    if form.validate_on_submit():
	    listData = Lists(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			list_title=form.list_title.data,
			list_description=form.list_description.data,
                        favourites=form.favourites.data,
                        games_id=form.games_id.data
    	    )
	    db.session.add(listData)
	    db.session.commit()
	    return redirect(url_for('home'))

    else:
	    print(form.errors)
    return render_template('lists.html', title='Lists', form=form, lists=listData)


