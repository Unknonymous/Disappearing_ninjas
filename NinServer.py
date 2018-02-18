from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def noNinjas():
    return render_template('default.html')

@app.route('/ninja')
def ninja():
    imgSpot = "../static/tmnt.png"
    return render_template('ninja.html', imgSpot = imgSpot)

@app.route('/ninja/<name>')
def colors(name):
    if (name == 'orange'):
        turtle = "michelangelo"
    elif (name == 'red'):
        turtle = "raphael"
    elif (name == 'purple'):
        turtle = "donatello"
    elif (name == 'blue'):
        turtle = "leonardo"
    else:
        turtle = "notapril"
    imgSpot = "../static/" + turtle + ".jpg"
    return render_template('ninja.html', imgSpot = imgSpot)


app.run(debug=True)