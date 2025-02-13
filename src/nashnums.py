import findkey
import transpose

nashNumsMaj = ["OUK","I", "II", "III", "IV", "V", "VI", "VII*"]
nashNumsMin = ["OUK", "i", "ii", "iii", "iv", "v", "vi", "vii*"]

sharps = ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]
flats = ["G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb"]

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
        else:
            intervals.append('0')
        '''elif any(chord[0] in key for chord in key):     #if the root is in the key
            matching_indices = [i+1 for i, j in enumerate(key) if chord[0] in j] #gets the index of the chord with the shared natural note
            if matching_indices:
                sharps_flats = findkey.getSharpsFlats(chord)
                intervals.append(f"{sharps_flats}{matching_indices[0]}")  #Accounts for sharp/flat chords outside the key'''
    
    return intervals

def toNashNums(chords):
    intervals = getIntervals(chords)
    nashNums = ""
    for i, interval in enumerate(intervals):
        if findkey.isMinor(chords.split()[i]):
            nashNums += (nashNumsMin[int(interval[0])]) + " "
            print("jfdigf")
        else: 
            nashNums += (nashNumsMaj[int(interval[0])]) + " "
    return nashNums

def outOfKey(key, chord):   #Figures out the nashville numbering of an out of key chord
    key = keys[key]
    root = transpose.readChord(chord)[0]

#print(toNashNums("C G Am C"))
    
    
    

