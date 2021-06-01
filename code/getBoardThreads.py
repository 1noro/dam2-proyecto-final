@app.route('/<slug>/threads', methods=["GET"])
def ping(slug):
    data = None
    with open(db_file, 'r') as file:
        data = json.load(file)
    with open(db_file, 'w') as file:
        if name not in data:
            data[name] = {}
        data[name]["ip"] = request.remote_addr
        data[name]["timestamp"] = datetime.timestamp(datetime.now())
        data[name]["active"] = True
        json.dump(data, file)
    return "pong", 201