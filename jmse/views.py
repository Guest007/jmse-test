# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Estate


class EstateList(ListView):
    """List of all stores with pagination and filters"""

    queryset = Estate.objects.filter(is_publish=True)
    paginate_by = 21
    template_name = 'base.html'

    # def get_queryset(self):