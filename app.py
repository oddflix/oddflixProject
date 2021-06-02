from flask import Flask, render_template
from py1337x import py1337x

app = Flask(__name__)
tor = py1337x(proxy='1337x.to')

@app.route("/")
def index():
    return "0"

@app.route('/<search>', defaults={'source': 0})
@app.route("/<string:search>/<int:source>")
def video(search,source):
    res = tor.search(search)
    gg = tor.info(res["items"][source]["link"])
    magnet = gg["magnetLink"]
    name = gg["name"]
    json = {"name":name, "magnet":magnet, "search":search, "searchSource":search+str(source)}
    return render_template("index.html",json=json)



if __name__ == '__main__':
    app.run(debug=True,port=5000)    