from findkey import *

sharps = ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]
flats = ["G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb"]

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

def nextKey(key, direction, interval):
    root = readChord(key)[0]
    newRoot = nextRoot(root, direction, interval)
    if isMinor(key): 
        return newRoot + 'm'
    return newRoot


def buildChord(chord, direction, interval): #Finds next chord and adds extension back on
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


def mapToKey(roots):    #returns an array of nautural notes starting on the natural version of the first note in the progression (Maj and Min delt with later)
    ordered_notes = []
    start = naturals.index(roots[0][0])
    for i in range(start, 7+start):
        ordered_notes.append(naturals[i%(7)])
    return ordered_notes

    
    





