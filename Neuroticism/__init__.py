from otree.api import *
from otree.api import models
from otree.forms.widgets import RadioSelect

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Neuroticism'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Neur_1=models.IntegerField(
        label="Ich bin oft deprimiert, niedergeschlagen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_2 = models.IntegerField(
        label="Ich bin entspannt, lasse mich durch Stress nicht aus der Ruhe bringen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_3 = models.IntegerField(
        label="Ich reagiere leicht angespannt.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_4 = models.IntegerField(
        label="Ich mache mir oft Sorgen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_5 = models.IntegerField(
        label="Ich bin emotional ausgeglichen, nicht leicht aus der Fassung zu bringen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_6 = models.IntegerField(
        label="Ich kann launisch sein, habe schwankende Stimmungen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_7 = models.IntegerField(
        label="Ich bleibe ruhig, selbst in Stresssituationen.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

    Neur_8 = models.IntegerField(
        label="Ich werde leicht nervös und unsicher.",
        choices=[
            [1, 'Stimme überhaupt nicht zu'],
            [2, 'Stimme nicht zu'],
            [3, 'Neutral'],
            [4, 'Stimme zu'],
            [5, 'Stimme vollkommen zu'],
        ],
        widget=RadioSelect,
    )

# PAGES
class Neuroticism_instructions(Page):
    pass

class Neuroticism(Page):
    form_model = 'player'
    form_fields = ['Neur_1', 'Neur_2', 'Neur_3', 'Neur_4']

class Neuroticism1(Page):
    form_model = 'player'
    form_fields = ['Neur_5', 'Neur_6', 'Neur_7', 'Neur_8']


page_sequence = [Neuroticism_instructions, Neuroticism, Neuroticism1]
