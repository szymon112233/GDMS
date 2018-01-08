from django.forms import ModelForm
from mainGDMS.models import *


class EnemiesForm(ModelForm):
    class Meta:
        model = enemy
        fields = ('name', 'modelID', 'damage', 'speed', 'health', 'vision_range', 'chase_range')

class SkillsForm(ModelForm):
    class Meta:
        model = skill
        fields = ('name', 'desc', 'req_lvl', 'damage', 'is_targeted', 'is_aoe', 'is_passive')

class ItemForm(ModelForm):
    class Meta:
        model = item
        fields = ('name', 'desc', 'type', 'damage')

class PlayersForm(ModelForm):
    class Meta:
        model = player
        fields = ('user',)

class CharacterForm(ModelForm):
    class Meta:
        model = character
        fields = ('name', 'owner')

class NpcsForm(ModelForm):
    class Meta:
        model = npc
        fields = ('name', 'spriteID')

class SkillbookForm(ModelForm):
    class Meta:
        model = skillbook
        fields = ('skill_base', 'skill_owner')

class ConfigForm(ModelForm):
    class Meta:
        model = configs
        fields = ('database_ver', 'game_ver', 'exp_mult')

class InvForm(ModelForm):
    class Meta:
        model = inventory
        fields = ('item_base', 'item_owner')

class LocaleForm(ModelForm):
    class Meta:
        model = locale
        fields = ('default_transl', 'en_transl', 'pl_transl')
