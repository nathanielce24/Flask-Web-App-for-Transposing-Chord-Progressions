import flask
from flask import Flask, request, render_template
import transpose
import findkey
import nashnums 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chord_input = ""
    step_input = ""
    last_value = ""
    result = ""
    key = ""
    new_key = ""
    if request.method == "POST":
        chord_input = request.form["chord_input"]
        step_input = request.form["step_input"]
        direction_value = request.form.get('value')
        
        try:
            key = findkey.findKey(chord_input)
            result = transpose.transposeChords(chord_input, direction_value, int(step_input))# Call the main function'
            new_key = transpose.nextKey(key, direction_value, int(step_input))

        except:
            result = "Invalid Input"


    return render_template("index.html", 
                           result=result, 
                           chord_input=chord_input, 
                           step_input=step_input,
                           key = key,
                           new_key = new_key)

if __name__ == "__main__":
    app.run(debug=True)