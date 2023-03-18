from flask import Flask, render_template

imams = Flask(__name__)


@imams.route("/")
def hello_world():
    # return render_template("historical.html")
    return render_template("base.html")


@imams.route("/imams")
def the_imams():
    return render_template("Imam.html")


@imams.route("/historical")
def historical():
    return render_template("historical.html")

# if __name__ == '__main__':
#     imams.run(host='0.0.0.0', debug=True)
