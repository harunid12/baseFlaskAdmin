from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard')
def home():
    return render_template('dashboard/view.html')

if __name__ == '__main__':
    app.run(debug=True)