from flask import Flask, render_template, redirect, request, jsonify, make_response, send_file, session, url_for
from flask_restful import Resource, Api
from dataframe import main
import os

app = Flask(__name__)
api = Api(app)
app.secret_key = ' key'

@app.route('/',methods=['POST', 'GET'])
def index():
    return render_template('home.html')

@app.route('/data', )
def data():
    if not session.get('form_submitted'):
        return redirect(url_for('home'))
    
    return render_template('data.html')

@app.route('/result/Datalix.xlsx')
def download_file():
    path = './result/Datalix.xlsx'
    return send_file(path, as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

class result(Resource):
    def post(self):
        session['form_submitted'] = True
        job =  request.form['job-name']
        location = request.form['job-location']
        res = {'job':job,'location':location}
        resume = request.files['file']
        filename = resume.filename
        basename, extension = os.path.splitext(filename)
        user_resume = f'user_resume{extension}' 
        # os.rename(filename, user_resume)
        resume.save(os.path.join('./data', user_resume))
        main(res) 
        
        # return a redirect response to the '/data' page
        response = make_response(redirect('/data'))
        return response
    
    def get(self):
        # return an error message for GET requests
        return {'message': 'This endpoint only accepts POST requests.'}, 405

api.add_resource(result, '/result')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 8080, debug=True)