sharps = ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]
flats = ["G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb"]

nashvilleNumsMaj = ["I", "II", "III", "IV", "V", "VI", "VII*"]
nashvilleNumsMin = ["i", "ii", "iii", "iv", "v", "vi", "vii*"]

keys = {
    # Major Keys
    "C": {"C", "Dm", "Em", "F", "G", "Am", "Bdim"},
    "G": {"G", "Am", "Bm", "C", "D", "Em", "F#dim"},
    "D": {"D", "Em", "F#m", "G", "A", "Bm", "C#dim"},
    "A": {"A", "Bm", "C#m", "D", "E", "F#m", "G#dim"},
    "E": {"E", "F#m", "G#m", "A", "B", "C#m", "D#dim"},
    "B": {"B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"},
    "F#": {"F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"},
    "Db": {"Db", "Eb", "F", "Gb", "Ab", "Bb", "Cdim"},
    "Ab": {"Ab", "Bb", "Cm", "Db", "Eb", "Fm", "Gm"},
    "Eb": {"Eb", "F", "Gm", "Ab", "Bb", "Cm", "Ddim"},
    "Bb": {"Bb", "Cm", "Dm", "Eb", "F", "Gm", "A#dim"},
    "F": {"F", "Gm", "Am", "Bb", "C", "Dm", "Edim"},

    # Minor Keys
    "Am": {"Am", "Bdim", "C", "D", "E", "F", "G"},
    "Em": {"Em", "F#dim", "G", "Am", "Bm", "C", "D"},
    "Bm": {"Bm", "C#dim", "D", "E", "F#", "G", "A"},
    "F#m": {"F#m", "G#dim", "A", "B", "C#", "D", "E"},
    "C#m": {"C#m", "D#dim", "E", "F#", "G#", "A", "B"},
    "G#m": {"G#m", "A#dim", "B", "C#", "D#", "E", "F#"},
    "D#m": {"D#m", "F#dim", "F#", "G#", "A#", "B", "C#"},
    "Fm": {"Fm", "Gdim", "Ab", "Bb", "Cm", "Db", "Eb"},
    "Cm": {"Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"},
    "Gm": {"Gm", "Adim", "Bb", "C", "Dm", "Eb", "F"},
    "Dm": {"Dm", "Edim", "F", "Gm", "Am", "Bb", "C"},
    "Bbm": {"Bbm", "C#dim", "D", "Eb", "F", "G", "A"},
    "Abm": {"Abm", "Bbdim", "C", "Db", "Eb", "F", "Gb"},
    "Ebm": {"Ebm", "Fdim", "G", "Ab", "Bb", "C", "D"},
}


major_to_minor = {
        "C": "Am", "G": "Em", "D": "Bm", "A": "F#m", "E": "C#m", "B": "G#m",
        "F#": "D#m", "Db": "Bbm", "Ab": "Fm", "Eb": "Cm", "Bb": "Gm", "F": "Dm"
    }


naturals = ["A", "B", "C", "D", "E", "F", "G"]


def readChord(chord):    #Reads the important infomation to transpose chord
    root = ""
    extra = ""
    if not chord or chord[0] not in "ABCDEFG":
        print("Invalid Chord")
        return()
    if (len(chord)>1) and (chord[1] == "b" or chord[1] == "#"):   #The 'extra' stuff starts after the sharp or flat (for transposing purposes)
        root= chord[:2]
        extra = chord[2:]
    else:
        root = chord[0]
        extra = chord[1:]
    return(root, extra)


def findKey(chords):
    chords_set = set(chords.split())
    curr_key_shared = 0
    curr_key = chords[0][-1]          #Starts by assuming the key is the last note of the progression
    for key, notes in keys.items():
        notes_shared = len(notes.intersection(chords_set))   #How many notes does the progression share with this key?
        if notes_shared > curr_key_shared:
            curr_key_shared = notes_shared
            curr_key = key
    if (isMinor(chords.split()[-1])):       #if the progression resolves to a minor chord, switch to the realitive minor. Not foolproof but correct most of the time
            return major_to_minor[curr_key]
    return curr_key



def nextRoot(root, direction, interval):  #Finds next root noe
     notes = []
     if "b" in root: notes = flats
     else: notes = sharps
     if direction == "Down": interval = 12 - interval
     for _ in range(interval):
        root = notes[(notes.index(root)+1)%len(notes)]
     return root


def buildChord(chord, direction, interval): #Adds extension back on
    if not readChord(chord): print("Error")
    root, extra = readChord(chord)
    next = nextRoot(root, direction, interval)
    nextChord = next + extra
    print(nextChord)
    return nextChord


def transposeChords(chords, direction, interval): #Transposes full progression
    chords = chords.split()
    print(chords)
    transposed = []
    for chord in chords:
        transposed.append(buildChord(chord, direction, interval))
    output = ""
    for chord in transposed:
        output += (f"{chord} ")
    return output


def mapToKey(roots):    #returns an array of nautural notes starting on the natural version of the first note in the progression
    ordered_notes = []
    start = naturals.index(roots[0][0])
    for i in range(start, 7+start):
        ordered_notes.append(naturals[i%(7)])
    return ordered_notes


def isMinor(chord):
    if "m" in chord:
        return True
    return False


def isFlat(chord):
    if "b" in chord:
        return True
    return False


def isSharp(chord):
    if "#" in chord:
        return True
    return False


def getSharpMinor(chord):
    result = ''
    if isFlat(chord): result += "b"
    if isSharp(chord): result += "#"
    if isMinor(chord): result+= "m"
    return result
   

def getNashNums(chords):  #BROKEN, ADD EVERY KEY
    pass
    

def test_findKey():
    test_cases = [
        ("F C Gm Db", "F major"),
        ("Am Dm E7", "A minor"),
        ("C G Am F", "C major"),
        ("D A Bm G", "D major"),
        ("Em B7 Am C", "A minor"),
        ("C Dm G7 C", "C major"),
        ("Bb F Gm Eb", "Bb major"),
        ("G D Em C", "G major"),
        ("F#m D E A", "A major")
    ]
    
    for chords, expected_key in test_cases:
        # Assuming findKey function returns a key
        returned_key = findKey(chords)  # This is the function call you're testing
        print(f"Chords: {chords}")
        print(f"Returned Key: {returned_key}, Expected Key: {expected_key}\n")

# Call the test function
test_findKey()


    

    
    





