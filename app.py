from flask import Flask, render_template,jsonify

app=Flask(__name__,template_folder='templates')

Jobs = [
    {
        "id":'1',
        "title":'Data Analyst',
        "location":'Roorkee, Uttarakhand',
        "Salary":'1,00,000'
    },
    {
        "id":'2',
        "title":'Data Engineer',
        "location":'Roorkee, Uttarakhand',
        "Salary":'12,00,000'
    },
    {
         "id":'3',
        "title":'Web Developer',
        "location":'Roorkee, Uttarakhand',
        "Salary":'14,00,000'
    },
    {
         "id":'4',
        "title":'Blockchain Developer',
        "location":'Roorkee, Uttarakhand',
        "Salary":'16,00,000'
    }
]

@app.route("/")

def home():
    return render_template('home.html', jobs=Jobs)

@app.route("/api/jobs")

def list_jobs():
    return jsonify(Jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)