from flask import Flask, jsonify, request, render_template
import json

app = Flask("__name__")

@app.route("/")
def dashbord():
    return render_template("dashbord.html")

@app.route("/reset")
def reset():
    data = {}
    data["tmp"] = []
    data["hum"] = []
    data["x"] = []
    f = open("state.json", "w", encoding="utf-8")
    f.write(json.dumps(data))
    f.close()
    return jsonify(data)

@app.route("/control")
def route():
    f = open("control.json", "r", encoding="utf-8")
    jsondata = f.read()
    f.close()
    jsondata = json.loads(jsondata)
    return jsonify(jsondata)

@app.route("/input-sensor", methods=["POST"])
def input_sensor():
    hum = float(request.form["hum"])
    tmp = float(request.form["tmp"])
    ido = float(request.form["ido"])
    kei = float(request.form["kei"])
    f = open("state.json", "r", encoding="utf-8")
    jsondata = f.read()
    f.close()
    dic = json.loads(jsondata)
    hums = dic["hum"]
    tmps = dic["tmp"]
    co2s = dic["co2"]
    x = dic["x"]
    hums.append(hum)
    tmps.append(tmp)
    co2s.append(co2)
    x.append(len(x))
    dic2 = {}
    dic2["hum"] = hums
    dic2["tmp"] = tmps
    dic2["x"] = x
    f = open("state.json", "w", encoding="utf-8")
    f.write(json.dumps(dic2))
    f.close()
    geo = """{ "type": "Point",
  "crs": { "type": "name",
    "properties": {
      "name": "Current Location"
       }
      },
  "coordinates": [%f, %f]
 }
    """%(kei, ido)
    f = open("point.geojson", "w", encoding="utf-8")
    f.write(geo)
    f.close()
    return jsonify(dic2)

@app.route("/get-state")
def get_state():
    f = open("state.json", "r", encoding="utf-8")
    data = f.read()
    f.close()
    data = json.loads(data)
    return jsonify(data)

@app.route("/get-geo")
def get_geo():
    f = open("point.geojson", "r", encoding="utf-8")
    data = f.read()
    f.close()
    data = json.loads(data)
    return jsonify(data)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80)
