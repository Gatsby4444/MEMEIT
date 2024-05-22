from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/')
def exe():
    return render_template("index.html")


@app.route('/index2', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        image_url = request.form.get('image_url', '').strip()
        if image_url:
            session['image_url'] = image_url
            return redirect(url_for('texte'))
    return render_template("index.html", error="Please provide a valid image URL")


@app.route('/index2', methods=['GET'])
def show_image():
    image_url = session.get('image_url', None)
    if image_url:
        return render_template("index2.html", image_url=image_url)
    return redirect(url_for('exe'))


@app.route('/index3', methods=['GET', 'POST'])
def texte():
    if request.method == 'POST':
        texte_saisi = request.form.get('texte_saisi', '').strip()
        if texte_saisi:
            session['texte_saisi'] = texte_saisi
            return redirect(url_for('show_meme'))
    return render_template("index2.html", error="Please provide a valid text description")


@app.route('/index3', methods=['GET'])
def show_meme():
    image_url = session.get('image_url', None)
    texte_saisi = session.get('texte_saisi', None)
    if image_url and texte_saisi:
        return render_template('index3.html', texte_saisi=texte_saisi, image_url=image_url)
    return redirect(url_for('exe'))


if __name__ == '__main__':
    app.run(debug=True)
