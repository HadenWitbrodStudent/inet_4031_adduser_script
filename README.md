# inet_4031_adduser_script

Program Description

This script reads user data from a file and automatically creates user accounts, sets passwords, and assigns groups.

Program User Operation

Run the script and redirect an input file into it:

./create-users.py < create-users.input

Input File Format

Each line must follow this format:

username:password:last:first:group1,group2

Lines starting with # are treated as comments and skipped.

Command Execution

The script builds system commands like adduser and passwd and runs them using os.system().

"Dry Run"

For testing, you can print the commands instead of running them to verify correctness before making changes.
