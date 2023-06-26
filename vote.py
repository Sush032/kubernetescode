from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize the vote counts
votes = {
    'option1': 0,
    'option2': 0,
    'option3': 0
}

@app.route('/')
def index():
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form['option']
    votes[selected_option] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
