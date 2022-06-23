import discord
from discord.ext import commands
from django.apps import AppConfig
from django.shortcuts import render
client = discord.Client()


# Create your views here.
from django.http import HttpResponse


def startbot(request):

    return HttpResponse("yoyoyoyoyoyo im a bot but started.")


def stopbot(request):
    return HttpResponse("yoyoyoyoyoyo im a bot but stoped.")    
    @client.command(aliases=["quit"])

    