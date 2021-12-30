import json
import pandas as pd
from team import Team
from tournament import Tournament
from match import Match


def to_dict(obj):
    json_data = json.dumps(obj.__dict__, default=lambda o: o.__dict__)
    return json.loads(json_data)


def load_played():
    table = pd.read_csv('result_played.csv')
    table_rows = table.to_dict(orient='records')
    return table_rows


def load_upcoming():
    table = pd.read_csv('result_upcoming.csv')
    table_rows = table.to_dict(orient='records')
    return table_rows


def get_matches(team=None, status=None, tournament=None):
    matches = []
    upcoming = load_upcoming()
    played = load_played()
    for row in upcoming:
        if (team is None or team == row['home_team'] or team == row['away_team'])\
                and (status is None or status == 'upcoming')\
                and (tournament is None or tournament == row['tournament']):
            match = Match(
                home_team=Team(name=row['home_team']),
                away_team=Team(name=row['away_team']),
                start_time=row['start_time'],
                kickoff=row['kickoff'],
                tournament=Tournament(name=row['tournament']),
                status='upcoming'
            )
            matches.append(to_dict(match))
    for row in played:
        if (team is None or team == row['home_team'] or team == row['away_team'])\
                and (status is None or status == 'played') \
                and (tournament is None or tournament == row['tournament']):
            match = Match(
                home_team=Team(name=row['home_team']),
                away_team=Team(name=row['away_team']),
                start_time=row['start_time'],
                kickoff=row.get('kickoff'),
                tournament=Tournament(name=row['tournament']),
                status='played',
                home_score=row['home_score'],
                away_score=row['away_score']
            )
            matches.append(to_dict(match))
    return json.dumps(matches)


if __name__ == '__main__':
    result = get_matches('Sutton United', status='upcoming', tournament='fa')
    print(result)
