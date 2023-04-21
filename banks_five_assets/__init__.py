from otree.api import *
import pandas as pd
import random


author = 'Felix Holzmeister'
doc = 'Allocation decision task with five assets as in Banks et al. (2017)'



# ******************************************************************************************************************** #
# *** CLASS CONSTANTS
# ******************************************************************************************************************** #
class C(BaseConstants):
    NAME_IN_URL = 'banks_five_assets'
    PLAYERS_PER_GROUP = None

    # import choice sets from *.xlsx-file
    # ----------------------------------------------------------------------------------------------------------------
    f = pd.read_excel('_static/banks_five_assets/data/assets.xlsx')
    choice_sets = list(zip(
        f['set'],
        f['a_h'].tolist(), f['a_t'].tolist(),
        f['b_h'].tolist(), f['b_t'].tolist(),
        f['c_h'].tolist(), f['c_t'].tolist(),
        f['d_h'].tolist(), f['d_t'].tolist(),
        f['e_h'].tolist(), f['e_t'].tolist(),
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
    c_h = models.FloatField(
        doc="asset c: outcome heads"
    )
    c_t = models.FloatField(
        doc="asset c: outcome tails"
    )
    d_h = models.FloatField(
        doc="asset d: outcome heads"
    )
    d_t = models.FloatField(
        doc="asset d: outcome tails"
    )
    e_h = models.FloatField(
        doc="asset e: outcome heads"
    )
    e_t = models.FloatField(
        doc="asset e: outcome tails"
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
    asset_c = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        doc="player's investment decision: allocation to asset c"
    )
    asset_d = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        doc="player's investment decision: allocation to asset d"
    )
    asset_e = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        doc="player's investment decision: allocation to asset e"
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

    # c_set globals for randomly chosen decision
    # ----------------------------------------------------------------------------------------------------------------
    risk_perception = models.IntegerField(
        doc="player's self-reported perception of the risk level associated with the 25 decisions (scale: 1 - 4)"
    )


# shuffle choice sets on participant level
# ----------------------------------------------------------------------------------------------------------------
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            p.participant.vars['adt5_choice_sets'] = C.choice_sets.copy()
            random.shuffle(p.participant.vars['adt5_choice_sets'])
            p.participant.vars['banks5_round_to_pay'] = random.randint(1, C.NUM_ROUNDS)


# ******************************************************************************************************************** #
# *** CLASS DECISION
# ******************************************************************************************************************** #
class Decision(Page):
    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = [
        'asset_a',
        'asset_b',
        'asset_c',
        'asset_d',
        'asset_e'
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
        choice_sets = player.participant.vars['adt5_choice_sets']
        cset = player.c_set = choice_sets[page - 1][0]

        a_h = player.a_h = choice_sets[page - 1][1]
        a_t = player.a_t = choice_sets[page - 1][2]
        b_h = player.b_h = choice_sets[page - 1][3]
        b_t = player.b_t = choice_sets[page - 1][4]
        c_h = player.c_h = choice_sets[page - 1][5]
        c_t = player.c_t = choice_sets[page - 1][6]
        d_h = player.d_h = choice_sets[page - 1][7]
        d_t = player.d_t = choice_sets[page - 1][8]
        e_h = player.e_h = choice_sets[page - 1][9]
        e_t = player.e_t = choice_sets[page - 1][10]

        return {
            'page':         page,
            'total':        total,
            'progress':     progress,
            'c_set':        cset,
            'a_h':          a_h,
            'a_t':          a_t,
            'b_h':          b_h,
            'b_t':          b_t,
            'c_h':          c_h,
            'c_t':          c_t,
            'd_h':          d_h,
            'd_t':          d_t,
            'e_h':          e_h,
            'e_t':          e_t,
            'y_title':      'Your Investment'
        }

    # before next page...
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(player: Player, timeout_happened):
        choice_sets = player.participant.vars['adt5_choice_sets']

        # payoffs
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        a_h = float(player.a_h)
        a_t = float(player.a_t)
        b_h = float(player.b_h)
        b_t = float(player.b_t)
        c_h = float(player.c_h)
        c_t = float(player.c_t)
        d_h = float(player.d_h)
        d_t = float(player.d_t)
        e_h = float(player.e_h)
        e_t = float(player.e_t)

        # outcome if "heads" is drawn
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        heads = sum([
            a_h * player.asset_a,
            b_h * player.asset_b,
            c_h * player.asset_c,
            d_h * player.asset_d,
            e_h * player.asset_e
        ]) 
        player.heads = heads

        # outcome if "tails" is drawn
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        tails = sum([
            a_t * player.asset_a,
            b_t * player.asset_b,
            c_t * player.asset_c,
            d_t * player.asset_d,
            e_t * player.asset_e
        ]) 
        player.tails = tails

        if player.participant.vars['exp_to_pay'] == 2 and player.participant.vars['exp2_task'] == 5 and player.round_number == player.participant.vars['banks5_round_to_pay']:
            pay_for = random.choice(['Kopf', 'Zahl'])
            player.paid_for = pay_for
            player.participant.vars["banks5_coinflip"] = pay_for
            player.participant.vars["banks5_round"] = player.round_number
            player.payoff = player.heads if pay_for == 'Kopf' else player.tails
            player.participant.vars["exp2_pay_ecu"] = player.payoff
            # print(f"Player {player.id_in_subsession} has been paid {player.payoff} ECU for round {player.round_number} of experiment 2 task 5.")


# ******************************************************************************************************************** #
# *** CLASS PAGE SEQUENCE
# ******************************************************************************************************************** #
page_sequence = [
    Decision
]
