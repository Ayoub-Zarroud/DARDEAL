from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching during development

@app.route('/')
@app.route('/Home')
def index():
    return render_template('index.html')

@app.route('/Hero')
def hero():
    return render_template('hero.html')

@app.route('/Contact-Us')
def contact():
    return render_template('contact-us.html')

@app.route('/Branding-in-Morocco')
def blog1():
    return render_template('blog1.html')

@app.route('/Typography-Style-Guide')
def blog2():
    return render_template('blog2.html')

@app.route('/Audiovisual-Production')
def blog3():
    return render_template('blog3.html')

# Serve images
@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('static/images', filename)

# Serve CSS
@app.route('/styles.css')
def serve_css():
    return send_from_directory('static', 'styles.css')

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 404

@app.errorhandler(500)
def server_error(e):
    return "Internal Server Error", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)