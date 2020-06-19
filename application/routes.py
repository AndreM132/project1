from application import app, db
from flask import render_template, redirect, url_for, request
from application.forms import ListForm, GCForm, UpdateForm
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
                        games_id=int(form.games_id.data)
    	    )
	    db.session.add(listData)
	    db.session.commit()
	    return redirect(url_for('lists'))

    else:
	    print(form.errors)
    return render_template('lists.html', title='Lists', form=form, lists=listData)


@app.route('/lists/update/<int:list_id>', methods=['GET', 'POST'])
def update(list_id):
    form = ListForm()
    listData = Lists.query.filter_by(list_id=list_id).first()
    if form.validate_on_submit():
        listData.first_name=form.first_name.data
        listData.last_name=form.last_name.data
        listData.list_title=form.list_title.data
        listData.list_description=form.list_description.data
        listData.favourites=form.favourites.data
        listData.games_id=int(form.games_id.data)
        db.session.commit()
        return redirect(url_for('lists'))
    elif request.method == 'GET':
        form.first_name.data=listData.first_name
        form.last_name.data=listData.last_name.data
        form.list_title.data=listData.list_title.data
        form.list_description.data=listData.list_description.data
        form.favourites.data=listData.favourites.data
        form.games_id.data=listData.games_id.data

    return render_template('update.html', title='Update', form=form)


@app.route("/lists/delete/<int:list_id>", methods=["GET", "POST"])
def delete(list_id):
    dellists = Lists.query.filter_by(list_id=list_id).first()
    db.session.delete(dellists)
    db.session.commit()
    return redirect(url_for('lists'))
