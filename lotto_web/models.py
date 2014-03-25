from django.db import models

class Person(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	telephone = models.CharField(max_length=25, null=True)
	email = models.CharField(max_length=50, null=True)
	password = models.CharField(max_length=50, null=True)
	
	def __unicode__(self):
		return self.name

class Game(models.Model):
	BRANDS = (
		('MM', 'Mega Millions'),
		('PB', 'Power Ball'),
	)

	brand = models.CharField(max_length=3, choices=BRANDS)
	description = models.CharField(max_length=40, blank=True)

	def __unicode__(self):
		return self.brand

class LotteryTicket(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	player = models.ForeignKey(Person)
	# image = models.ImageField(upload_to="images", blank=True, null=True)
	lottery_date = models.DateField(auto_now_add=False)
	name = models.CharField(max_length=100)
	bar_code =  models.CharField(max_length=100, null=True)
	game = models.ForeignKey(Game)

	def __unicode__(self):
		return self.name


class LotteryNumber(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	ticket = models.ForeignKey(LotteryTicket)
	number1 = models.IntegerField()
	number2 = models.IntegerField()
	number3 = models.IntegerField()
	number4 = models.IntegerField()
	number5 = models.IntegerField()
	ball = models.IntegerField()
	

class LotteryResult(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	prize = models.BigIntegerField()
	number1 = models.IntegerField(null=True )
	number2 = models.IntegerField(null=True )
	number3 = models.IntegerField(null=True )
	number4 = models.IntegerField(null=True )
	number5 = models.IntegerField(null=True )
	ball = models.IntegerField(null=True )
	game = models.ForeignKey(Game)
	lottery_date = models.DateField(auto_now_add=False)
