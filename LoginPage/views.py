# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import LoginPage


class LogIn(View):

    def get(self, request):
    	loginPage = LoginPage()
    	return render(request, "login.html", {'loginPage': loginPage})

    def post(self, request):
    	loginPage = LoginPage(request.POST)
    	if loginPage.is_valid():
    		return render(request, "login.html", {'loginPage': loginPage})

	