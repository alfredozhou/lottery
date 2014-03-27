from django.contrib import admin
from lotto_web.models import User, Game, LotteryTicket, LotteryResult, LotteryNumber

admin.site.register(User)
admin.site.register(Game)
admin.site.register(LotteryTicket)
admin.site.register(LotteryNumber)
admin.site.register(LotteryResult)
