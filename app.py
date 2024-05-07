from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder for storing visit details
visits = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Import request from Flask
    from flask import request
    
    # Extract visit details from the form
    name = request.form['name']
    location = request.form['location']
    details = request.form['details']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    # Store visit details in the visits list
    visits.append({'name': name, 'location': location, 'details': details, 'latitude': latitude, 'longitude': longitude})
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/visits')
def view_visits():
    return render_template('visits.html', visits=enumerate(visits, start=1))

if __name__ == '__main__':
    app.run(debug=True)
