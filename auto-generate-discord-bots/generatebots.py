import random
import requests
from colorama import init, Fore
import os
import time
import importlib.util

init()

def check_package(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"{Fore.YELLOW}INFO: {Fore.GREEN}Installing required packages")
        os.system(f"pip install -r requirements")

required_packages = ["requests", "colorama", "threading", "discord", "time"]
for package in required_packages:
    check_package(package)
    
print("------------------------------------------------")
print("------------------------------------------------")
print("███████╗██╗░░░██╗░██████╗░░██╗░░░░░░░██╗███████╗")
print("╚════██║██║░░░██║██╔═══██╗░██║░░██╗░░██║╚════██║")
print("░░███╔═╝██║░░░██║██║██╗██║░╚██╗████╗██╔╝░░███╔═╝")
print("██╔══╝░░██║░░░██║╚██████╔╝░░████╔═████║░██╔══╝░░")
print("███████╗╚██████╔╝░╚═██╔═╝░░░╚██╔╝░╚██╔╝░███████╗")
print("╚══════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══════╝")
print("------------------------------------------------")
print("------------------------------------------------")
time.sleep(1)
print(f"{Fore.BLUE}CREDITS: {Fore.RED}MADE BY ZUQWZ")
print('ANY QUESTIONS ADD ME IN DISCORD "valray" or "valray#5901" ')
time.sleep(1)
print(" ")
print(" ")
print(" ")
print(" ")

input("Press enter to start.")

num_threads = int(input("How many threads (applications) do you want to create? "))

name_option = input("Do you want to use names from 'names.txt'? (y/n): ")

if name_option.lower() == "y":
    with open("names.txt", "r") as file:
        names = file.readlines()
        names = [name.strip() for name in names if name.strip()]
else:
    names = []

token_option = input("Do you want to use Discord tokens from 'discordtokens.txt'? (y/n): ")

if token_option.lower() == "y":
    with open("discordtokens.txt", "r") as file:
        tokens = file.readlines()
        tokens = [token.strip() for token in tokens if token.strip()]
else:
    tokens = []

server_join_option = input("Do you want the bot to join a server? (y/n): ")

if server_join_option.lower() == "y":
    server_id = input("Enter the server ID to join: ")

print(f"{Fore.YELLOW}INFO: {Fore.GREEN}Creating discord application(s)")

app_url = "https://discord.com/api/v9/applications"

for _ in range(num_threads):
    if names and name_option.lower() == "y":
        name = random.choice(names)
        names.remove(name)  # Remove the chosen name from the list
    else:
        name = input("Enter a name for the application: ")

    if tokens:
        bot_token = random.choice(tokens)
        tokens.remove(bot_token)
    else:
        bot_token = input("enter your specific token to create applications:")
        

    headers = {
        "Authorization": bot_token
    }

    data = {
        "name": name
    }
    response = requests.post(app_url, headers=headers, json=data)
    if response.status_code >= 400:
        print(f"{Fore.RED}ERROR: {Fore.WHITE}Failed to create application! Status Code: {response.status_code} - {response.text}")
        input("Press enter to exit.")
        break
    bot_id = response.json()["id"]
    print(f"{Fore.YELLOW}INFO: {Fore.GREEN}Successfully created application {bot_id}")

    reset_token_url = f"https://discord.com/api/v9/applications/{bot_id}/bot/reset"
    reset_response = requests.post(reset_token_url, headers=headers)
    if reset_response.status_code >= 400:
        print(f"{Fore.RED}ERROR: {Fore.WHITE}Failed to reset token for application {bot_id}! Status Code: {reset_response.status_code} - {reset_response.text}")
        input("Press enter to exit.")
        break

    bot_token = reset_response.json()["token"]
    tokens.append(bot_token)

    # Save token to tokens.txt file
    with open("tokens.txt", "a", encoding="utf-8") as file:
        file.write("\n" + bot_token)  # Add a newline character before writing the token

    if server_join_option.lower() == "y":
        join_url = f"https://discord.com/api/v9/invite/{server_id}?scope=bot&permissions=0"
        join_response = requests.post(join_url, headers=headers)
        if join_response.status_code >= 400:
            print(f"{Fore.RED}ERROR: {Fore.WHITE}Failed to join server {server_id} with bot {bot_id}! Status Code: {join_response.status_code} - {join_response.text}")
            input("Press enter to exit.")
            break

if len(tokens) >= num_threads:
    print(f"{Fore.YELLOW}INFO: {Fore.GREEN}All tokens have been created and saved in tokens.txt")

    massdm_option = input("Do you want to open the mass DM script? (y/n): ")
    if massdm_option.lower() == "y":
        os.system("python massdm.py")
else:
    input("Press enter to exit.")
