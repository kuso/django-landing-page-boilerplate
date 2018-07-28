# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def landing_page(request):
    output = render_to_string('index.html', {})
    return HttpResponse(output)
