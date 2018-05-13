import discord
import json
import os.path

client=discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('Coded by: TheRealCed')
	print('~~~~~~~~~~~~~~~~~~~~~~')

@client.event
async def on_message(message):
    user_id = message.author.id

    author_level = get_level(user_id)
    author_xp = get_xp(user_id)

    if author_level == 0 and author_xp >= 100:
        set_level(user_id, 1)
        await client.send_message(message.channel, "You Reached Level: 1")

    if author_level == 1 and author_xp >= 202:
        set_level(user_id, 2)
        await client.send_message(message.channel, "You Reached Level: 2")
    if author_level == 2 and author_xp >= 300:
        set_level(user_id, 3)
        await client.send_message(message.channel, "You Reached Level: 3")
    if author_level == 3 and author_xp >= 400:
        set_level(user_id, 4)
        await client.send_message(message.channel, "You Reached Level: ")
        lvl_role = None
        for role in message.server.roles:
            if role.name == "level 4":
                lvl_role = role

        await client.add_roles(message.author, lvl_role)

    if message.content.lower().startswith('c!xp'):
        await client.send_message(message.channel, "You have: `{}` XP!".format(get_xp(message.author.id)))

    if message.content.lower().startswith('c!lvl'):
        level = get_level(user_id)
        await client.send_message(message.channel, "Your level is: {}".format(level))

    user_add_xp(message.author.id, 2)


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0

    
    if message.content.lower().startswith('c!help'):
        await client.send_message(message.author, "test")       


client.run('Mzk1MjA0NjM0MzY2NDQzNTIw.DXXrEQ.bF7sU8sE_X870Qx2BDZ5t3EH67w')
