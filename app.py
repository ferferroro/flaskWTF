from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length

# instantiate the app
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'secreto'

class myForm(FlaskForm):
    text = StringField('Romel text field', validators=[Length(min=5, max=10, message='Minimum lima at Maximum sampu')])
    password = PasswordField('Romel password field')
    checkbox = BooleanField('Romel boolean field')
    select = SelectField('Romel select field', choices=[('1','1'), ('2','2')])
    submit = SubmitField('Submit')

# index route
@app.route('/', methods=['GET', 'POST'])
def index():
    form = myForm()

    if request.method == 'GET':
        # do something
        return render_template('index.html', form=form)

    if request.method == 'POST':
        # old way I get the form data
        '''text = request.form['text']
        password = request.form['password']
        checkbox = request.form.get('checkbox')
        select = request.form['select']'''

        form.validate_on_submit() # or ganito -> form.validate

        # return f'{form.text.data=} {form.password.data=} {form.checkbox.data=} {form.select.data=}'
        # do something 
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
