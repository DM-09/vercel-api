from flask import Flask, jsonify, Response
import requests as req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/PS", methods=['GET'])
def GetSolvedCount():
    URL = ['https://happydm09.github.io/Page/json/solved.json', 'https://solved.ac/api/v3/user/show?handle=dongmin']

    try:
        data = req.get(URL[0]).json()
        baekjoon = req.get(URL[1]).json()

        datas = [baekjoon['solvedCount'], data['NYPC'], data['codeforces'], data['programmers']]

        json_file = {'baekjoon': datas[0], 'NYPC': datas[1],
                     'codeforces': datas[2], 'programmers': datas[3],
                     'All': sum(datas)}
    except:
        return Response('Error', 404)
    return jsonify(json_file), 200
