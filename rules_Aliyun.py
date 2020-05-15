BRIDGES = {
    'WORLDWIDE': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 91,    'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'ON',  'ON': [91,], 'OFF': [46001], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 1, 'TGID': 91, 'ACTIVE': True,'TIMEOUT': 15, 'TO_TYPE': 'NONE',  'ON': [91,], 'OFF': [], 'RESET': []},
                 ],
    'CN46001TS1': [
            {'SYSTEM': 'MASTER-1',    'TS': 1, 'TGID': 46001,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [46001,], 'OFF': [8,10], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 2, 'TGID': 46001,   'ACTIVE': True, 'TIMEOUT': 2, 'TO_TYPE': 'NONE', 'ON': [46001,], 'OFF': [8,10], 'RESET': []},
                 ],
    'CN46001TS2': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 46001, 'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'ON', 'ON': [46001,], 'OFF': [91], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 1, 'TGID': 46001, 'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'NONE', 'ON': [46001,], 'OFF': [], 'RESET': []},
                 ],
    'HOME166': [
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 166, 'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'NONE', 'ON': [166], 'OFF': [46001,91,73], 'RESET': []},
            {'SYSTEM': 'REPEATER-1',    'TS': 1, 'TGID': 46005, 'ACTIVE': False, 'TIMEOUT': 15, 'TO_TYPE': 'NONE', 'ON': [5,], 'OFF': [6,10], 'RESET': []},
               ],
    'TG73': [                                                                        
            {'SYSTEM': 'MASTER-1',    'TS': 2, 'TGID': 73, 'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'NONE', 'ON': [73,], 'OFF': [46001,91], 'RESET': []},
            {'SYSTEM': 'REPEATER-2',    'TS': 2, 'TGID': 22317, 'ACTIVE': True, 'TIMEOUT': 15, 'TO_TYPE': 'NONE', 'ON': [22317,], 'OFF': [5,10], 'RESET': []},
               ]
           }

if __name__ == '__main__':
   from pprint import pprint
   pprint(BRIDGES)
