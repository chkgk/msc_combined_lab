from os import environ
import random

SESSION_CONFIGS = [
   dict(
        name='combined_experiment_regular',
        display_name="Combined Experiment Regular",
        app_sequence=['combined_intro',
                      # Experiment 1 Regular
                      'ZTSN',
                      # Bridge
                      'combined_bridge',
                      # experiment 2
                      'instructions',
                      'overconfidence_prime',
                      'overconfidence_measurement',
                      'banks_2_anleitung',
                      'banks_two_assets',
                      'banks_5_anleitung',
                      'banks_five_assets',
                      'Neuroticism',
                      'fernandes',
                      'Demographics'],
        num_demo_participants=2,
        timeseries_filepath='_static/ZTSN/timeseries_files/',
        session_name='test_session',
        timeseries_filename='["Testround.csv", "High.csv", "Low.csv"]',
        refresh_rate_ms='[1400, 1400, 1400]',
        initial_cash='[120, 120, 120]',
        initial_shares='[0, 0, 0]',
        trading_button_values='[1, 1, 1]',
        random_round_payoff=True,
        training_round=True,
        graph_buffer=1,
    ),
    dict(
        name='combined_experiment_gamified',
        display_name="Combined Experiment Gamified",
        app_sequence=['combined_intro',
                      # Experiment 1 Gamified
                      'ZTS',
                      # Bridge
                      'combined_bridge',
                      # experiment 2
                      'instructions',
                      'overconfidence_prime',
                      'overconfidence_measurement',
                      'banks_2_anleitung',
                      'banks_two_assets',
                      'banks_5_anleitung',
                      'banks_five_assets',
                      'Neuroticism',
                      'fernandes',
                      'Demographics'],
        num_demo_participants=2,
        timeseries_filepath='_static/ZTS/timeseries_files/',
        session_name='test_session',
        timeseries_filename='["Testround.csv", "High.csv", "Low.csv"]',
        refresh_rate_ms='[1400, 1400, 1400]',
        initial_cash='[120, 120, 120]',
        initial_shares='[0, 0, 0]',
        trading_button_values='[1, 1, 1]',
        random_round_payoff=True,
        training_round=True,
        graph_buffer=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=4.00, doc=""
)

PARTICIPANT_FIELDS = ['exp_to_pay', 'round_to_pay', 'exp1_pay_ecu', 'exp2_pay_ecu', 'exp2_task', 'banks5_round_to_pay', 'banks2_round_to_pay', "banks2_coinflip", "banks5_coinflip"]
SESSION_FIELDS = ['num_rounds']

ROOMS = [
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'ECU'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5892252521073'
