from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


class IndexView(View):
    def get(self, *args, **kwargs):
        return HttpResponse()


class ListView(TemplateView):
    template_name = 'base.html'