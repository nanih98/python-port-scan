class LogColors:
    BLUE1 = '\033[95m'
    BLUE2 = '\033[96m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    NOCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    START_ERROR = ERROR + 'ERROR |X| '
    START_WARNING = WARNING + '|·| '
    START_INFO = BLUE2 + '|·| '
    START_TITLE = WARNING + '  |·'
    START_SUBTITLE = BLUE1 + '  |·'
    START_SUBTITLE_2 = BLUE2 + '  |·'
    START_DEBUG = BLUE2 + '|DEBUG| '
    START_SUCCESS = SUCCESS + '|·| '
    LOADING = BLUE1 + 'ººº' + NOCOLOR
    INTERSECTION = ERROR + ' · '
