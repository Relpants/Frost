import requests
import json

"""
Hockey (NHL) competitions also include:
	awayScore Away team score at time of the play. 		
	homeScore Home team score at time of the play. 		
	athletes Involved Array of athlete IDs involved in the play. Ranked in order of importance. 		
	teamId Team ID of the team involved in the play. 		
	xCoordinate The x coordinate of where the play occurred on the ice. 		
	yCoordinate The y coordinate of where the play occurred on the ice. 		
	strength Object indicating power-play situation, with the following properties: 		
	id - The ID associated with the strength type. 		
	description - String description associated with the strength type, e.g. "even" or "shorthanded." 
"""

class Team:
	def __init__(self):
		self.__name = ""	# __ double underscore indicates private member
		self.__logo = ""
		self.__score = 0
		self.__goalie = ("","")
	def setName(self, name):
		self.__name = name
	def setLogo(self, logo):
		self.__logo = logo
	def setScore(self, score):
		self.__score = score
	def setStartingGoalie(self, goalieName, savepct):
		self.__goalie = (goalieName, savepct)

	def getName(self):
		return self.__name
	def getLogo(self):
		return self.__logo
	def getScore(self):
		return self.__score
	def getStartingGoalie(self):
		return self.__goalie


def make_request(date):
	resp = requests.get('https://site.web.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?region=us&lang=en&contentorigin=espn&limit=100&calendartype=blacklist&includeModules=videos%2Ccards&dates='+date+'&buyWindow=1m&showAirings=buy%2Clive&showZipLookup=true')
	resp = json.dumps(resp.json(), sort_keys=True, indent=4)
	r = json.loads(resp)
	return r

def start(date):

	r = make_request(date)
	num_of_games = r["events"]
	i = 0

	home_team_list = []
	away_team_list = []

	while(i < len(num_of_games)):

		home_team = Team()
		away_team = Team()
		game = r["events"][i]
		game_stats = game["competitions"][0]

		home_team_info = game["competitions"][0]["competitors"][0]
		home_team.setName(home_team_info["team"]["displayName"])
		home_team.setLogo(home_team_info["team"]["logo"])
		home_team.setScore(home_team_info["score"])

		away_team_info = game["competitions"][0]["competitors"][1]
		away_team.setName(away_team_info["team"]["displayName"])
		away_team.setLogo(away_team_info["team"]["logo"]) 
		away_team.setScore(away_team_info["score"]) 

		#I
		if(home_team_info["winner"] == True and (game_stats["status"]["featuredAthletes"][0]["athlete"]["team"]["id"] == home_team_info["team"]["id"])):
			home_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][0]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])
			away_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][1]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
		else:
			home_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][1]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][1]["statistics"][6]["displayValue"])
			away_team.setStartingGoalie(game_stats["status"]["featuredAthletes"][0]["athlete"]["displayName"],game_stats["status"]["featuredAthletes"][0]["statistics"][6]["displayValue"])
		
		home_team_list.append(home_team)
		away_team_list.append(away_team)
		i = i + 1


	return home_team_list,away_team_list