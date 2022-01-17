import flask
import webbrowser
from flask import *
import time
import pyperclip as pc


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    uname = request.form['mytext']
    url = "www.eksisozluk.com/biri/"
    url = url + uname
    #os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s" % url)
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
    #sleep for a little
    time.sleep(1)
    newurl = pc.paste()
    #return clipboard
    return render_template('foto.html', data=newurl)

if __name__ == "__main__":
	app.run(debug=True)