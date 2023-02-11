#!/usr/bin/env python3

import subprocess
import re
import smtplib
from email.mime.text import MIMEText
import logging
import argparse

def check_for_rootkits():
    result = subprocess.run(['chkrootkit'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if re.search(r"INFECTED", output):
        logging.warning("Rootkit found!")
        logging.warning(output)
        return True, output
    else:
        logging.info("No rootkits found.")
        return False, output

def send_notification(output, recipient):
    msg = MIMEText(output)
    msg['Subject'] = 'Rootkit Detection'
    msg['From'] = 'rootkitdetector@example.com'
    msg['To'] = recipient
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rootkit Detection Script')
    parser.add_argument('-r', '--recipient', type=str, required=True, help='Email recipient address')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    rootkit_detected, output = check_for_rootkits()
    if rootkit_detected:
        send_notification(output, args.recipient)
