from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Server is live!"

@app.route('/download')
def download_zip():
    return send_file('fake_data.zip', as_attachment=True, mimetype='application/zip')
