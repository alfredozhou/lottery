from django.contrib import admin
from lotto_web.models import Person, Game, LotteryTicket, LotteryResult, LotteryNumber

admin.site.register(Person)
admin.site.register(Game)
admin.site.register(LotteryTicket)
admin.site.register(LotteryNumber)
admin.site.register(LotteryResult)
