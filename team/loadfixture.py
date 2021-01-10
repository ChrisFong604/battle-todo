import json

player_fixtures = [
    {
        'model': 'team.player',
        'pk': 1,
        'fields': {
            'player_name': 'a',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 2,
            'special_attack': 5,
            'special_defense': 2,
            'speed': 5
        }
    },
    {
        'model': 'team.player',
        'pk': 2,
        'fields': {
            'player_name': 'b',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 6,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 3,
        'fields': {
            'player_name': 'c',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 5,
            'special_attack': 2,
            'special_defense': 3,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 4,
        'fields': {
            'player_name': 'd',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 4,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 6
        }
    },
    {
        'model': 'team.player',
        'pk': 5,
        'fields': {
            'player_name': 'e',
            'player_points': 0,
            'player_team': 1,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 5,
            'physical_defense': 6,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 6,
        'fields': {
            'player_name': 'f',
            'player_points': 0,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 5,
            'special_defense': 4,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 7,
        'fields': {
            'player_name': 'g',
            'player_points': 0,
            'player_team': 2,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 4,
            'physical_defense': 1,
            'special_attack': 1,
            'special_defense': 4,
            'speed': 2
        }
    },
    {
        'model': 'team.player',
        'pk': 8,
        'fields': {
            'player_name': 'h',
            'player_points': 0,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 9,
            'special_defense': 1,
            'speed': 1
        }
    },
    {
        'model': 'team.player',
        'pk': 9,
        'fields': {
            'player_name': 'i',
            'player_points': 0,
            'player_team': 2,
            'player_special_select': True,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 1,
            'physical_defense': 1,
            'special_attack': 5,
            'special_defense': 1,
            'speed': 5
        }
    },
    {
        'model': 'team.player',
        'pk': 10,
        'fields': {
            'player_name': 'j',
            'player_points': 0,
            'player_team': 2,
            'player_special_select': False,
            'has_attacked': False,
            'damage_dealt': 0.0,
            'todo_points': 10,
            'physical_attack': 2,
            'physical_defense': 6,
            'special_attack': 1,
            'special_defense': 2,
            'speed': 1
        }
    }
]

team_fixtures = [
    {
        'model': 'team.team',
        'pk': 1,
        'fields': {
            'team_name': 'team_1',
            'team_points': 0
        }
    },
    {
        'model': 'team.team',
        'pk': 2,
        'fields': {
            'team_name': 'team_2',
            'team_points': 0
        }
    } 
]

with open('team/fixtures/fixtures.json', 'w') as outfile:
    json.dump(team_fixtures + player_fixtures, outfile)