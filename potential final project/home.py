from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route("/product")
def product():
    return render_template("OurProducts.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("AboutUs.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

