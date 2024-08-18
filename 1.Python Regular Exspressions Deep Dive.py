# Task 1
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

print(f"Emails before the filtered email:{emails}")

exclude_email = 'exclude.com'
emails_filtered = [email for email in emails if not email.endswith(f'@{exclude_email}')]

print(f"Emails after filtering out the email: {emails_filtered}")
