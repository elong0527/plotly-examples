# We need to import the jsonify object, it will let us
# output json, and it will take care of the right string
# data conversion, the headers for the response, etc
from flask import Flask, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)


# This route will return a list in JSON format
@app.route('/')
def index():
    # This is a dummy list, 2 nested arrays containing some
    # params and values
    test = [
        range(10),
        range(10)
    ]
    x1 = {
          "x" : [1, 2, 3, 4],
          "y" : [10, 10, 10, 10],
          "mode" : 'markers'
    }
    
    x2 = {
          "x" : [1, 2, 3, 4],
          "y" : [11, 10, 9, 8],
          "mode" : 'lines+markers'
    }
        
    x3 = {
          "x" : [1, 2, 3, 4],
          "y" : [10, 6, 10, 7],
          "mode" : 'markers'
    }
    # jsonify will do for us all the work, returning the
    # previous data structure in JSON
    return render_template('index.html', x1 = x1, x2 = x2, x3 = x3 )

if __name__ == '__main__':
    app.run(debug = True)