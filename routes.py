import os, pyexts
from flask import Flask, render_template, request, flash, redirect
from forms import ContactForm, srsForm
from flask.ext.mail import Message, Mail

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

# home

@app.route('/', methods=['GET', 'POST'])
def home():
	form = srsForm()
	if request.method == 'GET':
		return render_template('home.html', form=form)
	else: 
		if form.validate() == False:
			flash('Please enter a subreddit.')
			return render_template('home.html', form=form)
		else:
			srs = pyexts.srs_scraper(form.srs_input.data)
			return render_template('scraper.html', form=form, srs=srs)
			#formatting
			#error messages

# about
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return 'Something is broken.'

# scraper script

@app.route('/scraper', methods=['GET', 'POST'])
def scraper():

	if request.method == 'GET':
		return redirect("/", code=302)

# contact

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender = 'dev.rioht@gmail.com',recipients=['davecha@gmail.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)

			return render_template('contact.html', success=True)

	elif request.method == 'GET':
		return render_template('contact.html', form=form)

# error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)