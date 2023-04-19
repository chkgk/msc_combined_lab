from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'oerconfidence_prime'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TREATMENTS = ['control', 'treatment']


def creating_session(subsession):
    for p in subsession.get_players():
        p.treatment = random.choice(C.TREATMENTS)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.LongStringField()
    control_field = models.LongStringField(label="Sie haben nun 5 Minuten Zeit, um über den gestrigen Tag nachzudenken und ihn zu beschreiben:")
    treatment_field = models.LongStringField(label="Sie haben nun 5 Minuten Zeit, um über das Ereignis nachzudenken und die Situation zu schildern:")



class ControlQuestion(Page):
    timeout_seconds = 320
    def is_displayed(player):
        return player.treatment == 'control'
    
    form_model = 'player'
    form_fields = ['control_field']

class TreatmentQuestion(Page):
    timeout_seconds = 320
    def is_displayed(player):
        return player.treatment == 'treatment'
    
    form_model = 'player'
    form_fields = ['treatment_field']

page_sequence = [ControlQuestion, TreatmentQuestion]


