from otree.api import *
import pandas as pd
import random


author = 'Felix Holzmeister'
doc = 'Allocation decision task with two assets as in Banks et al. (2017)'


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS
# ******************************************************************************************************************** #
class C(BaseConstants):
    NAME_IN_URL = 'banks_two_assets'
    PLAYERS_PER_GROUP = None

    # import choice sets from *.xlsx-file
    # ----------------------------------------------------------------------------------------------------------------
    f = pd.read_excel('_static/banks_two_assets/data/assets.xlsx')
    choice_sets = list(zip(
        f['set'],
        f['a_h'].tolist(), f['a_t'].tolist(),
        f['b_h'].tolist(), f['b_t'].tolist()
    ))

    NUM_ROUNDS = len(f['n'])



# ******************************************************************************************************************** #
# *** CLASS SUBSESSION
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    pass


# ******************************************************************************************************************** #
# *** CLASS GROUP
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # model fields: assets
    # ----------------------------------------------------------------------------------------------------------------
    c_set = models.IntegerField(
        doc="number/id of decision (1 - 10)"
    )
    a_h = models.FloatField(
        doc="asset a: outcome heads"
    )
    a_t = models.FloatField(
        doc="asset a: outcome tails"
    )
    b_h = models.FloatField(
        doc="asset b: outcome heads"
    )
    b_t = models.FloatField(
        doc="asset b: outcome tails"
    )

    # model fields: investment decision
    # ----------------------------------------------------------------------------------------------------------------
    asset_a = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        doc="player's investment decision: allocation to asset a"
    )
    asset_b = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        doc="player's investment decision: allocation to asset b"
    )

    # model fields: outcomes
    # ----------------------------------------------------------------------------------------------------------------
    heads = models.FloatField(
        doc="portfolio payoff if coin shows up heads"
    )
    tails = models.FloatField(
        doc="portfolio payoff if coin shows up tails"
    )
    paid_for = models.StringField()



# shuffle choice sets on participant level
# ----------------------------------------------------------------------------------------------------------------
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['adt2_choice_sets'] = C.choice_sets.copy()
            random.shuffle(p.participant.vars['adt2_choice_sets'])
            p.participant.vars['banks2_round_to_pay'] = random.randint(1, C.NUM_ROUNDS)


# ******************************************************************************************************************** #
# *** CLASS DECISION
# ******************************************************************************************************************** #
class Anleitung(Page):
    pass

class Decision(Page):

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = [
        'asset_a',
        'asset_b'
    ]

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(player: Player):

        # specify info for progress bar
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        total = C.NUM_ROUNDS
        page = player.subsession.round_number
        progress = round(page / total * 100)

        # asset payoffs
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        choice_sets = player.participant.vars['adt2_choice_sets']
        c_set = player.c_set = choice_sets[page - 1][0]

        a_h = player.a_h = choice_sets[page - 1][1]
        a_t = player.a_t = choice_sets[page - 1][2]
        b_h = player.b_h = choice_sets[page - 1][3]
        b_t = player.b_t = choice_sets[page - 1][4]

        return {
            'page':             page,
            'total':            total,
            'progress':         progress,
            'c_set':            c_set,
            'a_h':              a_h,
            'a_t':              a_t,
            'b_h':              b_h,
            'b_t':              b_t,
            'y_title':          'Your Investment'
        }

    # before next page...
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(player: Player, timeout_happened):
        round_num = player.subsession.round_number
        # payoffs
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        a_h = float(player.a_h)
        a_t = float(player.a_t)
        b_h = float(player.b_h)
        b_t = float(player.b_t)

        # outcome if "heads" is drawn
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        heads = sum([
            a_h * player.asset_a,
            b_h * player.asset_b
        ]) 
        player.heads = heads

        # outcome if "tails" is drawn
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        tails = sum([
            a_t * player.asset_a,
            b_t * player.asset_b
        ]) 
        player.tails = tails

        if player.participant.vars['exp_to_pay'] == 2 and player.participant.vars['exp2_task'] == 2 and round_num == player.participant.vars['banks2_round_to_pay']:
            pay_for = random.choice(['Kopf', 'Zahl'])
            player.paid_for = pay_for
            player.participant.vars["banks_coinflip"] = pay_for
            player.participant.vars["banks_round"] = round_num
            player.payoff = player.heads if pay_for == 'Kopf' else player.tails
            player.participant.vars["exp2_pay_ecu"] = player.payoff


# ******************************************************************************************************************** #
# *** CLASS PAGE SEQUENCE
# ******************************************************************************************************************** #
page_sequence = [Decision]
