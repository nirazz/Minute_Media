

class Match:

    def __init__(self, home_team, away_team, start_time, kickoff, tournament, status='upcoming', home_score=None,
                 away_score=None):
        self.home_team = home_team
        self.away_team = away_team
        self.start_time = start_time
        self.kickoff = kickoff
        self.tournament = tournament
        self.status = status
        if home_score is not None:
            self.home_score = home_score
        if away_score is not None:
            self.away_score = away_score

    def set_status(self, status):
        self.status = status

    def set_score(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
