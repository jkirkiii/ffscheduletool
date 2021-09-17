import schedule
import team as t
import player as p

userTeam = t.Team()
entry = ''
gamePlayerCount = {}

def playerEntry():
    player = p.Player(name=input('Enter player name: '))
    player.team(input('Enter player team: '))
    player.position(input('Enter player position: '))
    print(player)
    userTeam.addPlayer(player)    


week2 = schedule.Schedule(name="Week 2", games=( ('NYG','WAS'), ('CIN','CHI'), ('HOU','CLE'), ('LAR','IND'),
                                        ('BUF','MIA'), ('NE','NYJ'), ('SF','PHI'), ('LV','PIT'),
                                        ('NO','CAR'), ('DEN','JAC'), ('MIN','ARI'), ('ATL','TB'),
                                        ('DAL','LAC'), ('TEN','SEA'), ('KC','BAL'), ('DET','GB')) )

userTeam.name(input('Enter your team name: '))

while entry != 'q':
    playerEntry()
    entry = input('Press \'q\' to quit, or any other key to enter another player: ')

print(userTeam)

for g in week2.games():
    pcount = 0
    for p in userTeam.players():
        if p.team() in g:
            pcount += 1
    gamePlayerCount.update({g: pcount})

print(gamePlayerCount)
