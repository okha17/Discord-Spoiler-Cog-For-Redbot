from .spoiler import Spoilercog


def setup(bot):
    bot.add_cog(Spoilercog(bot))
