# Job Automation Emails Project

---

## **Overview**
The Job Automation Emails Project automates job application processes by reading job details from a structured spreadsheet and sending personalized emails to recruiters. It ensures a streamlined and efficient workflow for job seekers by leveraging Python libraries such as `pandas`, `requests`, and `email`.

---

## **Features**
- Convert an `.xlsx` file to a .csv file format and then read the `.csv` file.
- Filters jobs based on:
  - Application status (`applied: no`)
  - Application due date.
- Sends automated, personalized job application emails with:
  - Customized subject lines and email bodies.
  - Resumes attached using file download links.
- Tracks and reports the total number of emails sent.

---

## **Prerequisites**
### 1. **Software Requirements**
- Python 3.7 or later
- Email server access (e.g., Gmail SMTP with App Passwords).

### 2. **Python Libraries**
Install the required libraries using pip:
```bash
pip install pandas requests
```

## **Spreadsheet Format**
The input spreadsheet should have the following columns:
- `name`: Recipient name.
- `email`: Recipient's email address.
- `position`: Job title or position you’re applying for.
- `company`: Name of the company.
- `date`: Application date (`dd/mm/yyyy` format).
- `applied`: Application status (`yes` or `no`).
- `resume_url`: Downloadable link to the resume.

---
## **Screenshots**
- Add data in Google spreadsheet file
![Google Spreadsheet data](https://github.com/user-attachments/assets/411b04c8-9549-494e-93fc-7be2438f85b2)

- Successfully deployed the project on a reliable hosting platform, scheduled to run every day at 10:30 AM for seamless accessibility and performance
  ![Screenshot 2024-11-19 174356](https://github.com/user-attachments/assets/72af88e0-25f2-4719-bf1d-384fef007be0)
  

## **Usage**

### 1. **Set up the Project**
- Clone the repository:
  ```bash
  git clone https://github.com/adityagavandi/job-automation-emails.git
  cd job-automation-emails 
  ```
### **2. Add dotenv File**
- Add your email address to the `.env` file.
- Use the app password generated by Google Authenticator instead of your regular password.
- Add the Google spreadsheet link.
```bash![Screenshot 2024-11-19 130436](https://github.com/user-attachments/assets/e132e5a3-95cf-41ad-aeff-b37eb9cda5d4)

pip install dotenv
```
```bash
EMAIL=example@gmail.com
PASSWORD=your_app_password
SHEET_URL=your_spreadsheet_google_link

```

### 3. **Run the Script**
Execute the main script to start sending emails:
```bash
python main.py
```

### 4. **Key Workflow**
- Reads the spreadsheet using `pandas`.
- Downloads resume using the `requests` library.
- Sends emails using the `email` library.
- Updates the application status in the spreadsheet.

---

## **Customization**
- Modify the email body or subject in the `send_email()` function to match your requirements.
- Adjust the spreadsheet structure by editing the column mapping in the code.

---

## **Future Enhancements**
- Support for additional file types and email servers should be added.
- Implement error handling for failed downloads or email sends.
- Enhance the reporting system to better track sent applications.

---

## **Credits**
**Aditya Gavandi developed this project** as a practical implementation of Python automation to solve real-world job application challenges.

- **GitHub Repository**: [https://github.com/adityagavandi](https://github.com/adityagavandi)  
- **LinkedIn**: [Aditya Gavandi](https://www.linkedin.com/in/adityagavandi)
