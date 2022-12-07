import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import networkx as nx
# Consequents

def thuattoan(dsip,gdpip,urip):
    score = ctrl.Consequent(np.arange(0, 11), 'Score')

# Antecedents
    danso = ctrl.Antecedent(np.arange(0, 200), 'Dan So')
    gdp = ctrl.Antecedent(np.arange(0, 700000, 10000), 'GDP')
    ur = ctrl.Antecedent(np.arange(0, 30, 0.1), 'UR')

# print(danso, gdp, ur, score)

# CHIA DAN SO
    danso['LP'] = fuzz.trapmf(danso.universe, [0, 0, 10, 26])
    danso['MP'] = fuzz.trimf(danso.universe, [10, 26, 60])
    danso['HP'] = fuzz.trapmf(danso.universe, [26, 60, 200, 200])

# CHIA GDP
    gdp['Lgdp'] = fuzz.trapmf(gdp.universe, [0, 0, 40000, 290000])
    gdp['Mgdp'] = fuzz.trimf(gdp.universe, [40000, 290000, 600000])
    gdp['Hgdp'] = fuzz.trapmf(gdp.universe, [290000, 600000, 700000, 700000])

# CHIA UR
    ur['Lur'] = fuzz.trapmf(ur.universe, [0, 0, 1, 6])
    ur['Mur'] = fuzz.trimf(ur.universe, [1, 6, 20])
    ur['Hur'] = fuzz.trapmf(ur.universe, [6, 20, 40, 40])

# CHIA DIEM
    score['LS'] = fuzz.trapmf(score.universe, [0, 0, 1, 5])
    score['MS'] = fuzz.trimf(score.universe, [1, 5, 9])
    score['HS'] = fuzz.trapmf(score.universe, [5, 9, 10, 10])

# TAO RULE
# RULE1 - LS
    rule1 = ctrl.Rule(
        (danso['LP'] & ur['Hur'] & gdp['Lgdp']) |
        (danso['LP'] & ur['Hur'] & gdp['Mgdp']) |

        (danso['MP'] & ur['Hur'] & gdp['Lgdp']) |
    (danso['MP'] & ur['Hur'] & gdp['Mgdp']) |
    (danso['MP'] & ur['Mur'] & gdp['Lgdp']) |

    (danso['HP'] & ur['Lur'] & gdp['Lgdp']) |
    (danso['HP'] & ur['Mur'] & gdp['Lgdp']) |
    (danso['HP'] & ur['Mur'] & gdp['Mgdp']) |
    (danso['HP'] & ur['Hur'] & gdp['Lgdp']) |
    (danso['HP'] & ur['Hur'] & gdp['Mgdp']) |

    (danso['HP'] & ur['Hur'] & gdp['Hgdp'])

    , score['LS'])

# RULE2- MS
    rule2 = ctrl.Rule(
    (danso['LP'] & ur['Lur'] & gdp['Lgdp']) |
    (danso['LP'] & ur['Mur'] & gdp['Lgdp']) |
    (danso['LP'] & ur['Mur'] & gdp['Mgdp']) |
    (danso['LP'] & ur['Hur'] & gdp['Hgdp']) |

    (danso['MP'] & ur['Lur'] & gdp['Lgdp']) |
    (danso['MP'] & ur['Lur'] & gdp['Mgdp']) |
    (danso['MP'] & ur['Mur'] & gdp['Mgdp']) |
    (danso['MP'] & ur['Hur'] & gdp['Hgdp']) |

    (danso['HP'] & ur['Lur'] & gdp['Mgdp']) |
    (danso['HP'] & ur['Mur'] & gdp['Hgdp'])

    , score['MS'])

# RULE3-HS
    rule3 = ctrl.Rule(
    (danso['LP'] & ur['Lur'] & gdp['Mgdp']) |
    (danso['LP'] & ur['Lur'] & gdp['Hgdp']) |
    (danso['LP'] & ur['Mur'] & gdp['Hgdp']) |

    (danso['MP'] & ur['Lur'] & gdp['Hgdp']) |
    (danso['MP'] & ur['Mur'] & gdp['Hgdp']) |

    (danso['HP'] & ur['Lur'] & gdp['Hgdp'])

    , score['HS'])
    score_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    score_output = ctrl.ControlSystemSimulation(score_ctrl)

    score_output.input['Dan So'] = dsip
    score_output.input['GDP'] = gdpip
    score_output.input['UR'] = urip
    score_output.compute()
    return score_output.output['Score']