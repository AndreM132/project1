from application import app, db
from flask import render_template, redirect, url_for
from application.forms import ListForm, GCForm
from application.models import Lists, GC


@app.route('/')
@app.route('/home')
def home():
	listData = Lists.query.all()
	return render_template('home.html', title='Home', lists=listData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
	
@app.route('/gamesconsoles', methods=['GET', 'POST'])
def gamesconsoles():
    form = GCForm()
    if form.validate_on_submit():
            GCData = GC(
                    games_title=form.games_title.data,
                    age_rating=form.age_rating.data,
                    games_price=form.games_price.data,
                    games_description=form.games_description.data,
                    console_title=form.console_title.data,
                    console_price=form.console_price.data,
                    console_description=form.console_description.data
            )
            db.session.add(GCData)
            db.session.commit()
            return redirect(url_for('gamesconsoles'))

    else:
            print(form.errors)
    return render_template('gamesconsoles.html', title='Games and Consoles', form=form)


@app.route('/lists', methods=['GET', 'POST'])
def lists():
	form = ListForm()
	if form.validate_on_submit():
		listData = Lists(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			list_title=form.list_title.data,
			list_description=form.list_description.data,
                        favourites=form.favourites.data
		)
		db.session.add(listData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('lists.html', title='Lists', form=form)

