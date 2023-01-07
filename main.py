from colorama import Fore, Style, Back, init as coloramaInit
import pyperclip
import discum
import httpx
import json
import time
import re
import os

TOKEN_REGEX = '[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}'

coloramaInit()
print(Fore.RESET, Style.NORMAL)  # clean up terminal yk

clean_tokens = []

def help_display():
    print(f'{Fore.GREEN}- Help Menu -{Fore.RESET}\n')

    count = 0
    for cmd in commands:
        text = ""
        cmd_name = cmd.get('name')
        cmd_params = cmd.get('params')
        cmd_desc = cmd.get('desc')

        if cmd_params == []:
            text += f'{Fore.GREEN}{count}{Fore.RESET}.\n{Fore.LIGHTMAGENTA_EX}"{cmd_name}"\nDesc:\n{Fore.WHITE}{Style.BRIGHT}\t{cmd_desc}{Style.NORMAL}{Fore.RESET}'
        else:
            text += f'{Fore.GREEN}{count}{Fore.RESET}.\n{Fore.LIGHTMAGENTA_EX}"{cmd_name}"\nDesc:\n{Fore.WHITE}{Style.BRIGHT}\t{cmd_desc}{Style.NORMAL}\n{Fore.LIGHTMAGENTA_EX}Params:\n{Fore.RESET}'

        if cmd_params != []:
            for prm in cmd_params:
                # print(prm)
                prm_name = prm.get('name')
                prm_type = prm.get('type')
                prm_req = prm.get('required')
                text += f"{Fore.WHITE}{Style.BRIGHT}\t-{prm_name}, type: {prm_type}, required: {prm_req}\n{Fore.RESET}"

        text += Fore.RESET+Style.NORMAL+"\n\n"

        print(text)
        count += 1


with open('config.json', 'r') as f:
    config = json.loads(f.read())


def is_nan(num):
    return num != num


def get_guilds(token: str):
    guilds = httpx.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true',
                       headers={'Authorization': token}).json()

    print(f'{Fore.GREEN}{Style.BRIGHT}Pick your guild -> {Style.NORMAL}{Fore.RESET}')

    for i, guild in enumerate(guilds):
        print(f'{Fore.GREEN}{i}.{Fore.WHITE} {Style.BRIGHT}' +
              guild['name']+' ('+guild['id']+')'+f'{Style.NORMAL}{Fore.RESET}')

    while True:
        index = input("> ")
        try:
            int(index)
            if is_nan(float(index)) == True or index.strip() == '':
                print(
                    f'{Fore.RED}{Style.BRIGHT}Invalid input{Style.NORMAL}{Fore.RESET}')
            else:
                return guilds[int(index)]['id']
        except:
            print(f'{Fore.RED}{Style.BRIGHT}Invalid input{Style.NORMAL}{Fore.RESET}')


def token_input() -> str:
    string = ""
    count = 0
    print(f'{Fore.GREEN}{Style.BRIGHT}Pick your account -> {Style.NORMAL}{Fore.RESET}')
    for tok in clean_tokens:
        dict_username = tok.get('username')
        dict_id = tok.get('id')
        string += f'{Fore.GREEN}{count}{Fore.RESET} {Fore.MAGENTA}-{Fore.RESET} {Fore.WHITE}{Style.BRIGHT}{dict_username} ({dict_id}){Style.NORMAL}{Fore.RESET}\n'
        count += 1
    print(string)

    while True:
        index = input("> ")
        try:
            int(index)
            if is_nan(float(index)) == True or index.strip() == '':
                print(
                    f'{Fore.RED}{Style.BRIGHT}Invalid input{Style.NORMAL}{Fore.RESET}')
            else:
                clean_token = clean_tokens[int(index)].get('token')
                return clean_token
        except:
            print(f'{Fore.RED}{Style.BRIGHT}Invalid input{Style.NORMAL}{Fore.RESET}')


def load_tokens(): 
    if config.get('tokens') == []:
        print(f'{Fore.YELLOW}{Style.BRIGHT}No tokens stored.{Style.NORMAL}{Fore.RESET}')
        return

    token_len = len(config.get('tokens'))
    current_token = 0
    print(f'{Fore.GREEN}Tokens stored: {token_len}.{Fore.RESET}')

    for token in config.get('tokens'):
        current_token += 1
        if re.compile(TOKEN_REGEX).search(token) == None:
            print(
                f'{Fore.YELLOW}{Style.BRIGHT}Invalid token "{token}", skipping.{Style.NORMAL}{Fore.RESET}')
            continue

        try:
            user = httpx.get('https://discord.com/api/v8/users/@me',
                             headers={'Authorization': token}).json()
            username = user.get('username') + '#' + user.get('discriminator')
            user_id = user.get('id')
            print(
                f'{Fore.GREEN}Loaded user "{username}" ({user_id}). {current_token}/{token_len}{Fore.RESET}')
            clean_tokens.append({
                "username": username,
                "token": token,
                "id": user_id
            })
            time.sleep(0.75)
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}Failed to load token "{token}".{Style.NORMAL}{Fore.RESET}')


def scrape_members(channel_id: str, hide: bool):
    token = token_input()
    guild = get_guilds(token)

    bot = discum.Client(token=token, log=False)
    user = httpx.get('https://discord.com/api/v8/users/@me',
                     headers={'Authorization': token}).json()
    nitro = user.get('premium_type') != 0

    def generate_message(m1, m2):
        # return m1 + ('||\u200b||' * 196) + m2 # kinda broken ig
        return m1 + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||" + m2

    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            lenmembersfetched = len(
                bot.gateway.session.guild(guild_id).members)
            print(str(lenmembersfetched) +
                  f'{Fore.MAGENTA} members fetched...{Fore.RESET}')
            bot.gateway.removeCommand(
                {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
        bot.gateway.command({'function': close_after_fetching,
                            'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members

    message = ''
    message_count = 0
    members = get_members(guild, channel_id)
    for id in members:
        if hide == True:
            if nitro == True:
                if (message_count + 980) >= 4000:
                    break
            else:
                if (message_count + 980) >= 2000:
                    break
        else:
            if nitro == True:
                if (message_count) >= 4000:
                    break
            else:
                if (message_count) >= 2000:
                    break
        message += f'<@{id}>'
        message_count += 22
    if hide == True:
        hidden = generate_message("@everyone", message)
    else:
        hidden = message
    pyperclip.copy(hidden)
    print(f"{Fore.GREEN}{Style.BRIGHT}Copied to clipboard!{Style.RESET_ALL}{Fore.RESET}")


commands = [
    {
        "name": "scrapeall",
        "desc": "Scrapes all possible members in a server and compiles it into a mass ping.",
        "callback": None,
        "params": [
            {
                "name": "channel",
                "type": 'int',
                "required": True
            },
            {
                "name": "hide",
                "type": 'bool',
                "required": False,
                "default": "true"
            }
        ]
    },
    {
        "name": "help",
        "desc": "Displays the help menu",
        "callback": help_display,
        "params": []
    },
    {
        "name": "addtoken",
        "desc": "Adds token to store.",
        "callback": None,
        "params": []
    },
    {
        "name": "removetoken",
        "desc": "Removes token from store.",
        "callback": None,
        "params": []
    },
    {
        "name": "spamgif",
        "desc": "Spams a list of gifs.",
        "callback": None,
        "params": [
            {
                "name": "file",
                "type": 'str',
                "required": True,
            },
            {
                "name": "channel",
                "type": 'str',
                "required": True,
            }
        ]
    },
]


def parse_cmd(cmd: str):
    split = cmd.split(' ')

    is_valid = False
    for i in commands:
        if split[0] == i['name']:
            if i['params'] == [] and i['callback'] != None:
                i['callback']()
            is_valid = True
            break

    if is_valid != True:
        print(
            f'{Fore.RED}{Style.BRIGHT}Invalid command "{split[0]}"{Style.NORMAL}{Fore.RESET}')
        return

    full = {}

    for command in commands:
        for param in command['params']:
            for index, i in enumerate(split):
                if i.startswith('-'+param['name']):
                    value = split[index+1]

                    full[param['name']] = value
    if split[0] == 'spamgif':
        try:
            split[1].strip()
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}No filename input.{Style.NORMAL}{Fore.RESET}')
            return

        channel = full.get('channel')
        file = full.get('file')

        if channel == None:
            print(
                f'{Fore.RED}{Style.BRIGHT}Missing parameter "channel"{Style.NORMAL}{Fore.RESET}')
            return
        if file == None:
            print(
                f'{Fore.RED}{Style.BRIGHT}Missing parameter "file"{Style.NORMAL}{Fore.RESET}')
            return

        try:
            int(channel)
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}Invalid type in parameter "channel", check help.{Style.NORMAL}{Fore.RESET}')
            return

        if os.path.exists(file) == False:
            print(
                f'{Fore.RED}{Style.BRIGHT}File not found.{Style.NORMAL}{Fore.RESET}')
            return

        token = token_input()
        bot = discum.Client(token=token, log=False)

        with open(file, 'r') as f:
            try:
                lines = f.readlines()
                while True:
                    for i in lines:
                        bot.sendMessage(channel, i.strip())
                        time.sleep(0.35)
            except KeyboardInterrupt:
                print(f'{Fore.GREEN}Stopped.{Fore.RESET}')

    elif split[0] == 'addtoken':
        try:
            split[1].strip()
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}No token input.{Style.NORMAL}{Fore.RESET}')
            return

        dirty_token = split[1].strip()

        if dirty_token in config['tokens']:
            print(
                f'{Fore.YELLOW}{Style.BRIGHT}Token has already been stored.{Style.NORMAL}{Fore.RESET}')
            return

        if re.compile(TOKEN_REGEX).search(dirty_token) == None:
            print(
                f'{Fore.RED}{Style.BRIGHT}Invalid token "{dirty_token}"{Style.NORMAL}{Fore.RESET}')
            return

        config['tokens'].append(split[1].strip())

        with open('config.json', 'w') as f:
            f.write(json.dumps(config))
            print(f'{Fore.GREEN}Saved token.{Fore.RESET}\n')
            f.close()

        load_tokens()

    elif split[0] == 'removetoken':
        try:
            split[1].strip()
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}No token input.{Style.NORMAL}{Fore.RESET}')
            return

        if split[1].strip() not in config['tokens']:
            print(
                f'{Fore.YELLOW}{Style.BRIGHT}Token doesn\'t exist.{Style.NORMAL}{Fore.RESET}')
            return

        config['tokens'].remove(split[1].strip())

        with open('config.json', 'w') as f:
            f.write(json.dumps(config))
            print(f'{Fore.GREEN}Saved.{Fore.RESET}\n')
            f.close()
    elif split[0] == 'scrapeall':
        channel = full.get('channel')
        hide = full.get('hide')  # not required

        if hide == None:
            hide = True
        else:
            hide = [hide.lower() in ['true', '1', 't', 'y', 'yes']][0]

        if channel == None:
            print(
                f'{Fore.RED}{Style.BRIGHT}Missing parameter "channel"{Style.NORMAL}{Fore.RESET}')
            return
        try:
            int(channel)
        except:
            print(
                f'{Fore.RED}{Style.BRIGHT}Invalid type in parameter "channel", check help.{Style.NORMAL}{Fore.RESET}')
            return

        scrape_members(channel, hide)


load_tokens()

print(f'{Fore.MAGENTA}{Style.DIM}Welcome.{Style.NORMAL}{Fore.RESET}')

try:
    while True:
        cmd = input("> ")
        parse_cmd(cmd)
except KeyboardInterrupt:
    print(f'{Fore.MAGENTA}{Style.DIM}Goodbye.{Style.NORMAL}{Fore.RESET}')
    exit()

