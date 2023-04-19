from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'overconfidence_measurement'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    luther_lower = models.IntegerField(min=0, label="Untere Grenze")
    luther_upper = models.IntegerField(min=0, label="Obere Grenze")

    nil_lower = models.IntegerField(min=0, label="Untere Grenze")
    nil_upper = models.IntegerField(min=0, label="Obere Grenze")

    bridge_lower = models.IntegerField(min=0, label="Untere Grenze")
    bridge_upper = models.IntegerField(min=0, label="Obere Grenze")

    turm_lower = models.IntegerField(min=0, label="Untere Grenze")
    turm_upper = models.IntegerField(min=0, label="Obere Grenze")

    boeing_lower = models.IntegerField(min=0, label="Untere Grenze")
    boeing_upper = models.IntegerField(min=0, label="Obere Grenze")

    bach_lower = models.IntegerField(min=0, label="Untere Grenze")
    bach_upper = models.IntegerField(min=0, label="Obere Grenze")

    elefant_lower = models.IntegerField(min=0, label="Untere Grenze")
    elefant_upper = models.IntegerField(min=0, label="Obere Grenze")

    mond_lower = models.IntegerField(min=0, label="Untere Grenze")
    mond_upper = models.IntegerField(min=0, label="Obere Grenze")

    londontokio_lower = models.IntegerField(min=0, label="Untere Grenze")
    londontokio_upper = models.IntegerField(min=0, label="Obere Grenze")

    unabhängigkeit_lower = models.IntegerField(min=0, label="Untere Grenze")
    unabhängigkeit_upper = models.IntegerField(min=0, label="Obere Grenze")

# PAGES
class overconfidence(Page):
    pass

class q_1(Page):

    form_model = 'player'
    form_fields = ['luther_lower', 'luther_upper']

class q_2(Page):
    form_model = 'player'
    form_fields = ['nil_lower', 'nil_upper']

class q_3(Page):
    form_model = 'player'
    form_fields = ['bridge_lower', 'bridge_upper']

class q_4(Page):
    form_model = 'player'
    form_fields = ['turm_lower', 'turm_upper']

class q_5(Page):
    form_model = 'player'
    form_fields = ['boeing_lower', 'boeing_upper']

class q_6(Page):
    form_model = 'player'
    form_fields = ['bach_lower', 'bach_upper']

class q_7(Page):
    form_model = 'player'
    form_fields = ['elefant_lower', 'elefant_upper']

class q_8(Page):
    form_model = 'player'
    form_fields = ['mond_lower', 'mond_upper']

class q_9(Page):
    form_model = 'player'
    form_fields = ['londontokio_lower', 'londontokio_upper']

class q_10(Page):
    form_model = 'player'
    form_fields = ['unabhängigkeit_lower', 'unabhängigkeit_upper']

class WaitForAll(WaitPage):
    wait_for_all_groups = True


page_sequence = [overconfidence, q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
