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


   
