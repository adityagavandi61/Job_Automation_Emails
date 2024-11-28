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

def send_email(subject, recipient_email, name, position, company,resume_path,platform):
    # Base code for mail
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = formataddr(("Aditya Gavandi", sender_email))
    message["To"] = recipient_email
    message["BCC"] = sender_email

    # Email content
    message.set_content(
        f"""
        Dear {name},

        I am interested in applying for the {position} position at {company}. I have a solid base with Python programming, and by applying my experience in carrying out impactful projects in my previous roles, I seek to bring that into the team.

        During my career, I have started projects that demonstrate good technical skills with problem-solving abilities. These include:
        A full-stack social media web application built on the design and development basis of Python, Django and SQLite. This is considered a good runner-up in terms of designing a social networking site, so it is therefore strong and friendly to a user.
        Job Application Automation Tool: I designed an automation application using Python and libraries like pandas and requests that automates email communications about job applications. This project demonstrates my ability to overcome real-world challenges by innovative solutions.
        Portfolio Website: To showcase all the projects and skills, I developed a personal portfolio, ensuring seamless user experience through responsive design and efficient backend functionality.

        In addition to the technical capabilities, I would bring collaborative thinking and the ability to quickly change gears to address different challenges and I assure you that my skills are rather well-aligned with your overall objectives. I have attached my resume and the link to my portfolio below. I would be more than happy to discuss how my experience and skills may contribute to the success of {company}.

        I am writing to simply thank you for your time. I am excited to join your team and grow with {company}.
        Warm regards,
        Aditya Anand Gavandi
        +91 9637980861
        adityagavandi1998@gmail.com
        Porfolio : {portfolio_url}
        """,
        subtype="plain",
    )

    # HTML content
    message.add_alternative(
        f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 20px;">
        <p>Dear <strong>{name}</strong>,</p>

        <p>
            I am interested in applying for the <strong>{position}</strong> position at <strong>{company}</strong>. I have a solid base with Python programming, and by applying my experience in carrying out impactful projects in my previous roles, I seek to bring that into the team.
        </p>

        <p>
            During my career, I have started projects that demonstrate good technical skills with problem-solving abilities. These include:
        </p>

        <ul>
            <li>
                A full-stack social media web application built on the design and development basis of Python, Django, and SQLite. This project was a strong runner-up in a competition for designing a social networking site, highlighting its robustness and user-friendly features.
            </li>
            <li>
                <strong>Job Application Automation Tool:</strong> I designed an automation application using Python and libraries like <code>pandas</code> and <code>requests</code> that automates email communications about job applications. This project demonstrates my ability to overcome real-world challenges with innovative solutions.
            </li>
            <li>
                <strong>Portfolio Website:</strong> To showcase all the projects and skills, I developed a personal portfolio, ensuring seamless user experience through responsive design and efficient backend functionality.
            </li>
        </ul>

        <p>
            In addition to the technical capabilities, I would bring collaborative thinking and the ability to quickly change gears to address different challenges, and I assure you that my skills are well-aligned with your overall objectives. I have attached my resume and included the link to my portfolio here: 
            <a href="{portfolio_url}" target="_blank">Link</a>. I would be more than happy to discuss how my experience and skills may contribute to the success of <strong>{company}</strong>.
        </p>

        <p>
            I am writing to simply thank you for your time. I am excited to join your team and grow with <strong>{company}</strong>.
        </p>

        <p>
            Warm regards,<br>
            <strong>Aditya Anand Gavandi</strong>
        </p>
        <p>
        📧 <a href="mailto:adityagavandi1998@gmail.com">adityagavandi1998@gmail.com</a> | 📞 +91 9637980861<br>
        <a href={linkedIn_url} target="_blank">LinkedIn</a> |
        <a href={github_url} target="_blank">GitHub</a> |
        <a href="{portfolio_url}" target="_blank">Portfolio</a> |
        </p>
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

