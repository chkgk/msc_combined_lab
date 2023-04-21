from otree.api import *
import math

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=16, max=110, label="Wie alt sind Sie?")
    geschlecht = models.IntegerField(
        label="Geschlecht:",
        choices=[
            [1, 'Männlich'],
            [2, 'Weiblich'],
            [3, 'Anderes'],
            [3, 'Keine Angabe'],
        ],
    )
    bildungsgrad = models.IntegerField(
        label="Höchster Bildungsabschluss:",
        choices=[
            [1, 'Abitur'],
            [2, 'Bachelor'],
            [3, 'Diplom'],
            [4, 'Master'],
            [5, 'PhD'],
            [6, 'Sonstiges'],
        ],
    )

    gehaltene_anlageprodukte = models.IntegerField(
        label="Wie viele verschiedene Anlageprodukte (z.B. Aktien, Fonds, Anleihen, Zertifikate) haben Sie innerhalb des letzten Jahres gehalten?",
        choices=[
            [1, '0'],
            [2, '1-5'],
            [3, '6-10'],
            [4, 'Mehr als 10'],
            [5, 'Weiß ich nicht'],
        ],
    )

    beschäftigungsstatus = models.IntegerField(
        label="Derzeitiger Beschäftigungsstatus:",
        choices=[
            [1, 'Vollzeit'],
            [2, 'Teilzeit'],
            [3, 'Vollzeitstudent'],
            [4, 'Weder beschäftigt noch Student'],
        ],
    )
    # check these
 
    field_of_studies = models.StringField(label='Was ist/war Ihre Hauptrichtung im Studium?')

# FUNCTIONS
def round_up_to_next_20_cents(value):
    return math.ceil(value * 5) / 5


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'geschlecht', 'bildungsgrad', 'gehaltene_anlageprodukte', 'beschäftigungsstatus', "field_of_studies"]

class Payoff(Page):
    def vars_for_template(player: Player):
        part = player.participant
        return {
            'pay_exp': part.vars.get('exp_to_pay', 0),
            'exp1_pay_round': part.vars.get('round_to_pay', 0),
            'exp1_pay_ecu': part.vars.get('exp1_pay_ecu', 0),
            'exp1_pay_eur': round(part.vars.get('exp1_pay_ecu', 0) / 10, 2),
            'exp2_task': part.vars.get('exp2_task', 0),
            'banks2_round': part.vars.get('banks2_round_to_pay', 0),
            'banks2_coinflip': part.vars.get('banks2_coinflip', None),
            'banks5_round': part.vars.get('banks5_round_to_pay', 0),
            'banks5_coinflip': part.vars.get('banks5_coinflip', None),
            'exp2_pay_ecu': part.vars.get('exp2_pay_ecu', 0),
            'exp2_pay_eur': round(part.vars.get('exp2_pay_ecu', 0) / 10, 2),
            'rounded_payoff': round_up_to_next_20_cents(part.payoff/10 + player.session.config['participation_fee'])
        }

page_sequence = [Demographics, Payoff]
