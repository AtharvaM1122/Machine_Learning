# Get thresholds for beginner mode
def get_thresholds_beginner():
    _ANGLE_HIP_KNEE_VERT = {
        'NORMAL': (0, 32),
        'TRANS': (35, 65),
        'PASS': (70, 95)
    }

    _ANGLE_ELBOW_CURL = {
        'NORMAL': (150, 180),  # Arm fully extended
        'TRANS': (90, 150),    # Mid curl
        'PASS': (30, 90)       # Fully bent
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 45,
        'KNEE_THRESH': [50, 70, 95],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50
    }

    # Add Bicep Curl Thresholds
    thresholds['ELBOW_CURL'] = _ANGLE_ELBOW_CURL

    return thresholds


# Get thresholds for pro mode
def get_thresholds_pro():
    _ANGLE_HIP_KNEE_VERT = {
        'NORMAL': (0, 32),
        'TRANS': (35, 65),
        'PASS': (80, 95)
    }

    _ANGLE_ELBOW_CURL = {
        'NORMAL': (150, 180),  # Arm fully extended
        'TRANS': (90, 150),    # Mid curl
        'PASS': (30, 90)       # Fully bent
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [15, 50],
        'ANKLE_THRESH': 30,
        'KNEE_THRESH': [50, 80, 95],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50
    }

    # Add Bicep Curl Thresholds
    thresholds['ELBOW_CURL'] = _ANGLE_ELBOW_CURL

    return thresholds
