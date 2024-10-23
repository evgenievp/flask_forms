from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'test'


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


@app.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return render_template('success.html')
    else:
        return render_template('denied.html')





if __name__ == '__main__':
    app.run(debug=True)
