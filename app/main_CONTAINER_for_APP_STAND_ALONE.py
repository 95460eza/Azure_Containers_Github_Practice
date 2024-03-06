
#import redis
#from flask import render_template, request
#from student import Student
#import docker
import azure.functions as func
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "La VRAIE Mme Koffi? C'est Natou Mon AMOUR hein !!"


# WITH Python programming model v2 for Azure Functions, you MUST DECLARE the HTTP trigger itself using a decorator

# APPROACH 1 - The "Trigger function" uses a decorator and ALSO handles the HTTP request directly via func.WsgiMiddleware(my_wsgi_app).handle(req) that PROCESSES the request
#@func.HttpTrigger(methods=['GET'], route='/')
#def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
#    return func.WsgiMiddleware(app).handle(req)

# APPROACH 2 - The separate function "main" handles the PROCESSING LOGIC via func.WsgiMiddleware(app).handle(req).
# Then the trigger function is decorated with @func.HttpTrigger and delegates the actual request handling to the main function by calling return main(req).
# Azure Function handler: handles the PROCESSING LOGIC
#def main(req: func.HttpRequest) -> func.HttpResponse:
#    return func.WsgiMiddleware(app).handle(req)


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Pass the request to the WSGI application
    wsgi_response = func.WsgiMiddleware(app).handle(req)

    # Convert the WSGI response to Azure Functions' HttpResponse
    status, headers, body = wsgi_response
    return func.HttpResponse(body.decode(), status_code=int(status.split()[0]), headers=dict(headers))


# The trigger function delegates the request handling to the main function by calling return main(req).
# @func.HttpTrigger(methods=['GET', 'POST'], route='example')
#@func.HttpTrigger(methods=['GET'], route='/')
#def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
#    return main(req)




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
