
from django.db import models
####### Added on 10jul2020
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.

############################################# BLOG WITH TAGS #######################################################

from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=250)
   
    description = models.TextField()
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()

    def __str__(self):
        return self.title


########################################################################################################################

######### Added on 10 july2020
class Profile(models.Model):
	ROLE =(('Customer','Customer'),('Astrologer','Astrologer'),)
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	profile_pic =  models.ImageField(default='def.jpg',upload_to="images",null=True, blank=True)
	user_role = models.CharField(max_length=30,choices=ROLE)

	def __str__(self):
		return self.user.username

class Astro_Profile(models.Model):
	LANGUAGES = (('English','English'),('Hindi','Hindi'),('Gujarati','Guarati'),('Marathi','Marathi'),('Tamil','Tamil'))
	SKILLS = (    
	    ('Vedic astrology','Vedic astrology'),
        ('Horoscopic astrology','Horoscopic astrology'),
        ('Vaastu','Vaastu'),
        ('Western astrology','Western astrology'),
        ('Numerology','Numerology'),
        ('Tarot divination','Tarot divination'),
        ('Prashna Kundali','Prashna Kundali'),
        ('KP astrology','KP astrology'),
    )
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
	skill = models.CharField(max_length=100,choices=SKILLS)
	language = MultiSelectField(choices=LANGUAGES,max_choices=5)
	experience = models.IntegerField()
	location = models.CharField(max_length=200)
	about = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.profile.user.username

class Wallet(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	balance = models.IntegerField(default=100)
	def __str__(self):
		return self.user.username



################################ HOROSCOPES MODELS ##############################################################

class DailyHoroscope(models.Model):
	ZODIACS = (('Aries','Aries'),('Taurus','Taurus'),('Gemini','Gemini'),('Cancer','Cancer'),
	           ('Leo','Leo'),('Virgo','Virgo'),('Libra','Libra'),('Scorpio','Scorpio'),
	            ('Sagittarius','Sagittarius'), ('Capricorn','Capricorn'),('Aquarius','Aquarius'),('Pisces','Pisces'))
	TYPES = (('Normal','Normal'),('Career','Career'),('Love','Love'),('Health','Health'))
	image = models.ImageField(default='zodiac2.jpg')
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)  
	zodiac = models.CharField(choices=ZODIACS, max_length=50) 
	date = models.DateField()
	category = models.CharField(choices=TYPES, max_length=50) 
	content = models.TextField()
	

	def __str__(self):
		return self.zodiac


class WeeklyHoroscope(models.Model):
	ZODIACS = (('Aries','Aries'),('Taurus','Taurus'),('Gemini','Gemini'),('Cancer','Cancer'),
	           ('Leo','Leo'),('Virgo','Virgo'),('Libra','Libra'),('Scorpio','Scorpio'),
	            ('Sagittarius','Sagittarius'), ('Capricorn','Capricorn'),('Aquarius','Aquarius'),('Pisces','Pisces'))
	TYPES = (('Normal','Normal'),('Career','Career'),('Love','Love'),('Health','Health'))
	image = models.ImageField(default='zodiac2.jpg')
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT) 
	zodiac =  models.CharField(choices=ZODIACS, max_length=50) 
	from_date = models.DateField()
	to_date = models.DateField()
	category = models.CharField(choices=TYPES, max_length=50) 
	content = models.TextField()

	def __str__(self):
		return self.zodiac


class MonthlyHoroscope(models.Model):
	ZODIACS = (('Aries','Aries'),('Taurus','Taurus'),('Gemini','Gemini'),('Cancer','Cancer'),
	           ('Leo','Leo'),('Virgo','Virgo'),('Libra','Libra'),('Scorpio','Scorpio'),
	            ('Sagittarius','Sagittarius'), ('Capricorn','Capricorn'),('Aquarius','Aquarius'),('Pisces','Pisces'))
	TYPES = (('Normal','Normal'),('Career','Career'),('Love','Love'),('Health','Health'))
	MONTHS = (('January','January'),('February','February'),('March','March'),('April','April'),
    	('May','May'),('June','June'),('July','July'),('August','August'),
    	('September','September'),('October','October'),('November','November'),('December','December'))
	YEARS = (('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'))
	image = models.ImageField(default='zodiac2.jpg')
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	zodiac = models.CharField(choices=ZODIACS, max_length=50) 
	month = models.CharField(choices=MONTHS, max_length=50)
	year = models.CharField(choices=YEARS, max_length=50)
	category = models.CharField(choices=TYPES, max_length=50)
	content = models.TextField()

	def __str__(self):
		return self.zodiac

class YearlyHoroscope(models.Model):
	ZODIACS = (('Aries','Aries'),('Taurus','Taurus'),('Gemini','Gemini'),('Cancer','Cancer'),
	           ('Leo','Leo'),('Virgo','Virgo'),('Libra','Libra'),('Scorpio','Scorpio'),
	            ('Sagittarius','Sagittarius'), ('Capricorn','Capricorn'),('Aquarius','Aquarius'),('Pisces','Pisces'))
	TYPES = (('Normal','Normal'),('Career','Career'),('Love','Love'),('Health','Health'))
	YEARS = (('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	image = models.ImageField(default='zodiac2.jpg')
	zodiac = models.CharField(choices=ZODIACS, max_length=50) 
	year = models.CharField(choices=YEARS, max_length=50)
	category = models.CharField(choices=TYPES, max_length=50)
	content = models.TextField()

	def __str__(self):
		return self.zodiac



########################################################### HOROSCOPE MODELS END ################################


############################ PANCHANG MODELS BEGIN ##############################################################

class DailyPanchang(models.Model):
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	date = models.DateField()
	tithi = models.CharField(max_length=50)
	nakshatra = models.CharField(max_length=50)
	karana = models.CharField(max_length=50)
	paksha = models.CharField(max_length=50)
	yoga = models.CharField(max_length=50)
	yoga_till = models.TimeField()
	day = models.CharField(max_length=50)


class DailySolarCycle(models.Model):
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	date = models.DateField()
	sunrise = models.TimeField()
	sunset = models.TimeField()
	moonsign = models.CharField(max_length=50)
	moonrise = models.TimeField()
	moonset = models.TimeField()
	ritu = models.CharField(max_length=50)

class HinduMonthYear(models.Model):
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	date = models.DateField()
	shakasamwat = models.IntegerField()
	vikramsamwat = models.IntegerField()
	monthamanta = models.CharField(max_length=50)
	monthpurnimanta = models.CharField(max_length=50)


class DailyTimings(models.Model):
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	date = models.DateField()
	rahu_from = models.TimeField()
	rahu_to = models.TimeField()
	yama_from = models.TimeField()
	yama_to = models.TimeField()
	gulika_from = models.TimeField()
	gulika_to = models.TimeField()
	abhi_from = models.TimeField()
	abhi_to = models.TimeField()
############################################################## PANCHANG MODELS END ##############################



################################ KUNDLI MODELS BEGIN #############################################################

class Kundli(models.Model):
	GENDERS = (('Male','Male'),('Female','Female'))
	name = models.CharField(max_length=100)
	gender = models.CharField(choices=GENDERS, max_length=20)
	birth_date = models.DateField()
	birth_time = models.TimeField()
	birth_place = models.CharField(max_length=50)

### ASSUMING SAME MODEL IS USED FOR THE KUNDLI MATCHMAKING METHOD TOO

######################################################## KUNDLI MODELS END ########################################


######################### NUMEROLOGY CREATION VIEWS ###############################################################


class DailyNumerology(models.Model):
	NUMBERS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	image = models.ImageField(default='zodiac2.jpg', blank=True)
	number = models.CharField(choices=NUMBERS, max_length=50) 
	date = models.DateField()
	content = models.TextField()


class WeeklyNumerology(models.Model):
	NUMBERS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	image = models.ImageField(default='zodiac2.jpg', blank=True)  
	number = models.CharField(choices=NUMBERS, max_length=50) 
	from_date = models.DateField()
	to_date = models.DateField()
	content = models.TextField()


class MonthlyNumerology(models.Model):
	MONTHS = (('January','January'),('February','February'),('March','March'),('April','April'),
    	('May','May'),('June','June'),('July','July'),('August','August'),
    	('September','September'),('October','October'),('November','November'),('December','December'))
	YEARS = (('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'))
	
	NUMBERS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)  
	image = models.ImageField(default='zodiac2.jpg', blank=True)  
	number = models.CharField(choices=NUMBERS, max_length=50) 
	month = models.CharField(choices=MONTHS, max_length=50)
	year = models.CharField(choices=YEARS, max_length=50)
	content = models.TextField()

class YearlyNumerology(models.Model):
	YEARS = (('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'))
	NUMBERS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'))

	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)
	image = models.ImageField(default='zodiac2.jpg', blank=True)    
	number = models.CharField(choices=NUMBERS, max_length=50) 
	year = models.CharField(choices=YEARS, max_length=50)
	content = models.TextField()

######################################################## NUMEROLOGY CREATION MODELS END ############################



########################## TAROT CREATION MODELS ###################################################################

class YearlyTarot(models.Model):
	YEARS = (('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'))
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.PROTECT)  
	
	year = models.CharField(choices=YEARS, max_length=50)
	content = models.TextField()

class TarotArticle(models.Model):
	astroprofile = models.ForeignKey(Astro_Profile, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	pic = models.ImageField(default="", upload_to="images",null=True, blank=True)
	content = models.TextField()
	date = models.DateField(auto_now_add=True)

class TarotQuestion(models.Model):
	post = models.ForeignKey(TarotArticle, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	question = models.TextField()


############################################################# TAROT CREATION MODELS END ############################


########################## LOVE CREATION MODELS ###################################################################

class Love(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.DateField()
	birth_time = models.TimeField()
	GENDERS = (('Male','Male'),('Female','Female'))
	gender = models.CharField(choices=GENDERS, max_length=20)
	partner_name = models.CharField(max_length=100)
	partner_birth_date = models.DateField()
	partner_birth_time = models.TimeField()
	






############################################################# LOVE CREATION MODELS END ############################


