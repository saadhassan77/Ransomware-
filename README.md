# Ransomware
Fulfilling a requirement for my Fundamentals of Malware Analysis (CY3004) course, this project not only strengthens my grasp of malware behavior and the tactics it employs for persistence, but also sheds light on the inner workings of file encryption and decryption as utilized by malware.

# Description

Here's a description of the Python code you provided:

## Purpose:

This code creates a ransomware program that encrypts files on a victim's computer and demands a ransom payment for decryption.
## Key Functions:

### RansomWare class:
Manages encryption/decryption keys and file operations.
Encrypts files with a generated Fernet key.
Encrypts the Fernet key itself using an RSA public key for added security.
Decrypts files when a specific file ("PUT_ME_ON_DESKTOP.txt") is placed on the desktop (intended for the attacker to provide).
Maintains a list of encrypted files.
Changes desktop wallpaper to a ransom image.
Creates a ransom note file with instructions for payment.
Forces persistence by adding itself to Windows startup.
# main function:
Creates a RansomWare object.
Initiates encryption, key management, and persistence actions.
Launches threads to continuously display the ransom note and monitor for the decryption file.
### Overall Flow:

The program generates or loads encryption keys.
It encrypts files with specified extensions (e.g., "txt") and maintains a list of encrypted files.
It encrypts the Fernet key itself using RSA.
It changes the desktop wallpaper and creates a ransom note.
It adds itself to Windows startup for persistence.
It displays the ransom note and monitors for the decryption file.
If the decryption file is found, it decrypts the Fernet key and uses it to decrypt the files.
# Important Notes:

This code is for educational and research purposes only. Using it for malicious activities is illegal and unethical.
The code has several debugging/testing comments that should be removed for actual use.
It's crucial to handle potential errors and exceptions gracefully in a real-world scenario.
Consider using more sophisticated encryption and anti-analysis techniques for advanced ransomware.


# Working
https://github.com/saadhassan77/Ransomware-/assets/104758930/a32b4e6c-8997-49dc-b331-a7c14dfb77c3
https://github.com/saadhassan77/Ransomware-/assets/104758930/45ac2861-74cf-48cc-ba0f-aa08961be628


