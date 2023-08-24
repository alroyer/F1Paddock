CAR_MOTION_DATA_COUNT = 22
PARTICIPANT_DATA_COUNT = 22
LAP_DATA_COUNT = 22

CAR_SETUP_DATA_COUNT = 22
CAR_TELEMETRY_DATA_COUNT = 22
CAR_STATUS_DATA_COUNT = 22

FINAL_CLASSIFICATION_DATA_COUNT = 22
LOBBY_INFO_DATA_COUNT = 22

MARSHAL_ZONE_COUNT = 21

WEATHER_SAMPLES_COUNT = 56

NAME_OF_PARTICIPANT_COUNT = 48

PACKET_ID = {
    0: 'Motion',
    1: 'Session',
    2: 'Lap',
    3: 'Event',
    4: 'Participants',
    5: 'Car Setups',
    6: 'Car Telemetry',
    7: 'Car Status',
    8: 'Final Classification',
    9: 'Lobby Info',
    10: 'Car Damage',
    11: 'Session History',
    12: 'Tyre Sets',
    13: 'Motion Ex',
}

EVENT_STRING_CODE = {
    'SSTA': 'Session Started',
    'SEND': 'Session Ended',
    'FTLP': 'Fastest Lap',
    'RTMT': 'Retirement',
    'DRSE': 'DRS enabled',
    'DRSD': 'DRS disabled',
    'TMPT': 'Team mate in pits',
    'CHQF': 'Chequered flag',
    'RCWN': 'Race Winner',
    'PENA': 'Penalty Issued',
    'SPTP': 'Speed Trap Triggered',
    'STLG': 'Start lights',
    'LGOT': 'Lights out',
    'DTSV': 'Drive through served',
    'SGSV': 'Stop go served',
    'FLBK': 'Flashback',
    'BUTN': 'Button status',
    'RDFL': 'Red Flag',
    'OVTK': 'Overtake',
}

BUTTON_FLAGS = {
    0x00000001: 'Cross or A',
    0x00000002: 'Triangle or Y',
    0x00000004: 'Circle or B',
    0x00000008: 'Square or X',
    0x00000010: 'D-pad Left',
    0x00000020: 'D-pad Right',
    0x00000040: 'D-pad Up',
    0x00000080: 'D-pad Down',
    0x00000100: 'Options or Menu',
    0x00000200: 'L1 or LB',
    0x00000400: 'R1 or RB',
    0x00000800: 'L2 or LT',
    0x00001000: 'R2 or RT',
    0x00002000: 'Left Stick Click',
    0x00004000: 'Right Stick Click',
    0x00008000: 'Right Stick Left',
    0x00010000: 'Right Stick Right',
    0x00020000: 'Right Stick Up',
    0x00040000: 'Right Stick Down',
    0x00080000: 'Special',
    0x00100000: 'UDP Action 1',
    0x00200000: 'UDP Action 2',
    0x00400000: 'UDP Action 3',
    0x00800000: 'UDP Action 4',
    0x01000000: 'UDP Action 5',
    0x02000000: 'UDP Action 6',
    0x04000000: 'UDP Action 7',
    0x08000000: 'UDP Action 8',
    0x10000000: 'UDP Action 9',
    0x20000000: 'UDP Action 10',
    0x40000000: 'UDP Action 11',
    0x80000000: 'UDP Action 12',
}
