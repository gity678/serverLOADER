from flask import Flask, request, jsonify
import json
import os
import random
import string

app = Flask(__name__)
CODES_FILE = 'codes.json'

# تحميل الأكواد من الملف
def load_codes():
    if not os.path.exists(CODES_FILE):
        with open(CODES_FILE, 'w') as f:
            json.dump([], f)
    with open(CODES_FILE, 'r') as f:
        return json.load(f)

# حفظ الأكواد
def save_codes(codes):
    with open(CODES_FILE, 'w') as f:
        json.dump(codes, f)

@app.route('/')
def home():
    return "✅ Server is Live"

# التحقق من الكود
@app.route('/check', methods=['GET'])
def check_code():
    code = request.args.get('code')
    codes = load_codes()
    if code in codes:
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'fail'})

# إضافة كود يدويًا
@app.route('/add', methods=['POST'])
def add_code():
    code = request.form.get('code')
    codes = load_codes()
    if code and code not in codes:
        codes.append(code)
        save_codes(codes)
        return jsonify({'status': 'added', 'code': code})
    return jsonify({'status': 'exists'})

# توليد كود تلقائيًا
def generate_code(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/generate', methods=['POST'])
def generate():
    code = generate_code()
    codes = load_codes()
    codes.append(code)
    save_codes(codes)
    return jsonify({'status': 'generated', 'code': code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
