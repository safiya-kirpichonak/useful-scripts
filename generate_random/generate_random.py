#!/usr/bin/env python

import argparse
import random
import string
import textwrap

hello_message = """
                                     __                                  __                 
.-----.-----.-----.-----.----.---.-.|  |_.-----.    .----.---.-.-----.--|  |.-----.--------.
|  _  |  -__|     |  -__|   _|  _  ||   _|  -__|    |   _|  _  |     |  _  ||  _  |        |
|___  |_____|__|__|_____|__| |___._||____|_____|    |__| |___._|__|__|_____||_____|__|__|__|
|_____|                                                                                     

This script generates random variables:
- Passwords (length 8 - 42)
- IPv4 and IPv6 addresses (local and global)
- MAC addresses
"""

print(hello_message)

description = "This script generates random variables."
parser = argparse.ArgumentParser(description=textwrap.dedent(description))

# initialize parser
parser.add_argument("-t", "--type", type=str, help="Type of generated string.")
parser.add_argument("-l", "--length", type=int, help="Length of password.")
args = parser.parse_args()

TYPE_IPV4 = "ipv4"
TYPE_IPV6 = "ipv6"
TYPE_MAC_ADDRESS = "mac"
TYPE_PASSWORD = "password"

def generate_password(length):
    """
    Generate a random password.
    """

    # validation
    MIN_LENGTH = 8
    MAX_LENGTH = 42
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return "Password length must be between 8 and 42 characters."

    # generate password
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(length))


if args.type == TYPE_PASSWORD and args.length:
    print(generate_password(args.length))
else:
    print("Invalid scheme.")
