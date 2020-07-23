####### Added on 10 july 2020
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import stripe
from django.shortcuts import render
from .filters import AstroFilter
from .decorators import restrict_customer
from datetime import date, timedelta

#### STRIPE KEY ########
stripe.api_key = ('sk_test_51GzwicFlMZrJNY0xzkbFfyuVlnGK2Fuu77qFgpsCdMjTuDT8aCTeh9bIUxmXMZmFCRSx0WLtnGQb7598hFFXcldp00xF0KKieG')


###########################################################################################################3

from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm

from taggit.models import Tag
from django.template.defaultfilters import slugify


def homeview(request):
    posts = Post.objects.all()
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'blogs/home.html', context)

def detailview(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'blogs/detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'common_tags':common_tags,
        'posts':posts,
    }
    return render(request, 'blogs/viewblog.html', context)





##########################################################################################################







# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def logout(request):
    return render(request,'logout.html')


######## Added on 10 july

##################### PROFILE VIEWS for every user #######################################################################

###### Signup and activation ############################################################################################

def Convert(string):
	li = list(string.split(" "))
	return li

def signup(request):
    if request.method == 'POST':
        form1 = SignupForm(request.POST)
       

        if form1.is_valid():

            user = form1.save(commit=True)
            user.is_active = False
            user.save()

            

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })

            to_email = Convert(form1.cleaned_data.get('email'))
            print(to_email)
            send_mail('test', message ,'najay357@gmail.com', to_email, fail_silently=False)
            
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form1 = SignupForm()
       
    return render(request, 'signup.html', {'form1': form1})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        
        pro = user
        user.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")


        return HttpResponse('We have confirmed account,  go to home')


        
    else:
        return HttpResponse('Activation link is invalid!')

################################################ Signup and activation end ###############################################

@login_required(login_url='index')
def dashboard(request):
    return render(request,'dashboard.html')

############################### PROFILE EDIT VIEWS for every user ######################################################

@login_required(login_url='index')
def completeprofile(request):
    if request.method == "POST":
        form1 = ProfileForm(request.POST)
        form2 = WalletForm(request.POST) 
        if form1.is_valid() and form2.is_valid():
            profile = form1.save(commit=False)
            profile.user = request.user
            profile.save()

            wallet = form2.save(commit=False)
            wallet.balance = 100
            wallet.user = request.user
            wallet.save()
            return redirect(reverse('dashboard'))

    else:
        form1 = ProfileForm()
        form2 = WalletForm()

    return render(request, 'completeprofile.html', {'form1':form1, 'form2':form2})

@login_required(login_url='index')
def updateprofile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))

    else:
        form = EditProfileForm(instance=request.user)
        context = { 'form': form }

        return render(request, 'editprofile.html', context)

@login_required(login_url='index')
def updateprofilepic(request):
    prof = request.user.profile
    form = ProfileForm(instance=prof)

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=prof)
        if form.is_valid():
            
            form.save()
            return redirect(reverse('dashboard'))

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'editprofilepic.html', {'form':form})

############################################## PROFILE EDIT VIEWS for every user end ######################################    

################################### PROFILE VIEWS for every user end #######################################################

########################## VIEWS FOR ONLY ASTROPROFILE ##################################################################

@login_required(login_url='index')
@restrict_customer
def createastroprofile(request):
    prof = request.user.profile
    if request.method == "POST":
        form = AstroProfileForm(request.POST)
         
        if form.is_valid():
            astro_profile = form.save(commit=False)
            astro_profile.profile = prof
            astro_profile.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = AstroProfileForm()
        

    return render(request, 'astroprofile.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def updateastroprofile(request):
    if request.method == "POST":
        form = AstroProfileForm(request.POST,instance=request.user.profile.astro_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))

    else:
        form = AstroProfileForm(instance=request.user.profile.astro_profile)
        context = { 'form': form }

        return render(request, 'editastroprofile.html', context)

############################## ASTROPROFILE VIEWS END #####################################################################

################################################ PROFILE VIEWS END #####################################################


###############################################3 WALLET RECHARGE VIEWS #################################################

@login_required(login_url='index')
def recharge(request):
    return render(request,'recharge.html')

@login_required(login_url='index')
def charge(request):
    if request.method == "POST":
        amount = int(request.POST['amount'])

        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.user.email,
            name=request.user.username,
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='INR',
            description="Donation"
            )

        Wallet.objects.filter(balance=request.user.wallet.balance).update(balance=F('balance')+ amount)

        return redirect('dashboard')
    return redirect('recharge')

################################################ WALLET RECHARGE VIEWS end ##################################################



def astrosearch(request):
    astrologer = Astro_Profile.objects.all()
    
    astro_count = astrologer.count()

    myFilter = AstroFilter(request.GET, queryset=astrologer)
    astrologer = myFilter.qs


    paginated_orders = Paginator(astrologer, 5)
    page_number = request.GET.get('page')
    order_page_obj = paginated_orders.get_page(page_number)

    context = { 'order_page_obj':order_page_obj, astrologer : astrologer, 'astro_count':astro_count, 'myFilter':myFilter}
    return render(request, 'search.html', context)


def astrodetail(request, id):
    detail = Astro_Profile.objects.get(pk=id)
    #reviews = Review.objects.filter(astroprofile=detail).order_by('-id')
    


    context = {'detail':detail}


    return render(request, 'singleastro.html', context)


########################################### HOROSCOPE CREATION VIEWS BEGIN ###########################################

@login_required(login_url='index')
@restrict_customer
def createdailyhoroscope(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyHoroscopeForm(request.POST)
         
        if form.is_valid():
            daily_horoscope = form.save(commit=False)
            daily_horoscope.astroprofile = astro_prof
            daily_horoscope.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = DailyHoroscopeForm()
        

    return render(request, 'horoscopes/createdailyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editdailyhoroscope(request, id):
    daily_horoscope = DailyHoroscope.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyHoroscopeForm(request.POST, instance=daily_horoscope)

        if form.is_valid():
            daily_horoscope = form.save(commit=False)
            daily_horoscope.astroprofile = astro_prof
            daily_horoscope.save()

            return redirect(reverse('dashboard'))

    else:
        form = DailyHoroscopeForm(instance=daily_horoscope)
        

    return render(request, 'horoscopes/createdailyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletedailyhoroscope(request, id):
    DailyHoroscope.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))

@login_required(login_url='index')
@restrict_customer
def createweeklyhoroscope(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = WeeklyHoroscopeForm(request.POST)
         
        if form.is_valid():
            weekly_horoscope = form.save(commit=False)
            weekly_horoscope.astroprofile = astro_prof
            weekly_horoscope.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = WeeklyHoroscopeForm()
        

    return render(request, 'horoscopes/createweeklyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editweeklyhoroscope(request, id):
    weekly_horoscope = WeeklyHoroscope.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = WeeklyHoroscopeForm(request.POST, instance=weekly_horoscope)

        if form.is_valid():
            daily_horoscope = form.save(commit=False)
            daily_horoscope.astroprofile = astro_prof
            daily_horoscope.save()

            return redirect(reverse('dashboard'))

    else:
        form = WeeklyHoroscopeForm(instance=weekly_horoscope)
        

    return render(request, 'horoscopes/createweeklyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deleteweeklyhoroscope(request, id):
    WeeklyHoroscope.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createmonthlyhoroscope(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = MonthlyHoroscopeForm(request.POST)
         
        if form.is_valid():
            monthly_horoscope = form.save(commit=False)
            monthly_horoscope.astroprofile = astro_prof
            monthly_horoscope.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = MonthlyHoroscopeForm()
        

    return render(request, 'horoscopes/createmonthlyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editmonthlyhoroscope(request, id):
    monthly_horoscope = MonthlyHoroscope.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = MonthlyHoroscopeForm(request.POST, instance=monthly_horoscope)

        if form.is_valid():
            monthly_horoscope = form.save(commit=False)
            monthly_horoscope.astroprofile = astro_prof
            monthly_horoscope.save()

            return redirect(reverse('dashboard'))

    else:
        form = MonthlyHoroscopeForm(instance=monthly_horoscope)
        

    return render(request, 'horoscopes/createmonthlyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletemonthlyhoroscope(request, id):
    MonthlyHoroscope.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createyearlyhoroscope(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyHoroscopeForm(request.POST)
         
        if form.is_valid():
            yearly_horoscope = form.save(commit=False)
            yearly_horoscope.astroprofile = astro_prof
            yearly_horoscope.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = YearlyHoroscopeForm()
        

    return render(request, 'horoscopes/createyearlyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def edityearlyhoroscope(request, id):
    yearly_horoscope = YearlyHoroscope.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyHoroscopeForm(request.POST, instance=yearly_horoscope)

        if form.is_valid():
            yearly_horoscope = form.save(commit=False)
            yearly_horoscope.astroprofile = astro_prof
            yearly_horoscope.save()

            return redirect(reverse('dashboard'))

    else:
        form = YearlyHoroscopeForm(instance=yearly_horoscope)
        

    return render(request, 'horoscopes/createyearlyhoroscope.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deleteyearlyhoroscope(request, id):
    YearlyHoroscope.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))

####################################################### HOROSCOPE CREATION VIEWS END ##########################



########################## PANCHANG CREATION VIEWS BEGIN #######################################################

@login_required(login_url='index')
@restrict_customer
def createdailypanchang(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyPanchangForm(request.POST)
         
        if form.is_valid():
            daily_panchang = form.save(commit=False)
            daily_panchang.astroprofile = astro_prof
            daily_panchang.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = DailyPanchangForm()
        

    return render(request, 'panchangs/createdailypanchang.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editdailypanchang(request, id):
    daily_panchang = DailyPanchang.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyPanchangForm(request.POST, instance=daily_panchang)

        if form.is_valid():
            daily_panchang = form.save(commit=False)
            daily_panchang.astroprofile = astro_prof
            daily_panchang.save()

            return redirect(reverse('dashboard'))

    else:
        form = DailyPanchangForm(instance=daily_panchang)
        

    return render(request, 'panchangs/createdailypanchang.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletedailypanchang(request, id):
    DailyPanchang.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createdailysolarcycle(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailySolarCycleForm(request.POST)
         
        if form.is_valid():
            daily_solarcycle = form.save(commit=False)
            daily_solarcycle.astroprofile = astro_prof
            daily_solarcycle.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = DailySolarCycleForm()
        

    return render(request, 'panchangs/createdailysolarcycle.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editdailysolarcycle(request, id):
    daily_solarcycle = DailySolarCycle.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailySolarCycleForm(request.POST, instance=daily_solarcycle)

        if form.is_valid():
            daily_solarcycle = form.save(commit=False)
            daily_solarcycle.astroprofile = astro_prof
            daily_solarcycle.save()

            return redirect(reverse('dashboard'))

    else:
        form = DailySolarCycleForm(instance=daily_solarcycle)
        

    return render(request, 'panchangs/createdailysolarcycle.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletedailysolarcycle(request, id):
    DailySolarCycle.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createhindumonthyear(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = HinduMonthYearForm(request.POST)
         
        if form.is_valid():
            hindu_month_year = form.save(commit=False)
            hindu_month_year.astroprofile = astro_prof
            hindu_month_year.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = HinduMonthYearForm()
        

    return render(request, 'panchangs/createhindumonthyear.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def edithindumonthyear(request, id):
    hindu_month_year = HinduMonthYear.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = HinduMonthYearForm(request.POST, instance=hindu_month_year)

        if form.is_valid():
            hindu_month_year = form.save(commit=False)
            hindu_month_year.astroprofile = astro_prof
            hindu_month_year.save()

            return redirect(reverse('dashboard'))

    else:
        form = HinduMonthYearForm(instance=hindu_month_year)
        

    return render(request, 'panchangs/createhindumonthyear.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletehindumonthyear(request, id):
    HinduMonthYear.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createdailytimings(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyTimingsForm(request.POST)
         
        if form.is_valid():
            daily_timings = form.save(commit=False)
            daily_timings.astroprofile = astro_prof
            daily_timings.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = DailyTimingsForm()
        

    return render(request, 'panchangs/createdailytimings.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editdailytimings(request, id):
    daily_timings = DailyTimings.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyTimingsForm(request.POST, instance=daily_timings)

        if form.is_valid():
            daily_timings = form.save(commit=False)
            daily_timings.astroprofile = astro_prof
            daily_timings.save()

            return redirect(reverse('dashboard'))

    else:
        form = DailyTimingsForm(instance=daily_timings)
        

    return render(request, 'panchangs/createdailytimings.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletedailytimings(request, id):
    DailyTimings.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


####################################################### PANCHANG CREATION VIEWS END ##########################




################### KUNDLI CREATION FORMS ###################################################################

def createkundli(request):
    if request.method == "POST":
        form = KundliForm(request.POST)
         
        if form.is_valid():
            form.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = KundliForm()
        

    return render(request, 'kundlis/createkundli.html', {'form':form})


######################### NUMEROLOGY CREATION VIEWS ###############################################################


@login_required(login_url='index')
@restrict_customer
def createdailynumerology(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyNumerologyForm(request.POST)
         
        if form.is_valid():
            daily_numerology = form.save(commit=False)
            daily_numerology.astroprofile = astro_prof
            daily_numerology.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = DailyNumerologyForm()
        

    return render(request, 'numerology/createdailynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editdailynumerology(request, id):
    daily_numerology = DailyNumerology.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = DailyNumerologyForm(request.POST, instance=daily_numerology)

        if form.is_valid():
            daily_numerology = form.save(commit=False)
            daily_numerology.astroprofile = astro_prof
            daily_numerology.save()

            return redirect(reverse('dashboard'))

    else:
        form = DailyNumerologyForm(instance=daily_numerology)
        

    return render(request, 'numerology/createdailynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletedailynumerology(request, id):
    DailyNumerology.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))

@login_required(login_url='index')
@restrict_customer
def createweeklynumerology(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = WeeklyNumerologyForm(request.POST)
         
        if form.is_valid():
            weekly_numerology = form.save(commit=False)
            weekly_numerology.astroprofile = astro_prof
            weekly_numerology.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = WeeklyNumerologyForm()
        

    return render(request, 'numerology/createweeklynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editweeklynumerology(request, id):
    weekly_numerology = WeeklyNumerology.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = WeeklyNumerologyForm(request.POST, instance=weekly_numerology)

        if form.is_valid():
            weekly_numerology = form.save(commit=False)
            weekly_numerology.astroprofile = astro_prof
            weekly_numerology.save()

            return redirect(reverse('dashboard'))

    else:
        form = WeeklyNumerologyForm(instance=weekly_numerology)
        

    return render(request, 'numerology/createweeklynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deleteweeklynumerology(request, id):
    WeeklyNumerology.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))

@login_required(login_url='index')
@restrict_customer
def createmonthlynumerology(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = MonthlyNumerologyForm(request.POST)
         
        if form.is_valid():
            monthly_numerology = form.save(commit=False)
            monthly_numerology.astroprofile = astro_prof
            monthly_numerology.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = MonthlyNumerologyForm()
        

    return render(request, 'numerology/createmonthlynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def editmonthlynumerology(request, id):
    monthly_numerology = MonthlyNumerology.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = MonthlyNumerologyForm(request.POST, instance=monthly_numerology)

        if form.is_valid():
            monthly_numerology = form.save(commit=False)
            monthly_numerology.astroprofile = astro_prof
            monthly_numerology.save()

            return redirect(reverse('dashboard'))

    else:
        form = MonthlyNumerologyForm(instance=monthly_numerology)
        

    return render(request, 'numerology/createmonthlynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletemonthlynumerology(request, id):
    MonthlyNumerology.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))

@login_required(login_url='index')
@restrict_customer
def createyearlynumerology(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyNumerologyForm(request.POST)
         
        if form.is_valid():
            yearly_numerology = form.save(commit=False)
            yearly_numerology.astroprofile = astro_prof
            yearly_numerology.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = YearlyNumerologyForm()
        

    return render(request, 'numerology/createyearlynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def edityearlynumerology(request, id):
    yearly_numerology = YearlyNumerology.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyNumerologyForm(request.POST, instance=yearly_numerology)

        if form.is_valid():
            yearly_numerology = form.save(commit=False)
            yearly_numerology.astroprofile = astro_prof
            yearly_numerology.save()

            return redirect(reverse('dashboard'))

    else:
        form = YearlyNumerologyForm(instance=yearly_numerology)
        

    return render(request, 'numerology/createyearlynumerology.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deleteyearlynumerology(request, id):
    YearlyNumerology.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


#################################################### 


############### TAROT CREATION VIEWS BEGIN#######################################################################3

@login_required(login_url='index')
@restrict_customer
def createyearlytarot(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyTarotForm(request.POST)
         
        if form.is_valid():
            yearly_tarot = form.save(commit=False)
            yearly_tarot.astroprofile = astro_prof
            yearly_tarot.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = YearlyTarotForm()
        

    return render(request, 'tarots/createyearlytarot.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def edityearlytarot(request, id):
    yearly_tarot = YearlyTarot.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = YearlyTarotForm(request.POST, instance=yearly_tarot)

        if form.is_valid():
            yearly_tarot = form.save(commit=False)
            yearly_tarot.astroprofile = astro_prof
            yearly_tarot.save()

            return redirect(reverse('dashboard'))

    else:
        form = YearlyTarotForm(instance=yearly_tarot)
        

    return render(request, 'tarots/createyearlytarot.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deleteyearlytarot(request, id):
    YearlyTarot.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))


@login_required(login_url='index')
@restrict_customer
def createtarotarticle(request):
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = TarotArticleForm(request.POST)
         
        if form.is_valid():
            tarot_article = form.save(commit=False)
            tarot_article.astroprofile = astro_prof
            tarot_article.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = TarotArticleForm()
        

    return render(request, 'tarots/createtarotarticle.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def edittarotarticle(request, id):
    tarot_article = TarotArticle.objects.get(pk=id)
    astro_prof = request.user.profile.astro_profile
    if request.method == "POST":
        form = TarotArticleForm(request.POST, instance=tarot_article)

        if form.is_valid():
            tarot_article = form.save(commit=False)
            tarot_article.astroprofile = astro_prof
            tarot_article.save()

            return redirect(reverse('dashboard'))

    else:
        form = TarotArticleForm(instance=tarot_article)
        

    return render(request, 'tarots/createtarotarticle.html', {'form':form})

@login_required(login_url='index')
@restrict_customer
def deletetarotarticle(request, id):
    TarotArticle.objects.filter(pk=id).delete()
    return redirect(reverse('dashboard'))



################################## Love Creation Views ###########################################################

def checklove(request):
    if request.method == "POST":
        form = LoveForm(request.POST)
         
        if form.is_valid():
            form.save()

            
            return redirect(reverse('dashboard'))

    else:
        form = LoveForm()
        

    return render(request, 'love/checklove.html', {'form':form})

def viewlove(request):
    posts = Post.objects.filter(title__icontains = 'Love')
    return render(request, 'love/viewlove.html', {'posts':posts})




################################################################# Love Creation Views End ########################    






############################################################################ Tarot ##############################


def viewtarot(request):
    articles = YearlyTarot.objects.all()
    tarot_articles = TarotArticle.objects.all()
    posts = Post.objects.filter(title__icontains = 'Tarot')
    return render(request, 'tarots/viewtarot.html', {'posts':posts,'tarot_articles':tarot_articles,'articles':articles})

def viewtarotarticle(request, id):
    article = TarotArticle.objects.filter(pk=id)
    return render(request, 'tarots/viewtarotarticle.html', {'article':article})

def viewyearlytarot(request):
    articles = YearlyTarot.objects.all()
    return render(request, 'tarots/viewyearlytarot.html', {'articles':articles})


def viewkundli(request):
    
    return render(request, 'kundlis/viewkundli.html')



def viewpanchang(request):
    today_date = date.today()
    today_panchang = DailyPanchang.objects.all().filter(date=today_date)
    today_solar_cycle = DailySolarCycle.objects.all().filter(date=today_date)
    today_hindu_month_year = HinduMonthYear.objects.all().filter(date=today_date)
    today_timings = DailyTimings.objects.all().filter(date=today_date)
    
    context = {'today_panchang':today_panchang, 'today_solar_cycle':today_solar_cycle, 'today_hindu_month_year':today_hindu_month_year, 'today_timings':today_timings }
    


    
    return render(request, 'panchangs/viewpanchang.html', context)


def horoscope(request):
    today_date = date.today()
    tomo_date = today_date + timedelta(days=1)
    today_normal_horo = DailyHoroscope.objects.all().filter(date=today_date, category='Normal')
    tomo_normal_horo = DailyHoroscope.objects.all().filter(date=tomo_date, category='Normal')[:4]
    context = {'today_normal_horo':today_normal_horo, 'tomo_normal_horo':tomo_normal_horo }
    return render(request, 'horoscopes/horoscope.html', context)


def viewdailyhoroscope(request, id):
    horoscope = DailyHoroscope.objects.get(pk=id)
    comments = DHComment.objects.filter(horoscope=horoscope)
    sim_zodi = horoscope.zodiac
    sim_cate = horoscope.category
    sim_date = horoscope.date
    sim_week_horo = WeeklyHoroscope.objects.all().filter(zodiac=sim_zodi, category=sim_cate, from_date__lte=sim_date)
    sim_zodi_horo = DailyHoroscope.objects.all().filter(zodiac=sim_zodi, date=sim_date)
    sim_date_horo = DailyHoroscope.objects.all().filter(date=sim_date, category='Normal')
    sim_cate_horo = DailyHoroscope.objects.all().filter(category=sim_cate, date=sim_date)[:3]
    context = {'comments':comments,'sim_cate_horo':sim_cate_horo,'sim_date_horo':sim_date_horo,'sim_zodi_horo':sim_zodi_horo,'horoscope':horoscope, 'sim_week_horo':sim_week_horo}

    return render(request, 'horoscopes/dailyhoroscope.html', context)



def viewweeklyhoroscope(request,id):
    horoscope = WeeklyHoroscope.objects.get(pk=id)
    sim_zodi = horoscope.zodiac
    sim_cate = horoscope.category
    sim_from_date = horoscope.from_date
    sim_to_date = horoscope.to_date
    sim_zodi_horo = WeeklyHoroscope.objects.all().filter(zodiac=sim_zodi, from_date=sim_from_date, to_date=sim_to_date)
    sim_week_horo = WeeklyHoroscope.objects.all().filter(from_date=sim_from_date, to_date=sim_to_date, category='Normal')
    sim_cate_horo = WeeklyHoroscope.objects.all().filter(category=sim_cate, from_date=sim_from_date, to_date=sim_to_date)[:3]
    context = {'sim_cate_horo':sim_cate_horo,'sim_week_horo':sim_week_horo,'sim_zodi_horo':sim_zodi_horo,'horoscope':horoscope}

    return render(request, 'horoscopes/weeklyhoroscope.html', context)

