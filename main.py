from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import smtplib
from email.message import EmailMessage

app = FastAPI()

SENDER_EMAIL = "satkritikhadka2061@gmail.com"
APP_PASSWORD = "ciqj nrnn erac fgso"

class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    body: str

@app.post("/send-email")
def send_email(data: EmailRequest):
    msg = EmailMessage()
    msg['Subject'] = data.subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = data.recipient
    msg.set_content(data.body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        return {"message": "Email sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email. Error: {str(e)}")

