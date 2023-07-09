from flask import Flask,jsonify,request
import ipl



app=Flask(__name__)

#home page
@app.route('/')
def home():
    return "Hello World"

#1st api
@app.route('/api/teams')
def teams():
    teams=ipl.teams_api()
    return jsonify(teams)

#2nd api
#Required input from url
#http://127.0.0.1:5000/api/teamvsteam?team1=Chennai Super Kings&team2=Mumbai Indians
#? means ithun pahila input start honar aahe
#& means ithun dusra input start honar aahe
@app.route('/api/teamvsteam')
def teamvsteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    result=ipl.team1_vs_team2_api(team1,team2)
    return jsonify(result)

#3rd api
@app.route('/api/batsman-record')
def batsman_record():
    batter=request.args.get('batsman')
    result=ipl.calculate_batsman_record(batter)
    return result






app.run(debug=True)

#Postman -To test api