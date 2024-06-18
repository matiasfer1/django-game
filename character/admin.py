from django.contrib import admin
from character.models import Player, Enemy

admin.site.register([Player, Enemy])