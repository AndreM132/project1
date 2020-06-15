from application import app, db
from flask import render_template, redirect, url_for
from application.forms import ListForm
from application.models import Lists


@app.route('/')
@app.route('/home')
def home():
	listData = Lists.query.all()
	return render_template('home.html', title='Home', lists=listData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
	
@app.route('/gamesconsoles')
def gamesconsoles():
    return render_template('gamesconsoles.html', title='Games and Consoles')


@app.route('/lists', methods=['GET', 'POST'])
def lists():
	form = ListForm()
	if form.validate_on_submit():
		listData = Lists(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			list_title=form.list_title.data,
			list_description=form.list_description.data
		)
		db.session.add(listData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('lists.html', title='Lists', form=form)

