from flask import Flask,render_template,request
import stopwords
import words

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def index():
    tokens = None
    if request.method == 'POST':
        text = request.form['text']
        stemmed_words = stopwords.get_stemmed_words(text)
        tokens = words.get_tokens(stemmed_words)
    return render_template('index.html',title = 'Home',tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True,port=1234)
