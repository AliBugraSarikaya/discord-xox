import discord
from discord.ext import commands
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.command()
async def xox(ctx):
    def check(msg):
        return msg.author != client.user
    input_player_name_control = []
    move_control = []
    board = [["-" for i in range(3)] for j in range(3)]
    #Get name of user1
    await ctx.send("Enter your name first player !!!")
    input_player_1 = await client.wait_for("message", check=check, timeout=10000.0)
    input_player_name_control.append(input_player_1.content)
    #Get name of user2
    await ctx.send("Enter your name second player !!!")
    input_player_2 = await client.wait_for("message", check=check, timeout=10000.0)
    #Check if user1 got this name
    while input_player_2.content in input_player_name_control:
        await ctx.send("First player used this name you have to use another name !!!")
        input_player_2 = await client.wait_for("message", check=check, timeout=10000.0)
    #Board
    await ctx.send("*1 2 3")
    for i in range(3):
        await ctx.send(f"{i+1} {'|'.join(board[i])}")
    #Get 8 moves(4 moves for user1 and 4 moves for user2)
    for i in range(4):
        #Get move of user1
        await ctx.send("Let's play {} !!!".format(input_player_1.content))
        move_player_1 = await client.wait_for("message", check=check, timeout=10000.0)
        #Check if this move has been used
        while move_player_1.content in move_control:
            await ctx.send("This move has been played you have to play another move !!!")
            await ctx.send("Let's play {} !!!".format(input_player_1.content))
            move_player_1 = await client.wait_for("message", check=check, timeout=10000.0)
        move_control.append(move_player_1.content)
        #Splitting the user1's movement by index1 and index2. Then marking his/her movement on the board
        first_index_of_player_1 = int(move_player_1.content.split(",")[0]) - 1
        second_index_of_player_1 = int(move_player_1.content.split(",")[1]) - 1
        board[first_index_of_player_1][second_index_of_player_1] = "X"
        #Board
        await ctx.send("*1 2 3")
        for i in range(3):
            await ctx.send(f"{i+1} {'|'.join(board[i])}")
        #Check if user1 wins
        if (board[0][0] == board[0][1] == board[0][2] == "X") or (board[1][0] == board[1][1] == board[1][2] == "X") or (board[2][0] == board[2][1] == board[2][2] == "X") or (board[0][0] == board[1][0] == board[2][0] == "X") or (board[0][1] == board[1][1] == board[2][1] == "X") or (board[0][2] == board[1][2] == board[2][2] == "X") or (board[0][0] == board[1][1] == board[2][2] == "X") or (board[0][2] == board[1][1] == board[2][0] == "X"):
            await ctx.send("WINNER {} !!!".format(input_player_1.content))
            await ctx.send("GAME OVER !!!")
            xox_restart = await client.wait_for("message", check=check, timeout=10000.0)
            if xox_restart.content == "!xox":
                await xox(ctx)
            break
        #Get move of user2
        await ctx.send("Let's play {} !!!".format(input_player_2.content))
        move_player_2 = await client.wait_for("message", check=check, timeout=10000.0)
        #Check if this move has been used
        while move_player_2.content in move_control:
            await ctx.send("This move has been played you have to play another move !!!")
            await ctx.send("Let's play {} !!!".format(input_player_2.content))
            move_player_2 = await client.wait_for("message", check=check, timeout=10000.0)
        move_control.append(move_player_2.content)
        #Splitting the user2's movement by index1 and index2. Then marking his/her movement on the board
        first_index_of_player_2 = int(move_player_2.content.split(",")[0]) - 1
        second_index_of_player_2 = int(move_player_2.content.split(",")[1]) - 1
        board[first_index_of_player_2][second_index_of_player_2] = "O"
        #Board
        await ctx.send("*1 2 3")
        for i in range(3):
            await ctx.send(f"{i+1} {'|'.join(board[i])}")
        #Check if user2 wins 
        if (board[0][0] == board[0][1] == board[0][2] == "O") or (board[1][0] == board[1][1] == board[1][2] == "O") or (board[2][0] == board[2][1] == board[2][2] == "O") or (board[0][0] == board[1][0] == board[2][0] == "O") or (board[0][1] == board[1][1] == board[2][1] == "O") or (board[0][2] == board[1][2] == board[2][2] == "O") or (board[0][0] == board[1][1] == board[2][2] == "O") or (board[0][2] == board[1][1] == board[2][0] == "O"):
            await ctx.send("WINNER {} !!!".format(input_player_2.content))
            await ctx.send("GAME OVER !!!")
            xox_restart = await client.wait_for("message", check=check, timeout=10000.0)
            if xox_restart.content == "!xox":
                await xox(ctx)
            break
    #Get 1 move(1 move for user1)
    for i in range(1):
        #Get move of user1
        await ctx.send("Let's play {}!!!".format(input_player_1.content))
        move_player_1 = await client.wait_for("message", check=check, timeout=10000.0)
        #Check if this move has been used
        while move_player_1.content in move_control:
            await ctx.send("This move has been played you have to play another move !!!")
            await ctx.send("Let's play {} !!!".format(input_player_1.content))
            move_player_1 = await client.wait_for("message", check=check, timeout=10000.0)
        move_control.append(move_player_1.content)
        #Splitting the user1's movement by index1 and index2. Then marking his/her movement on the board
        first_index_of_player_1 = int(move_player_1.content.split(",")[0]) - 1
        second_index_of_player_1 = int(move_player_1.content.split(",")[1]) - 1
        board[first_index_of_player_1][second_index_of_player_1] = "X"
        #Board
        await ctx.send("*1 2 3")
        for i in range(3):
            await ctx.send(f"{i+1} {'|'.join(board[i])}")
        #Check if user1 wins
        if (board[0][0] == board[0][1] == board[0][2] == "X") or (board[1][0] == board[1][1] == board[1][2] == "X") or (board[2][0] == board[2][1] == board[2][2] == "X") or (board[0][0] == board[1][0] == board[2][0] == "X") or (board[0][1] == board[1][1] == board[2][1] == "X") or (board[0][2] == board[1][2] == board[2][2] == "X") or (board[0][0] == board[1][1] == board[2][2] == "X") or (board[0][2] == board[1][1] == board[2][0] == "X"):
            await ctx.send(" WINNER {} !!!".format(input_player_1.content))
            await ctx.send("GAME OVER !!!")
            xox_restart = await client.wait_for("message", check=check, timeout=10000.0)
            if xox_restart.content == "!xox":
                await xox(ctx)
            break
        #Check if user1 and user2 draw
        else:
            await ctx.send("DRAW {} and {} !!!".format(input_player_1.content,input_player_2.content))
            await ctx.send("GAME OVER !!!")
            xox_restart = await client.wait_for("message", check=check, timeout=10000.0)
            if xox_restart.content == "!xox":
                await xox(ctx)
            break
client.run("YOUR BOT TOKEN")


