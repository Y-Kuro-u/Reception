from flask import *
app = Flask(__name__)

def process_request(post_request):
    global attendees
    try:
        attendees[post_request["name"]] = post_request["exit"]
    except:
        pass

@app.route("/",methods=["GET","POST"])
def main_process():
    global attendees
    return render_template("index.html",attendees = attendees)

@app.route("/add_list",methods=["POST"])
def add_list():
    global attendees
    if request.method == "POST":
        process_request(request.form)
        return render_template("index.html",attendees = attendees)

    else:
        return render_template("index.html",attendees = attendees)

@app.route("/delete_list",methods=["POST"])
def delete_list():
    try:
        global attendees
        name = request.form["name"]
        if name in attendees:
            del attendees[name]
        return render_template("index.html",attendees = attendees)
    
    except:
        return render_template("index.html",attendees = attendees)

if __name__ == "__main__":
    attendees = {}
    app.run()