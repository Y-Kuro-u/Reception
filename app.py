from flask import *
import os
import json

app = Flask(__name__)
PATH = "attendees_list.json"

def process_request(post_request):
    global attendees
    try:
        attendees[post_request["name"]] = post_request["exit"]
        
        if attendees[post_request["name"]] == "○":
            attendees[post_request["name"]] = 1
        else:
            attendees[post_request["name"]] = 0

    except:
        pass

@app.route("/",methods=["GET","POST"])
def main_process():
    global attendees
    read_list()
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

@app.route("/read_list",methods=["POST"])
def read_list():
    global attendees
    if os.path.exists(PATH):
        with open(PATH,"r") as files:
            attendees = json.load(files)
    else:
        pass
    return render_template("index.html",attendees = attendees)


@app.route("/dump_list",methods=["POST"])
def dump_json():
    global attendees
    with open(PATH,"w") as f:
        json.dump(attendees,f,indent=4)
    return render_template("index.html",attendees = attendees)

"""
@app.route("echo",methods=["POST"])
def recognize():
    global attendees

    #受け取る形式(ローマ字ひらがな等にばらつきがあれば整えてあげる)
    name = request.json.get("queryResult").get("paarameters").get("name")
    if name in attendees:
        attendees[name] = "○"
    else:

        ###ここに名前を正しく受け取れなかった時の処理を書く
        pass
    dump_json()
    return render_template("index.html",attendees = attendees)
"""

if __name__ == "__main__":
    attendees = {}
    app.run()