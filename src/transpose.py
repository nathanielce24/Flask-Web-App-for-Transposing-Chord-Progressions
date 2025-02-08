def readChord(chord):    #Reads the important infomation to transpose chord
    root = ""
    extra = ""
    if not chord or chord[0] not in "ABCDEFG":
        print("Invalid Chord")
        return()
    if (len(chord)>1) and (chord[1] == "b" or chord[1] == "#"):
        root= chord[:2]
        extra = chord[2:]
    else:
        root = chord[0]
        extra = chord[1:]
    return(root, extra)


sharps = ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]
flats = ["G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb"]

def nextRoot(root, direction, interval):  #Finds next root noe
     notes = []

     if "b" in root: notes = flats
     else: notes = sharps
     if direction == "Down": notes.reverse()  
     
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


    
    





