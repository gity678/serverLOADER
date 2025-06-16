from flask import Flask, request, render_template, redirect, url_for
import json, os, random, string

app = Flask(__name__)
CODES_FILE = 'codes.json'

def load_codes():
    if not os.path.exists(CODES_FILE):
        with open(CODES_FILE, 'w') as f:
            json.dump([], f)
    with open(CODES_FILE, 'r') as f:
        return json.load(f)

def save_codes(codes):
    with open(CODES_FILE, 'w') as f:
        json.dump(codes, f)

def generate_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    codes = load_codes()
    message = ''
    if request.method == 'POST':
        if 'new_code' in request.form:
            code = request.form['new_code'].strip()
            if code and code not in codes:
                codes.append(code)
                save_codes(codes)
                message = f'Added: {code}'
            else:
                message = 'Invalid or duplicate.'
        elif 'generate_code' in request.form:
            code = generate_code()
            codes.append(code)
            save_codes(codes)
            message = f'Generated: {code}'
        elif 'delete' in request.form:
            code = request.form['delete']
            if code in codes:
                codes.remove(code)
                save_codes(codes)
                message = f'Deleted: {code}'
    return render_template('index.html', codes=codes, message=message)

@app.route('/check')
def check():
    code = request.args.get('code','').strip()
    codes = load_codes()
    return {'status': 'ok' if code in codes else 'fail'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
