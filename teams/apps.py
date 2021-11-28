from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TeamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teams'


class GoalsConfig(AppConfig):
    name = 'cmdbox.goals'
    verbose_name = _('goals')
