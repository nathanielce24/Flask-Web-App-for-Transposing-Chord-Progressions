#Chords in format [Root][Accidental][Quality][Inversions/Extensions]
def readChord(chord):
    root = ""
    extra = ""

    if chord[0] not in "ABCDEFG":
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

def nextRoot(root, direction, interval):
     notes = []

     if "b" in root: notes = flats
     else: notes = sharps
     if direction == "-": notes.reverse()  
     
     for _ in range(interval):
        root = notes[(notes.index(root)+1)%len(notes)]
     return root

def buildChord(chord, direction, interval):
    if not readChord(chord): print("Error")
    root, extra = readChord(chord)
    next = nextRoot(root, direction, interval)
    nextChord = next + extra
    print(nextChord)
    return nextChord

def transposeChords(chords, direction, interval):
    chords = chords.split()
    print(chords)
    transposed = []
    for chord in chords:
        transposed.append(buildChord(chord, direction, interval))
    return transposed

print(transposeChords("G C F# A BbAug C Ddim A", "+",1))
        

      


    
    





