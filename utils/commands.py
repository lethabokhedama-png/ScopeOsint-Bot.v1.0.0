import discord
from discord.ext import commands
from utils.osint import run_search

async def register(bot: commands.Bot):

    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong! 🏓")

    @bot.command()
    async def search(ctx, search_type, *, query):
        await ctx.send(f"🔎 Running `{search_type}` search for `{query}`...")

        try:
            result = run_search(query, search_type)

            if "error" in result:
                await ctx.send(f"⚠️ {result['error']}")
                return

            urls = []
            snippets = []

            items = result.get("results", [])

            for item in items:
                if item.get("link"):
                    urls.append(item["link"])
                if item.get("snippet"):
                    snippets.append(item["snippet"])

            url_preview = "\n".join(urls[:3]) if urls else "None found"
            snippet_preview = "\n".join(snippets[:3]) if snippets else "None found"

            embed = discord.Embed(
                title=f"Results for `{query}` ({search_type})",
                color=0x2ecc71 if result.get("found") else 0xe74c3c
            )

            embed.add_field(name="URLs", value=url_preview[:1024], inline=False)
            embed.add_field(name="Snippets", value=snippet_preview[:1024], inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ Error: {str(e)}")

    @bot.command()
    async def last(ctx, query):
        import json
        try:
            with open("data/results.json") as f:
                data = json.load(f)

            res = data.get(query)

            if not res:
                await ctx.send("No saved results found.")
                return

            await ctx.send(f"Last results for `{query}`: {res}")

        except Exception as e:
            await ctx.send(f"⚠️ Error reading saved results: {str(e)}")
