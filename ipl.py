#All code of extracting data from ipl dataset will go here
import numpy as np
import pandas as pd

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
df=pd.read_csv(ipl_matches)

def teams_api():
    teams= list(df['Team1'].unique())
    team_dict={
        'teams':teams
    }
    return team_dict

def team1_vs_team2_api(team1,team2):
  matches=df[((df['Team1']==team1) | (df['Team1']==team2)) & ((df['Team2']==team1) | (df['Team2']==team2))].shape[0]
  matches_won_by_team_1=df[((df['Team1']==team1) | (df['Team1']==team2)) & ((df['Team2']==team1) | (df['Team2']==team2)) & (df['WinningTeam']==team1)].shape[0]
  matches_won_by_team_2=df[((df['Team1']==team1) | (df['Team1']==team2)) & ((df['Team2']==team1) | (df['Team2']==team2)) & (df['WinningTeam']==team2)].shape[0]
  draws=matches-(matches_won_by_team_1+matches_won_by_team_2)
  response={
      "total_matches":matches,
      f"Matches won by {team1}":matches_won_by_team_1,
      f"Matches won by {team2}":matches_won_by_team_2,
      "No result":draws
  }
  return response





