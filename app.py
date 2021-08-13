from flask import Flask, render_template
import json

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/projects', methods=['GET'])
def projects():
    with open('jsons/projects.json', 'r') as f:
        projects = json.load(f)
        f.close()
    return render_template('projects.html', projects=projects)

@app.route('/contacts', methods=['GET'])
def contacts():
    with open('jsons/contacts.json', 'r') as f:
        contacts = json.load(f)
        f.close()
    return render_template('contacts.html', contacts=contacts)

@app.route('/projects/<int:id>', methods=['GET'])
def project(id):
    with open('jsons/projects.json', 'r') as f:
        projects = json.load(f)
        f.close()
    project = projects[id]
    return render_template('project.html', project=project)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)