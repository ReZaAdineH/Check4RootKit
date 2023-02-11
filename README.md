# Check4RootKit
Rootkit Detection Tool

A Python script for detecting rootkits on a Linux system.

Features

Uses the chkrootkit command to check for rootkits
Sends an email notification to the specified recipient if a rootkit is detected
Uses logging to log important messages, making it easier to see important information and debug issues
Requirements

Python 3
A mail server installed and configured on the system (e.g. Postfix, Exim)
Usage

To run the script, use the following command:

java
 
python3 rootkit_detection.py -r recipient@example.com
Replace recipient@example.com with the email address of the recipient who should receive notifications if a rootkit is detected.

Future Improvements

Add the ability to schedule the script to run on a regular basis (e.g. daily, weekly) as part of a system maintenance routine.
Integrate with a centralized logging system to store rootkit detection results for future analysis.
