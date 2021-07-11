from collections import defaultdict

def tally(rows):
    standings = ["Team                           | MP |  W |  D |  L |  P"]

    teams = {}
    teams = defaultdict(lambda: {'w': 0, 'd': 0, 'l': 0, 'p': 0})
    for row in rows:
        team1, team2, result = row.split(';')

        if result.lower() == 'win':
            teams[team1]['w'] += 1
            teams[team1]['p'] += 3
            teams[team2]['l'] += 1
        elif result.lower() == 'loss':
            teams[team2]['w'] += 1
            teams[team2]['p'] += 3
            teams[team1]['l'] += 1
        else:
            teams[team1]['d'] += 1
            teams[team2]['d'] += 1
            teams[team1]['p'] += 1
            teams[team2]['p'] += 1

    teams = sorted(teams.items(), key=lambda x: (-1 * x[1]['p'], x[0]))

    for team, results in teams:
        mp = results['w'] + results['d'] + results['l']
        standings.append("{:30} | {:2} | {:2} | {:2} | {:2} | {:2}".format(
            team, mp, results['w'], results['d'], results['l'], results['p']))

    return standings
