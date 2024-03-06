
#import redis
#from flask import render_template, request
#from student import Student
#import docker
import azure.functions as func
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Natou Mon BEBE. Manifeste!! LOL"

# Azure Function handler
def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(app).handle(req)


# @app.route("/handle_data", methods=["POST"])
# def handle_data():
#     stud = Student(request, conn)
#     stud.get_values()
#     err = stud.record_student()
#     if err:
#         return render_template("error.html")
#     #print(type(results))
#     results = stud.get_all_students()
#     return render_template("result.html", results=results)


# Flask DEVELOPMENT SERVER not needed BELOW because using GUNICORN PRODUCTION SERVER in Dockerfile.GUNICORN must be requirements.txt file.
# The command is: CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main_CONTAINER_for_APP_STAND_ALONE:app"]
#if __name__ == "__main__":
#    app.run("0.0.0.0", 8000)
