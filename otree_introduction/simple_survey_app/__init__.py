from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'simple_survey_app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()


# PAGES
class Survey(Page):
    form_model = "player"
    form_fields = ["name", "age"]

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        name = player.name
        age = player.age
        return {
            "name": name,
            "age": age
        }


page_sequence = [Survey, Results]
