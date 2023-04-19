from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'banks_5_anleitung'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class WaitForAll(WaitPage):
    wait_for_all_groups = True

class Anleitung(Page):
    pass



page_sequence = [WaitForAll, Anleitung]
