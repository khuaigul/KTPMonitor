from ..models import MyUser
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .. import tokens
from django.utils.encoding import force_bytes
from ..models import *
from .DB.main_DB_modul import *
def registration_Re(request):
    to_email = request.POST['email']
    password = request.POST['password'] 
    if User.objects.filter(email=to_email).first() is not None:
        return {'status': False}       
    myuser = User.objects.create_user(to_email, to_email, password)
    muser = MyUser.objects.create(user=myuser)
    myuser.is_active = False
    muser.save()
    myuser.save()               
    current_site = get_current_site(request)         
    message = render_to_string('acc_active_email.html', {
            'user': myuser,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': tokens.account_activation_token.make_token(myuser),
        })        
    mail_subject = 'Activate your blog account.'        
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
    return {'status': True}