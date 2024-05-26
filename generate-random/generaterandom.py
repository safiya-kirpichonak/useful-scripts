#!/usr/bin/env python

import random
import string
import argparse


class Types:
    """
    Class containing all types of generated strings.
    """
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    MAC_ADDRESS = "mac"
    PASSWORD = "password"

def generate_password(length):
    """
    Generate a random password.
    """
    # validation, password length must be between 8 and 42 characters
    MIN_LENGTH = 8
    MAX_LENGTH = 42
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return "Password length must be between 8 and 42 characters."

    # generate password from random characters: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join([random.choice(characters) for _ in range(length)])


def generate_mac_address():
    """
    Generate a random MAC address. 

    MAC address contains 6 numbers (from 0 - 255) separated by colons in hexadecimal format.
    All mac addresses have 2 parts: OUI (Organizationally Unique Identifier) and NIC (Network Interface Controller).
    OUI is the company that created the device, and NIC is the id of the device itself.
    """
    mac = []
    for _ in range(6):
        random_number = random.randint(0x00, 0xFF)
        mac.append(f"{random_number:02x}")
    return ":".join(mac)


def generate_ipv4():
    """
    Generate a random IPv4 address.
    """
    return ".".join([str(random.randint(0, 255)) for _ in range(4)])


def generate_ipv6():
    """
    Generate a random IPv6 address.
    """
    mac = []
    for _ in range(8):
        random_number = random.randint(0x0000, 0xFFFF)
        mac.append(f"{random_number:04x}")
    return ":".join(mac)


if __name__ == "__main__":
    # initialize arguments parser
    parser = argparse.ArgumentParser(description="This script generates random variables.")
    parser.add_argument("-t", "--type", type=str, help="Type of generated string.")
    parser.add_argument("-l", "--length", type=int, help="Length of password. (required for password type)")
    args = parser.parse_args()

    # generate random string based on the type
    if args.type == Types.PASSWORD and args.length:
        print(generate_password(args.length))
    elif args.type == Types.MAC_ADDRESS:
        print(generate_mac_address())
    elif args.type == Types.IPV4:
        print(generate_ipv4())
    elif args.type == Types.IPV6:
        print(generate_ipv6())
    else:
        print("Invalid scheme.")
