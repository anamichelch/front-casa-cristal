from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
@app.route('/#contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        print(name, email)

        # Process the form data (e.g., send email, save to database, etc.)
        #TODO send email to customer saying thank you for your message!
        #TODO send "personalized email from Luis asking more questions and inquiries
        #TODO save email and name to database

        return "Thank you for your message!"
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, port=5002)