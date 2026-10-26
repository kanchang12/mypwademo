from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/next')
def next_page():
    return render_template('nextpage.html')

# Serve PWA static assets from the root path if needed
@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@app.route('/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js')

if __name__ == '__main__':
    app.run(debug=True)
