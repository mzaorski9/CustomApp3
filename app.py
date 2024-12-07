from flask import Flask, render_template, jsonify

app = Flask(__name__)


jobs = [
    { 
        'id': 1,
        'position': 'Frontend Engineer',
        'type': 'remote',
        'location': "Warsaw",
        'salary': 15000
     },
     { 
        'id': 2,
        'position': 'Backend Engineer',
        'type': 'remote',
        'location': 'Wroclaw',
        'salary': 25000
     },
     { 
        'id': 3,
        'position': 'Data Scientist',
        'type': 'hybrid',
        'location': 'Gdansk',
        'salary': 20000
     },
        { 
        'id': 4,
        'position': 'Software Engineer',
        'type': 'remote',
        'location': 'Warsaw',
        'salary': 16000
     }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=jobs,
                           company_name="XYZ")
@app.route("/jobs")
def render_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run('0.0.0.0', port=7777, debug=True)
