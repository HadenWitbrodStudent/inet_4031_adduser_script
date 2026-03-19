#!/usr/bin/python3

# INET4031
# Haden Witbrod
# Date Created 3/18/26
# Date Last Modified 3/18/26

# The imports allow us to run system commands, regex, and read inputs.
import os
import re
import sys

# The main function reads input and creates users from each valid line thats inputed.
def main():
    for line in sys.stdin:

        # Checks if the line starts with a '#', and if so we can ignore the line.
        match = re.match("^#", line)

        # Breaks the inputed line into parts using ':' as the delimiter.
        fields = line.strip().split(':')

        # Skip comment lines and anything that isn't in the right format.
        if match or len(fields) != 5:
            continue

        # Gathers the username, password, and name info from fields.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s" % (fields[3], fields[2])

        # Split the list into individual groups.
        groups = fields[4].split(',')

        # Prints out that we're creating the user.
        print("==> Creating account for %s..." % (username))

        # Builds the command that creates the users account.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Runs the command to create the user.
        os.system(cmd)

        # Prints out that we're setting the password.
        print("==> Setting the password for %s..." % (username))

        # Builds the command that sets the user's password.
        cmd = "/bin/echo -e '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Runs the command to set the password.
        os.system(cmd)

        for group in groups:
            # Only add the user if the group name isn't empty.
            if group != '':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == "__main__":
    main()
