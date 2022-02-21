# Bradley Stenseth
# CIS245-T303
# Assignment 10
# Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
# Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
# The program should then prompt the user for their name, address, and phone number.
# Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.

import os

# Prompts the directory location from the user
def prompt_directory():
    '''Prompts for the directory location'''
    directory_location = input('What is the directory location to save the file to? ')

    return directory_location

# Prompts the filename from the user
def prompt_filename():
    '''Prompts for the filename'''
    filename = input('What is the filename? ')

    return filename

# Prompts for the user information and puts in comma separated
def prompt_userinfo():
    '''Prompts for the user information'''
    print('Please enter the following.')
    full_name = input('Full Name: ')
    address = input('Address: ')
    phone_number = input('Phone Number: ')

    user_info = f'{full_name}, {address}, {phone_number}'

    return user_info

# Check if directory exists, if not then create it
def check_directory(directory):
    '''Checks if directory exists, if it doesn't then create it'''
    directory_exists = os.path.exists(directory)

    if not directory_exists:
        os.makedirs(directory)
        print('')
        print(f'Directory created: {directory}')

# Write userinfo to file
def write_file (directory, filename, user_info):
    '''Main function, writes user info the file and saves into directory'''
    path_name = os.path.join(directory, filename)

    user_file = open(path_name, 'w')
    user_file.write(user_info)
    user_file.close()

# Reads file contents
def read_file (directory, filename):
    '''Secondary function, reads the file contents'''
    path_name = os.path.join(directory, filename)

    user_file = open(path_name, 'r')
    file_contents = user_file.read()
    print('')
    print('Here are the contents of your new file:')
    print(file_contents)
    user_file.close()

# Main
def main():
    '''Main'''
    user_directory = prompt_directory()
    user_filename = prompt_filename()
    user_information = prompt_userinfo()
    check_directory(user_directory)
    write_file(user_directory, user_filename, user_information)
    read_file(user_directory, user_filename)

main()