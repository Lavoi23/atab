from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dictionnaire pour stocker les URLs
url_dict = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = shorten_url(original_url)
        return render_template('result.html', original_url=original_url, short_url=short_url)
    return render_template('index.html')

def shorten_url(original_url):
    hash_code = hash(original_url)
    short_code = hash_code & 0xffffffffffffffff  # Utilisation des 16 premiers caractères du hash
    short_url = hex(short_code)[2:10]
    url_dict[short_url] = original_url
    return short_url

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_dict.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)
