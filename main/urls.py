from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path


   





urlpatterns = [
    path('homeview', views.homeview, name="homeview"),
    path('post/<slug:slug>/', views.detailview, name="detailview"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
######## Added on 10jul2020
    ## register login paths, login path provided by default 
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    ## profile edit paths
    path('completeprofile', views.completeprofile, name='completeprofile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('updateprofilepic', views.updateprofilepic, name='updateprofilepic'),
    ## astroprofile creation and update paths
    path('createastroprofile', views.createastroprofile, name='createastroprofile'),
    path('updateastroprofile', views.updateastroprofile, name='updateastroprofile'),
    ## Wallet paths
    url(r'^recharge/$', views.recharge, name='recharge'),
    url(r'^charge/$', views.charge, name='charge'),
    ## password reset paths , default paths with no view only templates
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name='password_reset_complete'),
    path('astrosearch/', views.astrosearch, name='astrosearch'),
    path('astrodetail<str:id>', views.astrodetail, name='astrodetail'),

    ## Horoscopes urls
    path('horoscope', views.horoscope, name='horoscope'),
    path('viewdailyhoroscope<str:id>', views.viewdailyhoroscope, name='viewdailyhoroscope'),
    path('viewweeklyhoroscope<str:id>', views.viewweeklyhoroscope, name='viewweeklyhoroscope'),
    path('createdailyhoroscope', views.createdailyhoroscope, name='createdailyhoroscope'),
    path('editdailyhoroscope<str:id>', views.editdailyhoroscope, name='editdailyhoroscope'),
    path('deletedailyhoroscope<str:id>', views.deletedailyhoroscope, name='deletedailyhoroscope'),
    path('createweeklyhoroscope', views.createweeklyhoroscope, name='createweeklyhoroscope'),
    path('editweeklyhoroscope<str:id>', views.editweeklyhoroscope, name='editweeklyhoroscope'),
    path('deleteweeklyhoroscope<str:id>', views.deleteweeklyhoroscope, name='deleteweeklyhoroscope'),
    path('createmonthlyhoroscope', views.createmonthlyhoroscope, name='createmonthlyhoroscope'),
    path('editmonthlyhoroscope<str:id>', views.editmonthlyhoroscope, name='editmonthlyhoroscope'),
    path('deletemonthlyhoroscope<str:id>', views.deletemonthlyhoroscope, name='deletemonthlyhoroscope'),
    path('createyearlyhoroscope', views.createyearlyhoroscope, name='createyearlyhoroscope'),
    path('edityearlyhoroscope<str:id>', views.edityearlyhoroscope, name='edityearlyhoroscope'),
    path('deleteyearlyhoroscope<str:id>', views.deleteyearlyhoroscope, name='deleteyearlyhoroscope'),
    ## Panchang urls
    path('viewpanchang', views.viewpanchang, name='viewpanchang'),
    path('createdailypanchang', views.createdailypanchang, name='createdailypanchang'),
    path('editdailypanchang<str:id>', views.editdailypanchang, name='editdailypanchang'),
    path('deletedailypanchang<str:id>', views.deletedailypanchang, name='deletedailypanchang'),
    path('createdailysolarcycle', views.createdailysolarcycle, name='createdailysolarcycle'),
    path('editdailysolarcycle<str:id>', views.editdailysolarcycle, name='editdailysolarcycle'),
    path('deletedailysolarcycle<str:id>', views.deletedailysolarcycle, name='deletedailysolarcycle'),
    path('createhindumonthyear', views.createhindumonthyear, name='createhindumonthyear'),
    path('edithindumonthyear<str:id>', views.edithindumonthyear, name='edithindumonthyear'),
    path('deletehindumonthyear<str:id>', views.deletehindumonthyear, name='deletehindumonthyear'),
    path('createdailytimings', views.createdailytimings, name='createdailytimings'),
    path('editdailytimings<str:id>', views.editdailytimings, name='editdailytimings'),
    path('deletedailytimings<str:id>', views.deletedailytimings, name='deletedailytimings'),
    ## Kundli urls
    path('createkundli', views.createkundli, name='createkundli'),
    path('viewkundli', views.viewkundli, name='viewkundli'),
    ## Numerology urls
    path('createdailynumerology', views.createdailynumerology, name='createdailynumerology'),
    path('editdailynumerology<str:id>', views.editdailynumerology, name='editdailynumerology'),
    path('deletedailynumerology<str:id>', views.deletedailynumerology, name='deletedailynumerology'),
    path('createweeklynumerology', views.createweeklynumerology, name='createweeklynumerology'),
    path('editweeklynumerology<str:id>', views.editweeklynumerology, name='editweeklynumerology'),
    path('deleteweeklynumerology<str:id>', views.deleteweeklynumerology, name='deleteweeklynumerology'),
    path('createmonthlynumerology', views.createmonthlynumerology, name='createmonthlynumerology'),
    path('editmonthlynumerology<str:id>', views.editmonthlynumerology, name='editmonthlynumerology'),
    path('deletemonthlynumerology<str:id>', views.deletemonthlynumerology, name='deletemonthlynumerology'),
    path('createyearlynumerology', views.createyearlynumerology, name='createyearlynumerology'),
    path('edityearlynumerology<str:id>', views.edityearlynumerology, name='edityearlynumerology'),
    path('deleteyearlynumerology<str:id>', views.deleteyearlynumerology, name='deleteyearlynumerology'),
    ## Tarot urls
    path('createyearlytarot', views.createyearlytarot, name='createyearlytarot'),
    path('edityearlytarot<str:id>', views.edityearlytarot, name='edityearlytarot'),
    path('deleteyearlytarot<str:id>', views.deleteyearlytarot, name='deleteyearlytarot'),
    path('createtarotarticle', views.createtarotarticle, name='createtarotarticle'),
    path('edittarotarticle<str:id>', views.edittarotarticle, name='edittarotarticle'),
    path('deletetarotarticle<str:id>', views.deletetarotarticle, name='deletetarotarticle'),
    path('viewtarot', views.viewtarot, name='viewtarot'),
    path('viewtarotarticle<str:id>', views.viewtarotarticle, name='viewtarotarticle'),
    path('viewyearlytarot', views.viewyearlytarot, name='viewyearlytarot'),
    ## Love urls
    path('checklove', views.checklove, name='checklove'),
    path('viewlove', views.viewlove, name='viewlove'),
    





   


    
]