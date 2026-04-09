import smtplib 
from email.mime.text import MIMEText

def send_email(report, to_email):
    sender = "ahadshaikh2436@gmail.com"
    password = "srqs pnri qjwt yamt"   # NOT your real password

    msg = MIMEText(f"<pre>{report}</pre>", "html") 
    msg["Subject"] = "📊 Business Review Report" 
    msg["From"] = sender 
    msg["To"] = to_email 
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: 
        server.login(sender, password) 
        server.send_message(msg) 
        return True