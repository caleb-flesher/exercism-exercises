# Using serpensta's solution
BAND_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def label(colors):
    pref_ohms = (10 * BAND_COLORS.index(colors[0]) + BAND_COLORS.index(colors[1])) * (10 ** BAND_COLORS.index(colors[2]))
    
    if pref_ohms > 1000000000:
        pref = "giga"
        pref_ohms //= 1000000000
    elif pref_ohms > 1000000:
        pref = "mega"
        pref_ohms //=1000000
    elif pref_ohms > 1000:
        pref = "kilo"
        pref_ohms //=1000
    else:
        pref = ""
    
    return f"{pref_ohms} {pref}ohms"
