# Initial Conditions
BOARD_SIZE = (100,100)
MAX_BOARD_SIZE = 125
SCREEN_SIZE = (750,750)
FPS = 30

PALETTES = [
    ["fbf8cc", "fde4cf", "ffcfd2", "f1c0e8", "cfbaf0", "a3c4f3", "90dbf4", "8eecf5", "98f5e1", "b9fbc0"],
    ["001219", "005f73", "0a9396", "94d2bd", "e9d8a6", "ee9b00", "ca6702", "bb3e03", "ae2012", "9b2226"],
    ["9b5de5", "f15bb5", "fee440", "00bbf9", "00f5d4"],
    ["eec643","141414","eef0f2","0d21a1","011638"],
    ["ff0000","ff8700","ffd300","deff0a","a1ff0a","0aff99","0aefff","147df5","580aff","be0aff"],
    ["f72585","b5179e","7209b7","560bad","480ca8","3a0ca3","3f37c9","4361ee","4895ef","4cc9f0"],
    ["f4f1de","e07a5f","3d405b","81b29a","f2cc8f"],
    ["5f0f40","9a031e","fb8b24","e36414","0f4c5c"],
    ["006d77","83c5be","edf6f9","ffddd2","e29578"],
    ["ff1053","6c6ea0","66c7f4","c1cad6","ffffff"],
    ["b9e3c6","59c9a5","d81e5b","23395b","fffd98"]
]
# Current selected pallet in PALETTES list
CURRENT_PALLET = 0
# Draw modes:
#  0 - from center
#  1 - from top left
#  2 - from top right
#  3 - from bottom left
#  4 - from bottom right
#  5 - wandering
DRAW_MODE = 5
# 1 for gradient, 0 for hard color changes
COLOR_BLEND = False