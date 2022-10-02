from Student_app import api 
from Student_app.controller.controller import Student_csv, CSV_file

api.add_resource(Student_csv, '/api/v1/csv')
api.add_resource(CSV_file,'/api/csvfile')