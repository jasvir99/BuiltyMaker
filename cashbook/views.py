from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from BuiltyMaker.builty.models import *
from django.template import *
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Max ,Q, Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.db.models import F
from django import template
from tagging.models import Tag, TaggedItem
from django.core.mail import send_mail
import datetime

def index(request):
	if request.user.is_active == 1:
		return render_to_response('cashbook/index.html')
	else:
		return render_to_response('cashbook/index1.html')
