from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# import django.template as template
import os
from site_server import settings
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the mygame index.")
    return render(request, 'index.html')
def game_info(request, game_name):
    # file_path = os.path.join(settings.GAME_FILES_PATH, game_name, 'game.html')
    # print('file_path')
    # with open(file_path, 'r') as file:
    #     html_content = file.read()
    # return HttpResponse(html_content)
    template = loader.get_template('my_games/sudoku/index.html')
    return HttpResponse(template.render({'a':1}, request))