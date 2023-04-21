from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'combined_bridge'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Page1(Page):
    timeout_seconds = 10

class WaitForAll(WaitPage):
    wait_for_all_groups = True
    body_text = "Bitte warten Sie, bis die anderen Teilnehmer Experiment 1 ebenfalls abgeschlossen haben."

page_sequence = [WaitForAll, Page1]
