import os
import requests
from datetime import date,datetime
import pandas as pd
from send_email import send_email
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
env_path = current_dir / ".env"

load_dotenv(env_path)

# Read the environment variables
SheetURL = os.getenv("sheetURL")

# convert doc_sheet to csv
def convertsheet(sheetURL):
    #find docsheet or not
    if "docs.google.com/spreadsheets" in sheetURL:
        #if this excute means it is docsheet 
        #now convert xlsx file to csv
        if "/edit" in sheetURL:
            csv_format = sheetURL.split("/edit")[0] + "/export?format=csv"
        else:
            csv_format = sheetURL + "/export?format=csv"
        return csv_format
    else:
        raise ValueError("The provided URL does not seem to be a valid Google Sheets URL.")


# convert url into csv and assigned to csv_url variable
csv_url = convertsheet(SheetURL)


# convert drive link to export link resume
def drive_to_DLink(resume_path):
    if "drive.google.com/file" in resume_path:
        drive_id = resume_path.split("/file/d/")[1].split("/")[0]
        download_link = "https://drive.google.com/uc?export=download&id=" + drive_id
        download_file = download_link
        return download_file
    else:
        raise ValueError("The provided URL does not seem to be a valid Google Drive file URL.")


#download resume using drive link
def download_resume(download_link,save_path):
    response = requests.get(download_link,stream=True)
    if response.status_code == 200:
        with open(save_path,"wb") as file:
            file.write(response.content)
        print(f"Resume downloaded successfully and saved to {save_path}")
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

# local save path for the resume
save_path = "AdityaGavandi_Resume.pdf"


# load data from sheet using csv_url
def load_data(url):
    date = ['date']
    data = pd.read_csv(url,date_format=date)
    return data

def sheet_data(df):
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    present = date.today()
    email_counter = 0

    # extract row from file
    for index,row in df.iterrows():
        if (present >= row['date'].date()) and (row['applied'].lower() == 'no'):
            # Download the resume
            download_link = drive_to_DLink(row['resume_path'])
            download_resume(download_link, save_path)
            
            # send email
            send_email(
                subject=f"Application for {row['position']}",
                recipient_email=row['email'],
                platform = row['platform'],
                name=row['name'],
                position=row['position'],
                company=row['company'],
                resume_path=save_path,
            )

            # Update the applied status to yes
            df.at[index, 'applied'] = 'yes'
            email_counter += 1
            print(f"Email sent to {row['company']} regarding the {row['position']} position.")

            # delete downloaded resume
            os.remove(save_path)
            
    # Return a summary of the email activity
    print(f"Total emails sent: {email_counter}.")
    return df  # Return the updated DataFrame
    

df = load_data(csv_url)
result = sheet_data(df)
print(result)





