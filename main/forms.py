##### Added on 10july2020

from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','tags',]


########################################################################################################################

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='', help_text='Required')
    first_name = forms.CharField(max_length=200,label='', required=True)
    last_name = forms.CharField(max_length=200,label='', required=True)
   
   
    class Meta:
    	model = User
    	fields = ('first_name','last_name','email', 'username', 'password1', 'password2')
    

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user_role','profile_pic')


class AstroProfileForm(forms.ModelForm):
	class Meta:
		model = Astro_Profile
		fields = ('skill','language','experience','location','about',)

class WalletForm(forms.ModelForm):
	class Meta:
		model = Wallet
		exclude = ('balance', 'user' )

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email', 'username')
		exclude = ()

########################################################################## Horoscopes Forms ######################

class DailyHoroscopeForm(forms.ModelForm):
	class Meta:
		model = DailyHoroscope
		fields = ('image','zodiac','date','category','content',)

class WeeklyHoroscopeForm(forms.ModelForm):
	class Meta:
		model = WeeklyHoroscope
		fields = ('image','zodiac','from_date','to_date','category','content',)

class MonthlyHoroscopeForm(forms.ModelForm):
	class Meta:
		model = MonthlyHoroscope
		fields = ('image','zodiac','month','year','category','content',)

class YearlyHoroscopeForm(forms.ModelForm):
	class Meta:
		model = YearlyHoroscope
		fields = ('image','zodiac','year','category','content',)


########################################################################## Panchang Forms ##########################

class DailyPanchangForm(forms.ModelForm):
	class Meta:
		model = DailyPanchang
		fields = ('date','tithi','nakshatra','karana','paksha','yoga','yoga_till','day')

class DailySolarCycleForm(forms.ModelForm):
	class Meta:
		model = DailySolarCycle
		fields = ('date','sunrise','sunset','moonsign','moonrise','moonset','ritu',)

class HinduMonthYearForm(forms.ModelForm):
	class Meta:
		model = HinduMonthYear
		fields = ('date','shakasamwat','vikramsamwat','monthamanta','monthpurnimanta')

class DailyTimingsForm(forms.ModelForm):
	class Meta:
		model = DailyTimings
		fields = ('date','rahu_from','rahu_to','yama_from','yama_to','gulika_from','gulika_to','abhi_from','abhi_to')

######################################################################## Kundli Forms ##############################

class KundliForm(forms.ModelForm):
	class Meta:
		model = Kundli
		fields = ('name','gender','birth_date','birth_time','birth_place',)


##################################################################### Numerology Forms ###########################

class DailyNumerologyForm(forms.ModelForm):
	class Meta:
		model = DailyNumerology
		fields = ('number','date','content',)	


class WeeklyNumerologyForm(forms.ModelForm):
	class Meta:
		model = WeeklyNumerology
		fields = ('number','from_date','to_date','content',)		

class MonthlyNumerologyForm(forms.ModelForm):
	class Meta:
		model = MonthlyNumerology
		fields = ('number','month','year','content',)	

class YearlyNumerologyForm(forms.ModelForm):
	class Meta:
		model = YearlyNumerology
		fields = ('number','year','content',)	

######################################################################## Tarot Forms ############################

class YearlyTarotForm(forms.ModelForm):
	class Meta:
		model = YearlyTarot
		fields = ('year','content') 

class TarotArticleForm(forms.ModelForm):
	class Meta:
		model = TarotArticle
		fields = ('title','pic','content') 

############################################################### Love Forms #####################################

class LoveForm(forms.ModelForm):
	class Meta:
		model = Love
		fields = ('name','birth_date','birth_time','gender','partner_name','partner_birth_date','partner_birth_time',)