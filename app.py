from flask import Flask, render_template, request

# instantiate the app
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'secreto'

# index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # do something
        return render_template('index.html')

    if request.method == 'POST':
        # old way I get the form data
        text = request.form['text']
        password = request.form['password']
        checkbox = request.form.get('checkbox')
        select = request.form['select']
        # do something 
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
