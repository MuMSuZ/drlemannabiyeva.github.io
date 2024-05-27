from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'd9753fc8300256e944992fd584ea0f0b0cc528521ff0732f4130cb4d609edea8'  # Gizli anahtarınızı buraya koyun

# Flask-Mail ayarları
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mumsuz@outlook.com'  # Kendi e-posta adresinizi buraya koyun
app.config['MAIL_PASSWORD'] = '83968758Leman'   # Kendi e-posta şifrenizi buraya koyun

mail = Mail(app)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_mail', methods=['POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message(subject=f"New Message from {name}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['mumsuz@outlook.com'],  # Hedef e-posta adresinizi buraya ekleyin
                      body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")
        
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)  # Waitress ile uygulamayı çalıştır
