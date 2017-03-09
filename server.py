from flask import Flask , render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print"Got post info"

    return redirect('/')

@app.route ('/result', methods=['POST'])
def result():
    name=request.form['name']
    selected_language= request.form['FavoriteLanguage']
    location=request.form['Dojolocation']
    comment=request.form['description']
    return render_template("result.html", language=selected_language, location=location, name=name, comment=comment)


app.run(debug=True)
