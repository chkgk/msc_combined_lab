from otree.api import *

c = cu

doc = ''


class C(BaseConstants):
    NAME_IN_URL = 'fernandes'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    F1111 = models.StringField(blank=True,
                               label='1. Können Sie in eigenen Worten beschreiben was ETFs sind? Wenn Sie es nicht wissen, '
                                     'lassen Sie das Antwortfeld einfach leer.')
    F1 = models.IntegerField(choices=[[1, 'mehr kaufen als heute.'],
                                      [2, 'genau dasselbe kaufen wie heute.'],
                                      [3, 'weniger kaufen als heute.'], [4, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='2. Nehmen Sie an, dass die Zinsen auf Ihr Sparkonto bei 1% pro Jahr und die Inflation bei 2% pro Jahr liegen. Nach einem Jahr könnten Sie mit dem Geld auf Ihrem Sparkonto:',
                             widget=widgets.RadioSelect)
    F2 = models.IntegerField(
        choices=[[1, 'Richtig'], [2, 'Falsch'], [3, 'Ich weiß es nicht / möchte es nicht beantworten.']],
        label='3. "Anleihen sind normalerweise riskanter als Aktien." Glauben Sie, dass diese Aussage richtig oder falsch ist?',
        widget=widgets.RadioSelect)
    F3 = models.IntegerField(choices=[[1, 'Sparkonto'], [2, 'Aktien'], [3, 'Anleihen'], [4, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='4. Welcher der nachstehend beschriebenen Vermögenswerte hat über einen langen Zeitraum (z. B. 10 oder 20 Jahre) normalerweise die höchste Rendite?',
                             widget=widgets.RadioSelect)
    F4 = models.IntegerField(choices=[[1, 'Sparkonto'], [2, 'Aktien'], [3, 'Anleihen'], [4, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='5. Welcher der nachstehend beschriebenen Vermögenswerte beschreibt normalerweise die größten Schwankungen im Laufe der Zeit?',
                             widget=widgets.RadioSelect)
    F5 = models.IntegerField(choices=[[1, 'steigt'], [2, 'fällt'], [3, 'bleibt gleich'], [4, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='6. Wenn ein Investor sein Geld auf verschiedene Vermögenswerte verteilt, dann ________ das Risiko auf hohe Verluste.',
                             widget=widgets.RadioSelect)
    F6 = models.IntegerField(choices=[[1, 'Richtig'], [2, 'Falsch'], [3, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='8. "Wenn Sie €1,000 in Aktien investieren ist es möglich, dass Sie weniger als €1,000 haben, wenn Sie die Aktie wieder verkaufen wollen." Glauben Sie, dass diese Aussage richtig oder falsch ist?',
                             widget=widgets.RadioSelect)
    F7 = models.IntegerField(choices=[[1, 'Richtig'], [2, 'Falsch'], [3, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='9. "Ein Aktienfonds vereint das Geld vieler Anleger um eine Vielzahl von Aktien zu kaufen." Glauben Sie, dass diese Aussage richtig oder falsch ist?',
                             widget=widgets.RadioSelect)
    F8 = models.IntegerField(choices=[[1, 'Richtig'], [2, 'Falsch'], [3, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                             label='10. "Eine Hypothek mit 15 Jahren Laufzeit erfordert normalerweise höhere monatliche Zinszahlungen als eine Hypothek mit 30 Jahren Laufzeit, aber die über die gesamte Laufzeit des Darlehens gezahlten Zinsen sind geringer." Glauben Sie, dass diese Aussage richtig oder falsch ist?',
                             widget=widgets.RadioSelect)
    F9 = models.IntegerField(
        choices=[[1, 'Mehr als €200.'], [2, 'Genau €200.'], [3, 'Weniger als €200'], [4, 'Ich weiß es nicht / möchte es nicht beantworten.']],
        label='11. Nehmen Sie an Sie haben €100 in einem Sparkonto. Die Zinsen liegen bei 20% pro Jahr und Sie schauen erst nach 5 Jahren wieder auf den Kontostand. Wie viel glauben Sie haben Sie nach 5 Jahren insgesamt auf dem Konto?',
        widget=widgets.RadioSelect)
    F10 = models.IntegerField(choices=[[1, 'Die Person besitzt einen Anteil am Unternehmen B.'], [2, 'Die Person leiht Unternehmen B Geld.'],
                                       [3, 'Die Person haftet für die Schulden von Unternehmen B.'], [4, 'Keine der oben angeführten Aussagen.'],
                                       [5, 'Ich weiß es nicht / möchte es nicht beantworten.']],
                              label='12. Welche der nachstehenden Aussagen trifft zu, wenn jemand eine Anleihe des Unternehmens B kauft?',
                              widget=widgets.RadioSelect)

    F55 = models.StringField(
        choices=[[1, 'A'], [2, 'B'], [3, 'C'], [4, 'Ich weiß es nicht.'], [5, 'Ich möchte das nicht beantworten.']],
        label='6. Bitte wählen Sie Antwort C.')
class InstructionQuestionnaire(Page):
    form_model = 'player'


class Fernandes1(Page):
    form_model = 'player'
    form_fields = ['F1111', 'F1', 'F2', 'F3', 'F4', 'F5']

class Fernandes2(Page):
    form_model = 'player'
    form_fields = ['F55', 'F6', 'F7', 'F8', 'F9', 'F10']


page_sequence = [InstructionQuestionnaire, Fernandes1, Fernandes2]
