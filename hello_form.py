### Flask for Acitivity 4 ###
from flask import Flask, render_template, session, redirect, url_for, flash

# Styling
from flask_bootstrap import Bootstrap

# WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

### APP ###
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkeysecretkey'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST']) 
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index_form.html', form = form, name = session.get('name'))