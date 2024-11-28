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

        I am excited about the opportunity to apply for the {position} position currently open at {company}. Having a solid foundation with a proven history of successfully executing meaningful projects using Python programming, I look forward to bringing my capabilities and commitment to your team.

        Throughout my professional experience, I have taken assignments that show my technical ability and can solve problems. The high points include:
        Social Media Website: A fully functional social media website was designed and developed using Python, Django, and SQLite. This project won the second prize in a design competition for social networking sites, hence speaking to its robustness and user-friendly attributes.
        Job Application Automation Tool: I developed an application based on Python that uses libraries such as pandas and requests to automate email communication pertaining to job applications. This project shows my ability to address real-world problems through innovative solutions.
        Portfolio Website: Designed a personal portfolio that communicated all projects and skills while having responsive design and efficient functionality on the backend side.

        In addition to my technical expertise, I can bring a collaborative mindset and the ability to adapt quickly to new challenges and I feel that my skills are well in line with your goals. I have attached my resume and the link to my portfolio at ({portfolio_url}). It would be great if you would want to discuss my experience and expertise and how I might assist in making {company} a success.

        I appreciate your consideration of my application. I look forward to the opportunity to contribute to your team and develop professionally with {company}.
        Warm regards,
        Aditya Anand Gavandi
        +91 9637980861
        adityagavandi1998@gmail.com
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
            I am excited about the opportunity to apply for the <strong>{position}</strong> position currently open at <strong>{company}</strong>. Having a solid foundation with a proven history of successfully executing meaningful projects using Python programming, I look forward to bringing my capabilities and commitment to your team.
        </p>

        <p>
            Throughout my professional experience, I have taken assignments that show my technical ability and problem-solving skills. The high points include:
        </p>

        <ul>
            <li>
                <strong>Social Media Website:</strong> A fully functional social media website designed and developed using Python, Django, and SQLite. This project won second prize in a design competition for social networking sites, highlighting its robustness and user-friendly attributes.
            </li>
            <li>
                <strong>Job Application Automation Tool:</strong> A Python-based application utilizing libraries like <code>pandas</code> and <code>requests</code> to automate email communication for job applications. This project showcases my ability to address real-world problems through innovative solutions.
            </li>
            <li>
                <strong>Portfolio Website:</strong> A personal portfolio designed to showcase all projects and skills, featuring responsive design and efficient backend functionality.
            </li>
        </ul>

        <p>
            In addition to my technical expertise, I bring a collaborative mindset and the ability to adapt quickly to new challenges. I feel that my skills align well with your goals. I have attached my resume and included the link to my portfolio here:
            <a href="{portfolio_url}" target="_blank">Link</a>. I would be delighted to discuss my experience and expertise further and explore how I might assist in making <strong>{company}</strong> a success.
        </p>

        <p>
            I appreciate your consideration of my application. I look forward to the opportunity to contribute to your team and develop professionally with <strong>{company}</strong>.
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

