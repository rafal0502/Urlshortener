from django.shortcuts import render, render_to_response, get_object_or_404
import random, string, json
from shorterurl.models import Urls



def index()