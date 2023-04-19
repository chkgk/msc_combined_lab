from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

# Functions
def creating_session(subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['exp2_task'] = random.choice([2, 5])

# PAGES
class Instructions(Page):
    pass

page_sequence = [Instructions]
