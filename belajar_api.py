from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# objek flask
app = Flask(__name__)

# objek flask restfull
api = Api(app)

# objek flask cors
CORS(app)

identitas = {}
class ContohRes(Resource):
    def get(self):
        # response = {"msg":"Halo, ini daweng"}
        return identitas
    
    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']
        identitas['nama'] = nama 
        identitas['umur'] = umur
        response = {'msg': 'data berhasil'}
        return response

api.add_resource(ContohRes, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)