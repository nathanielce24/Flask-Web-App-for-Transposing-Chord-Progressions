import findkey
import transpose

nashvilleNumsMaj = ["I", "II", "III", "IV", "V", "VI", "VII*"]
nashvilleNumsMin = ["i", "ii", "iii", "iv", "v", "vi", "vii*"]

keys = findkey.keyLists

def stripChords(chords):
    newChords = []
    for chord in chords.split():
        newChords.append(chord[0] +findkey.getSharpMinor(chord))
    return newChords
        
def getIntervals(chords):
    intervals = []
    key = keys[findkey.findKey(chords)]
    strippedChords = stripChords(chords)
    for chord in strippedChords:
        if chord in key:
            intervals.append(str(key.index(chord)+1))
        elif any(chord[0] in key for chord in key):     #if the root is in the key
            matching_indices = [i+1 for i, j in enumerate(key) if chord[0] in j] #gets the index of the chord with the shared natural note
            if matching_indices:
                sharps_flats = findkey.getSharpsFlats(chord)
                intervals.append(f"{sharps_flats}{matching_indices[0]}")  
    return intervals

def toNashNums(chords):
    intervals = getIntervals(chords)
    

print(getIntervals("C Gb C# G"))


