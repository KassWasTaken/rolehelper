from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorCollection

class RoleHelper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    Assigns the given role to the user
    """
    @commands.command(name="addrole")
    @commands.has_role("Modmail")
    async def addrole(self, ctx, *, message):
        threadLog = await get_thread_log(self, ctx)
        user_id = threadLog['recipient']['id']

        await assign_role(self, ctx, user_id, message)

    """
    Removes the given role from the user
    """
    @commands.command(name="removerole")
    @commands.has_role("Modmail")
    async def removerole(self, ctx, *, message):
        threadLog = await get_thread_log(self, ctx)
        user_id = threadLog['recipient']['id']

        await remove_role(self, ctx, user_id, message)


async def get_thread_log(self, ctx):
    return await self.bot.api.db.logs.find_one({"channel_id": str(ctx.channel.id)})
        
async def assign_role(self, ctx, user_id, role_id):
    guild = ctx.guild.id
    member = await guild.fetch_member(user_id)
    role = guild.get_role(int(role_id))
    await member.add_roles(role)
    await ctx.send("Assigning " + str(role) + " to " + str(member))


async def remove_role(self, ctx, user_id, role_id):
    guild = ctx.guild.id
    member = await guild.fetch_member(user_id)
    role = guild.get_role(int(role_id))
    await member.remove_roles(role)
    await ctx.send("Removing " + str(role) + " from " + str(member))
   
def setup(bot):
    bot.add_cog(RoleHelper(bot))