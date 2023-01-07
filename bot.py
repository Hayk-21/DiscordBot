import discord
import responses
import permission as perm
TOKEN = 'MTA1ODExNTU5MjI5ODY5NjgyNA.GSXgcS.-EtgPVEFK-Jb1YCWFOG7HBJ4cDWq6unBVfQY0M'


async def send_message(message, user_message, is_private, client):
    try:
        response = responses.get_response(message=user_message, data=message, client=client)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def role_indentification(roles):
    for rol in roles:
        if str(rol).lower() in perm.roles:
            return True
    return False

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel).lower()
        roles = message.author.roles
        text_channel = client.get_channel('1059434645483175956')
        print(f'{username} said: "{user_message}" ({channel})')

        if (channel in perm.channels) and role_indentification(roles):
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True, client=client)
            else:
                await send_message(message, user_message, is_private=False, client=client)

    client.run(TOKEN)