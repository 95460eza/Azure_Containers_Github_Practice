
# The "redis" package brings an INTERFACE to INTERACT with the Redis in-memory data store USING Python code to store/retrieve data, or utilize other Redis features
import redis
from flask import Flask, render_template, request
from student import Student


app = Flask(__name__)
#app.config["DEBUG"] = True


# "container_redisdb" below is a "DNS name" that the DNS resolver (built in) should resolve to the ACTUAL IP address of your container
# With Docker-Compose when defining BOTH service1 (container_redisdb) AND service2 (container based on this file) under the SAME network (mynetwork), Docker creates a BRIDGE NETWORK
# allowing ALL containers on THAT network to communicate through their service names (service1 and service2), which act as DNS names within the network.
#conn = redis.Redis(host='localhost', port=6379, db=0)
conn = redis.Redis(host='container_redisdb', port=6379, db=0)

try:
    conn.ping()
except redis.exceptions.ConnectionError as err:
    raise err


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/handle_data", methods=["POST"])
def handle_data():
    stud = Student(request, conn)
    stud.get_values()
    err = stud.record_student()
    if err:
        return render_template("error.html")
    #print(type(results))
    results = stud.get_all_students()
    return render_template("result.html", results=results)


#if __name__ == "__main__":
#    app.run("0.0.0.0", 8000)