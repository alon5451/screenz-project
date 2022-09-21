import os
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from mocked_mdb import MockedMongoDB, Lecture
import json
import dataclasses

db = MockedMongoDB()
app = Flask(__name__, static_url_path='', static_folder='../client/build')


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api")
def api() -> str:
    return {
        "message": "Screenz-Project API is up & running"
    }

@app.route("/lecture")
def lectures() -> Lecture:
    lecture_id: int = int(request.args.get('id'))

    lecture_data: Lecture = db.find_one({'id': lecture_id})
    lecture_data_dict: dict = dataclasses.asdict(lecture_data) 

    return json.dumps(lecture_data_dict)


if __name__ == "__main__":
    port=int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)