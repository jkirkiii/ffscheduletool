import player as p

class Team:
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else None
        self._players = kwargs['players'] if 'players' in kwargs else []
    
    def name(self, n = None):
        if n: self._name = n
        return self._name
    
    def players(self, p = None):
        if p: self._players = p
        return self._players
    
    def addPlayer(self, player):
        for p in self.players():
            if p.name() == player.name():
                print('Player is already on the team!\n')
                return
        self.players().append(player)
        print('Player added!\n')
    
    def removePlayer(self, player):
        for p in self.players():
            if p.name() == player:
                self.players().pop(self.players().index(p))
                print(f'{p.name()} has been removed.\n')
                return
        print(f'{player} not found.')
    
    def __str__(self):
        output = f'{self.name()}\n'
        for p in self.players():
            output += f'{p.position()} {p.name()}, {p.team()}\n'
        return output
        
if __name__ == '__main__':
    roster = [ p.Player(name='Kyler Murray', position='QB', team='AZ'),
              p.Player(name='Alvin Kamara', position='RB', team='NO'),
              p.Player(position='WR', team='KC', name='Tyreek Hill') ]
    team1 = Team(name='Cascadia Trashrats', players=roster)
    print(team1)
    team1.addPlayer(p.Player(name='Mike Adams', position='RB', team='ATL'))
    print(team1)
    team1.addPlayer(p.Player(name='Tyreek Hill', position='WR', team='KC'))
    print(team1)
    team1.removePlayer('Mike Adams')
    print(team1)