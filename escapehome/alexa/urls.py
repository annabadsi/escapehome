from django.urls import path
from django_ask_sdk.skill_adapter import SkillAdapter

from alexa.skill import skill

view = SkillAdapter.as_view(skill=skill, verify_signature=False)

urlpatterns = [
    path("", view, name="index")
]
