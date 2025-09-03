from .App import app
from config import ABOUT

@app.route('/')
def index():
    return "Hello world !"

@app.route('/about/')
def about():
    return ABOUT

@app.route('/contact/')
def contact():
    return "07.82.52.45.37"

if __name__ == "__main__":
    app.run()