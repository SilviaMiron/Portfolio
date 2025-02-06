from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# iCloud SMTP Configuration
SMTP_SERVER = "smtp.mail.me.com"
SMTP_PORT = 465
EMAIL_ADDRESS = "silvia.miron@icloud.com"  # Your iCloud email
EMAIL_PASSWORD = "grtqzordfbfmbjiz"  # App-Specific Password from Apple


@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:                                                                                                        
        return jsonify({"message": "All fields are required!"}), 400

    # Email content
    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # Send to yourself
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        #server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
       # server.starttls()  # Secure connection
       server = smtplib.SMTP_SSL(SMTP_SERVER, 465)  # Use SSL instead of TLS
       server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
       server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
       server.quit()
    finally:  jsonify({"message": "Email sent successfully!"})
        #except Exception as e:
        #return jsonify({"message": f"Failed to send email: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
