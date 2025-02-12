import flask
from flask import Flask, request, render_template
import transpose

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chord_input = ""
    step_input = ""
    last_value = ""
    result = ""
    key = ""
    if request.method == "POST":
        chord_input = request.form["chord_input"]
        step_input = request.form["step_input"]
        direction_value = request.form.get('value')
        
        try:
            key = transpose.findKey(chord_input)
            result = transpose.transposeChords(chord_input, direction_value, int(step_input))# Call the main function'

        except:
            result = "Invalid Input"


    return render_template("index.html", 
                           result=result, 
                           chord_input=chord_input, 
                           step_input=step_input,
                           key = key)

if __name__ == "__main__":
    app.run(debug=True)