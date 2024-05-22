from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def exe():
    return render_template("index.html")

@app.route('/index2', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        session['image_url'] = request.form['image_url']
    return render_template("index2.html", image_url=session.get('image_url'))

@app.route('/index3', methods=['GET', 'POST'])
def texte():
    if request.method == 'POST':
        session['texte_saisi1'] = request.form['texte_saisi1']
        session['texte_saisi2'] = request.form['texte_saisi2']
    return render_template('index3.html', 
                           texte_saisi1=session.get('texte_saisi1'), 
                           texte_saisi2=session.get('texte_saisi2'), 
                           image_url=session.get('image_url'))

if __name__ == '__main__':
    app.run(debug=True)
