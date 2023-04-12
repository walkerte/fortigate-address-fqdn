import csv

filename = "fqdns.csv"
group_name = "fqdn_group"
output_file = "fgt_commands.txt"

# Read the FQDNs from the CSV file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fqdns = [row[0] for row in csvreader]

# Generate FortiGate CLI commands for creating FQDN address objects
formatted_fqdns = ["edit \"" + fqdn + "\"\n" +
                   "\t" + "set type fqdn\n" +
                   "\t" + "set fqdn \"" + fqdn + "\"\n" +
                   "next\n" for fqdn in fqdns]

# Generate FortiGate CLI commands for creating a group and adding the FQDNs to it
group_commands = ["config firewall addrgrp\n" +
                  "edit \"" + group_name + "\"\n"] + \
                 ["\t" + "append member \"" + fqdn + "\"\n" for fqdn in fqdns] + \
                 ["next\n" +
                  "end\n"]

# Concatenate the CLI commands into a single string
cli_commands = "config firewall address\n" + "".join(formatted_fqdns) + "end\n" + \
               "".join(group_commands)

# Write the CLI commands to the output file
with open(output_file, 'w') as f:
    f.write(cli_commands)
