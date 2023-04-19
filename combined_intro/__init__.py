from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'combined_intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# Functions
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.vars['exp_to_pay'] = random.randint(1, 2)

# PAGES
class Page1(Page):
    pass

class Page2(Page):
    timeout_seconds = 5


page_sequence = [Page1, Page2]
