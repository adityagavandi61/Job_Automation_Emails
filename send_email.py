import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
env_path = current_dir / ".env"
load_dotenv(env_path)

# Read the environment variables
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")

# social links
portfolio_url="https://adityagavandiportfolio.netlify.app/"
github_url="https://github.com/adityagavandi61"
linkedIn_url="https://linkedin.com/in/adityagavandi"

def send_email(subject, recipient_email, name, position, company,resume_path):
    # Base code for mail
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Aditya Gavandi", sender_email))
    message["To"] = recipient_email
    message["BCC"] = sender_email

    # Email content
    message.set_content(
        f"""
        Respected {name},
        
        I hope this email finds you well. I am writing to apply for the 
        {position} role at {company}, as advertised on LinkedIn.

        I am a skilled web developer with experience in Python and Django. I developed a 
        social media website that enables users to connect, share, and interact seamlessly. 
        This project demonstrates my proficiency in Python, Django, SQLite3, and front-end technologies like 
        HTML, CSS, and JavaScript. My work on this project earned me the runner-up prize in a social networking 
        site design competition.

        I attached my resume and portfolio attached for your review. I would welcome the opportunity 
        to discuss how I can contribute to your team.

        Thank you for considering my application. I look forward to hearing from you.

        Best regards,
        Aditya Anand Gavandi
        Python Django Developer
        """,
        subtype="plain",
    )

    # HTML content
    message.add_alternative(
        f"""
        <html>
        <body style="color: black; font-family: Arial, Helvetica, sans-serif; font-size: 14px;">
            <p>Respected {name},</p>
            <p>
                I hope this email finds you well. I am writing to apply for the 
                <strong style="font-weight: bold;">{position}</strong> role at <strong style="font-weight: bold;">{company}</strong>, as advertised on 
                <em style="font-style: italic;">LinkedIn</em>.
            </p>
            <p>
                I am a skilled web developer with experience in Python and Django. I developed a 
                <strong style="font-weight: bold;">social media website</strong> that enables users to connect, share, and interact seamlessly. 
                This project demonstrates my proficiency in Python, Django, SQLite3, and front-end technologies like 
                HTML, CSS, and JavaScript. My work on this project earned me the runner-up prize in a social networking 
                site design competition.
            </p>
            <p>
                I attached my resume and portfolio for your review. I would welcome the opportunity 
                to discuss how I can contribute to your team.
            </p>
            <p>Thank you for considering my application. I look forward to hearing from you.</p>
            <p>Best regards,</p>
            <div>
                <strong style="font-size: 16px;" >Aditya Anand Gavandi</strong><br>
                Python Django Developer<br>
                📧 <a href="mailto:adityagavandi1998@gmail.com">adityagavandi1998@gmail.com</a> | 📞 +91 9637980861<br>
                <a href={linkedIn_url} target="_blank">LinkedIn</a> | 
                <a href={github_url} target="_blank">GitHub</a> | 
                <a href="{portfolio_url}" target="_blank">Portfolio</a> | 
            </div>
        </body>
        </html>
        """,
        subtype="html",
    )

    # Attach the resume
    try:
        with open(resume_path, "rb") as file:
            resume = MIMEBase("application", "octet-stream")
            resume.set_payload(file.read())
            encoders.encode_base64(resume)
            resume.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(resume_path)}",
            )
            message.attach(resume)
    except FileNotFoundError:
        print(f"Error: The file {resume_path} was not found.")


    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(sender_email, sender_password)  # Log in
            server.send_message(message)  # Send the email
    except smtplib.SMTPAuthenticationError: # occurs when authentication failed
        print("Failed to login. Check your email and password.")
    except Exception as e:
        print(f"An error occurred: {e}")

