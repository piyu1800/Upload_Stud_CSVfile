from flask_restful import Resource, reqparse
from Student_app import app 
from Student_app.models.models import Student
import werkzeug
from Student_app.services.services import StudentServices


class Student_csv(Resource):
    def get(self):
        return "Welcome to APIs which will add student in CSV"

    
class CSV_file(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        print('Parse:',reqparse)
        parse.add_argument('file',type=werkzeug.datastructures.FileStorage,location='files')
        args=parse.parse_args()
        csv_file =args['file']
        print('CSV file:', csv_file)
        return StudentServices().uploadFiles(args['file'])

    
