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




# http://api.espn.com/v1/sports/hockey/nhl ?



r = requests.get('https://site.web.api.espn.com/apis/v2/scoreboard/header?sport=hockey&league=nhl&region=us&lang=en&contentorigin=espn&buyWindow=1m&showAirings=buy%2Clive%2Creplay&showZipLookup=true&tz=America/New_York')

r= json.dumps(r.json(), sort_keys=True, indent=4)
r = json.loads(r)
r = r["sports"][0]["leagues"][0]["events"]

print(json.dumps(r,indent=4))