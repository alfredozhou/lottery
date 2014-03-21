from django.contrib import admin
from lotto_web.models import Person, Game, LotteryTicket, LotteryResult

admin.site.register(Person)
admin.site.register(Game)
admin.site.register(LotteryTicket)
admin.site.register(LotteryResult)
