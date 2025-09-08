from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for complaints (use a database in production)
complaints = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        student_id = request.form.get('student_id')
        department = request.form.get('department')
        year = request.form.get('year')
        email = request.form.get('email')
        contact = request.form.get('contact')
        complaint_text = request.form.get('complaint')

        if name and student_id and department and year and email and contact and complaint_text:
            complaints.append({
                'name': name,
                'student_id': student_id,
                'department': department,
                'year': year,
                'email': email,
                'contact': contact,
                'complaint': complaint_text
            })
            return redirect(url_for('thank_you'))
        else:
            error = "Please fill in all fields."
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/complaints')
def view_complaints():
    return render_template('complaints.html', complaints=complaints)

@app.route('/thankyou')
def thank_you():
    return "<h2>Thank you for submitting your complaint.</h2><a href='/'>Submit another</a>"

if __name__ == '__main__':
    app.run(debug=True)
