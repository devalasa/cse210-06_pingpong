from game.casting.color import Color
# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Ping Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2
BALL_MAX_POINT_LOW = CENTER_Y + 210

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "game/assets/fonts/Tango_chips.ttf"
FONT_SIZE = 30

# SOUND
BOUNCE_SOUND = "game/assets/sounds/bouncing.wav"
WELCOME_SOUND = "game/assets/sounds/start.wav"
OVER_SOUND = "gameg/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
GREEN = Color(65, 220, 125)
BLUE = Color(0, 93, 243)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
ENTER = "enter"
PLAYER_1_UP = "q"
PLAYER_1_DOWN = "a"
PLAYER_2_UP = "p"
PLAYER_2_DOWN = "l"

# SCENES
NEW_GAME = 0
NEXT_SCENE = 1
IN_PLAY = 2
CONTINUE = 3
GAME_OVER = 4

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# SCORE STATS [NOT HUD]
SCORE_STATS_GROUP = "scorestats"

# HUD
HUD_MARGIN = 5
MAXIMUM_SCORE = 11
SCORE_1_GROUP = "score_1"
SCORE_2_GROUP = "score_2"
PLAYER_1_SCORE_FORMAT = "PLAYER 1 : {} "
PLAYER_2_SCORE_FORMAT = "PLAYER 2 : {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "game/assets/images/ball.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "RACKETs"
RACKET_IMAGE = "game/assets/images/racket.jpg"
RACKET_WIDTH = 28
RACKET_HEIGHT = 106
RACKET_RATE = 6
RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
CONTINUE_MESSAGE = "GAME WOULD CONTINUE IN A MOMENT"
ENTER_TO_START = "PRESS ENTER TO START"
PLAYER_WINS_MESSAGE = "GAME ENDED"


# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 0
MAXIMUM_LIVES = 11
