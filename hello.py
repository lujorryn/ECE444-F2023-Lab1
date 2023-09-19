from datetime import datetime
from flask import Flask, render_template
# Styling
from flask_bootstrap import Bootstrap
# Date and Time
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# In the screenshot of the assignment, we are on the / page not /user/<name>
# Hardcode name into the template for now
@app.route('/') 
def index():
    return render_template('index.html', name="Jorryn", current_time=datetime.utcnow())

### /user/<name> page not needed for this activity ###
# @app.route('/user/<name>') 
# def user(name):
#     return render_template('user.html', name=name)