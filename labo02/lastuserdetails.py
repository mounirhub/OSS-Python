#!/usr/bin/python3

with open('/etc/passwd', 'r') as passwd_file:
    last_line = passwd_file.readlines()[-1].strip()

    # split de lijn in velden op basis van de scheidingsteken ':'
    fields = last_line.split(':')

    # haal de gewenste velden op
    username = fields[0]
    uid = fields[2]
    home_dir = fields[5]

print(f"Gebruikersnaam: {username}")
print(f"UserID: {uid}")
print(f"Home directory: {home_dir}")