from flask import Flask,render_template,jsonify
app = Flask(__name__)
JOBS =[
  {'id':1,
  'title':'Data Analyst',
  'location':'Parow',
  'salary': 'R90000'
  },
  {'id':2,
  'title':'Data Processor',
  'location':'Goodwood',
  'salary': 'R190000'
  },
  {'id':3,
  'title':'Web Designer',
  'location':'Bellville',
  'salary': 'R90000'
  },
  {'id':4,
  'title':'AE Programmer',
  'location':'Parow',
  'salary': 'R80000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

  
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
  