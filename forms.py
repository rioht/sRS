from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError, StringField

class ContactForm(Form):
	name = StringField("Name", [validators.Required("Please enter your name.")])
	email = StringField("Email", [validators.Required("Please enter your email address."), validators.email()])
	subject = StringField("Subject", [validators.Required("Please enter a subject line.")])
	message = TextAreaField("Message", [validators.Required("Please enter a message.")])
	submit = SubmitField("Send")

class srsForm(Form):
	srs_input = StringField("srs_input", [validators.InputRequired()])
	submit = SubmitField("Action!")