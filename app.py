import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render يعطيك PORT
    app.run(host='0.0.0.0', port=port)
