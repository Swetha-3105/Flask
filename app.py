from flask import Flask
project=Flask(__name__)
@project.route("/")
def webapp():
    return "Welcome World!!!"

if __name__ == "__main__":
     project.run(debug=True) 