from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Server is live!"

@app.route('/download')
def download_zip():
    return send_file('fake_data.zip', as_attachment=True, mimetype='application/zip')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render يحدد المنفذ
    app.run(host='0.0.0.0', port=port)
