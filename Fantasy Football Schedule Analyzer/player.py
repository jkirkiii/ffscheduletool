class Player:
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else None
        self._position = kwargs['position'] if 'position' in kwargs else None
        self._team = kwargs['team'] if 'team' in kwargs else None
        
    def name(self, n = None):
        if n: self._name = n
        return self._name
    
    def position(self, p = None):
        if p: self._position = p
        return self._position
    
    def team(self, t = None):
        if t: self._team = t
        return self._team
    
    def __str__(self):
        return f'\nName: {self.name()}\nPosition: {self.position()}\nTeam: {self.team()}'
    
if __name__ == '__main__':
    p1 = Player(name='Kyler Murray', position='QB', team='Arizona Cardinals')
    print(p1)