from django.urls import path
from .views import *

urlpatterns = [
    # landing pages
    path('', homePage, name='home'),
    path('dashboard', adminHome, name='adminHome'),

    path('add/', addChild,name='add-child'),
    path('update-child/<str:pk>', updateChild,name='update-child'),
    path('delete/<str:pk>', deleteChild,name='delete'),
    path('children', fetchChildren,name='child-list'),
    path('sponsor/', addSponsor,name='add-sponsor'),
    path('sponsor-list/', getSponsors,name='sponsor-list'),
    path('add-employee/', addEmployee,name='add-employee'),
    path('employee-list/', getEmployees,name='employee-list'),

    # login url and logout url
    path('signin', userLogin,name='login'),
    path('signout', userLogout,name='logout'),
   
    #update urls
    path('sponsor/update/<str:pk>',updateSponsor, name='update-sponsor'),


    #delete urls
    path('delSponsor/<str:pk>',deleteSponsor, name='delete-sponsor'),

    #registration and login urls
    path('register/', addAdmin,name='register'),

    # url for sending an email
    path('enquiry', send_email,name='enquiry-mail'),
    
]
