from flask import Flask, render_template

imams = Flask(__name__)


@imams.route("/")
def hello_world():
    # return render_template("imam.html")
    return render_template("main.html")


@imams.route("/imams")
def his_imam():
    return render_template("imam.html")



# if __name__ == '__main__':
#     imams.run(host='0.0.0.0', debug=True)
