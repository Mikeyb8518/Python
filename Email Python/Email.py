import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails_from_csv(csv_file, email_template, my_email, my_password):
    # Set up the SMTP server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(my_email, my_password)

    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        #next(csv_reader)  # Skip the header row

        for row in csv_reader:
            recipient_name = row[0]
            recipient_email = row[1]
            message_body = email_template.replace("{NAME}", recipient_name)

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = recipient_email
            msg['Subject'] = "Personalized Email"

            # Attach the message body
            msg.attach(MIMEText(message_body, 'plain'))

            # Send the email
            server.send_message(msg)
            del msg  # Delete the message to free up memory

    # Terminate the SMTP session
    server.quit()

if __name__ == '__main__':
    MY_EMAIL = 'michaelboatwright8518@gmail.com'
    MY_PASSWORD = 'qckogaamttdttgds'
    CSV_FILE = 'contacts.csv'
    EMAIL_TEMPLATE = "Hello {NAME},\n\nThis is a personalized message for you!"

    send_emails_from_csv(CSV_FILE, EMAIL_TEMPLATE, MY_EMAIL, MY_PASSWORD)