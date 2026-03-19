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

    # Ask the user if they want to run in dry-run mode (Y = simulate, N = actually run)
    dry_run_input = input("Would you like to run the program in dry-run mode? (Y/N): ").strip().lower()
    # Convert the answer into a boolean (True = dry-run, False = normal run)
    dry_run = (dry_run_input == 'y')

    for line in sys.stdin:

        # Checks if the line starts with a '#', and if so we can ignore the line.
        match = re.match("^#", line)

        # Breaks the inputed line into parts using ':' as the delimiter.
        fields = line.strip().split(':')

        # Skip comment lines and anything that isn't in the right format.
        if match or len(fields) != 5:
            # In dry-run mode, show why the line is being skipped
            if dry_run:
                if match:
                    print("Skipping comment line.")
                else:
                    print("Error: invalid format ->", line.strip())
            # Skip processing this line
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

        # If dry-run is enabled, just print the command instead of running it
        if dry_run:
            print("[DRY-RUN]", cmd)
        else:
            # Runs the command to create the user.
            os.system(cmd)

        # Prints out that we're setting the password.
        print("==> Setting the password for %s..." % (username))

        # Builds the command that sets the user's password.
        cmd = "/bin/echo -e '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Again, only print the command in dry-run mode
        if dry_run:
            print("[DRY-RUN]", cmd)
        else:
            # Runs the command to set the password.
            os.system(cmd)

        for group in groups:
            # Only add the user if the group name isn't empty.
            if group != '':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Print instead of execute if dry-run is on
                if dry_run:
                    print("[DRY-RUN]", cmd)
                else:
                    os.system(cmd)

if __name__ == "__main__":
    main()
