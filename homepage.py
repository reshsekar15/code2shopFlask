from flask import Flask
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/code2shopv1'
heroku = Heroku(app)
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email
        
# User profile
class Profile(db.Model):
	profileid = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))
	def __init__(self, username):
		self.username = username
		self.password = password
		self.profileid = profileid
	def __repr__(self):
		return '<Profile %r>' % (self.username) 
	
#Challenges
class Challenges(db.Model):
	challengeID = db.Column(db.Integer, primary_key = True)
	challengeName = db.Column(db.String(150))
	challengePoints = db.Column(db.Integer)
	def __init__(self, challengeID):
		self.challengeID = challengeID
		self.challengeName = challengeName
		self.challengePoints = challengePoints
	def __repr__(self):
		return '<Challenges %r>' % (self.challengeID)

#Products
class Products(db.Model):
	productiD = db.Column(db.Integer, primary_key = True)
	productName = db.Column(db.String(150))
	def __init__(self, productiD):
		self.productiD=productiD
		self.productName = productName
	def __repr__(self):
		return '<Products %r>' % (self.productiD)

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/code2shopv1', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
