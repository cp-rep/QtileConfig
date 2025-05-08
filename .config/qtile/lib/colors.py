## colors.py


DoomOne = [
    ["#282c34ee", "#282c34dd"], # bg
    ["#bbc2cfee", "#bbcc2cfdd"], #fg
    ["#1c1f24", "#1c1f24"], # color01
    ["#ff6c6b", "#ff6c6b"], # color02
    ["#98be65", "#98be65"], # color03
    ["#da8548", "#da8548"], # color04
    ["#51afef", "#51afef"], # color05
    ["#c678dd", "#c678dd"], # color06
    ["#46d9ff", "#46d9ff"] # color07
]


Dracula = [
    ["#282a36ee", "#282a36dd"], # bg 0 - black
    ["#f8f8f2ee", "#f8f8f2dd"], #fg 1 - white
    ["#000000", "#000000"], # color 2 - transparent
    #["#ff5555", "#ff5555"], # color 3 - red
    ["#ffb15f", "#ffb15f"], # color 3 - orange
    ["#50fa7b", "#50fa7b"], # color 4 - green
    ["#f1fa8c", "#f1fa8c"], # color 5 - yellow
    ["#bd93f9", "#bd93f9"], # color 6 - purple
    ["#ff79c6", "#ff79c6"], # color 7 - pink
    ["#9aedf3", "#9aedf3"] # color 8 - light blue
    #["#ffb15f", "#ffb15f"] # color07
]


# Template = [
#     ["", ""], # bg
#     ["", ""], #fg
#     ["", ""], # color01
#     ["", ""], # color02
#     ["", ""], # color03
#     ["", ""], # color04
#     ["", ""], # color05
#     ["", ""], # color06
#     ["", ""] # color07
#     ]

# Set this to the defined color palette above to change the qtile color scheme
# While the color palettes are correct, to get nice looking output the colors
# Should be changed manually in the other qtile/lib files. e.g colors[0...8]
colors = Dracula
