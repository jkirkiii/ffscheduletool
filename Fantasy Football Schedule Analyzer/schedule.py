class Schedule:
    TEAMS = dict(ARI='Arizona Cardinals', ATL='Atlanta Falcons', BAL='Baltimore Ravens', BUF='Buffalo Bills',
                 CAR='Carolina Panthers', CHI='Chicago Bears', CIN='Cincinnati Bengals', CLE='Cleveland Browns', 
                 DAL='Dallas Cowboys', DEN='Denver Broncos', DET='Detroit Lions', GB='Green Bay Packers',
                 HOU='Houston Texans', IND='Indianapolis Colts', JAC='Jacksonville Jaguars', KC='Kansas City Chiefs',
                 LV='Las Vegas Raiders', LAC='Los Angeles Chargers', LAR='Los Angeles Rams', MIA='Miami Dolphins',
                 MIN='Minnesota Vikings', NE='New England Patriots', NO='New Orleans Saints', NYG='New York Giants',
                 NYJ='New York Jets', PHI='Philadelphia Eagles', PIT='Pittsburgh Steelers', SF='San Francisco 49ers',
                 SEA='Seattle Seahawks', TB='Tampa Bay Buccaneers', TEN='Tennessee Titans', WAS='Washington Football team')
    
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else None
        self._games = kwargs['games'] if 'games' in kwargs else None
        
    def name(self, n = None):
        if n: self._name = n
        return self._name
    
    def games(self, g = None):
        if g: self._games = g
        return self._games
    
    def abbrev(self):
        output = f'{self.name()}\n'
        for g in self.games():
            output += ' vs '.join(g) + '\n'
        return output
    
    def __str__(self):
        output = f'{self.name()}\n'
        for g in self.games():
            output += self.TEAMS.get(g[0]) + ' vs ' + self.TEAMS.get(g[1]) + '\n'
        return output
    
if __name__ == '__main__':
    week1 = Schedule(name='Week 1', games=( ('DEN','NYG'), ('BAL','LV'), ('KC','CLE')))
    print(week1)
    print(week1.abbrev())