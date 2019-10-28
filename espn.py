import requests
import json

"""
Hockey (NHL) competitions also include:
	awayScore Away team score at time of the play. 		
	homeScore Home team score at time of the play. 		
	athletesInvolved Array of athlete IDs involved in the play. Ranked in order of importance. 		
	teamId Team ID of the team involved in the play. 		
	xCoordinate The x coordinate of where the play occurred on the ice. 		
	yCoordinate The y coordinate of where the play occurred on the ice. 		
	strength Object indicating power-play situation, with the following properties: 		
	id - The ID associated with the strength type. 		
	description - String description associated with the strength type, e.g. "even" or "shorthanded." 
"""





r = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?region=us&lang=en&contentorigin=espn&limit=100&calendartype=blacklist&includeModules=videos%2Ccards&dates=20191027&buyWindow=1m&showAirings=buy%2Clive&showZipLookup=true')

r= json.dumps(r.json(), sort_keys=True, indent=4)
r = json.loads(r)
games = r["events"]
i = 0


while(i < len(games)):
	game = r["events"][i]
	rr = game["competitions"][0]
	home_team_info = game["competitions"][0]["competitors"][0]
	home_team_name = home_team_info["team"]["displayName"]
	home_team_score = home_team_info["score"]
	
	away_team_info = game["competitions"][0]["competitors"][1]
	away_team_name = away_team_info["team"]["displayName"]
	away_team_score = away_team_info["score"]
	if(home_team_info["winner"] == True and (rr["status"]["featuredAthletes"][0]["athlete"]["team"]["id"] == home_team_info["team"]["id"])):
		home_team_goalie = (rr["status"]["featuredAthletes"][0]["athlete"]["displayName"],rr["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])
		away_team_goalie = (rr["status"]["featuredAthletes"][1]["athlete"]["displayName"],rr["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
	else:
		home_team_goalie = (rr["status"]["featuredAthletes"][1]["athlete"]["displayName"],rr["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
		away_team_goalie = (rr["status"]["featuredAthletes"][0]["athlete"]["displayName"],rr["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])


	print("\n")
	print(("{} @ {}".center(70, ' ')).format(away_team_name, home_team_name))
	print(("{} - {}".center(99, ' ')).format(away_team_score,home_team_score))
	print(("{} - {}".center(45, ' ')).format(away_team_goalie,home_team_goalie))
	print("\n")

	i = i + 1