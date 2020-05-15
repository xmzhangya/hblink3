BRIDGES = {
    'WORLDWIDE': [
            {'SYSTEM': 'MASTER-1',    'TS': 1, 'TGID': 91,    'ACTIVE': False, 'TIMEOUT': 2, 'TO_TYPE': 'ON',  'ON': [2,], 'OFF': [9,10], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 1, 'TGID': 91, 'ACTIVE': False, 'TIMEOUT': 2, 'TO_TYPE': 'ON',  'ON': [2,], 'OFF': [9,10], 'RESET': []},
        ],
    'CHINESE': [
            {'SYSTEM': 'MASTER-1',    'TS': 1, 'TGID': 46001,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [3,], 'OFF': [8,10], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 1, 'TGID': 46001,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [3,], 'OFF': [8,10], 'RESET': []},
        ],
    'NATIVE': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 22317, 'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 2, 'TGID': 22317, 'ACTIVE': False, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [4,], 'OFF': [7,10], 'RESET': []},
        ]
}

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
