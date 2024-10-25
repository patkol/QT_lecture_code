from typing import Dict

from constants import NM, EV, M_E, CM, EPSILON_0


device_properties_dict: Dict[str, Dict] = {
    # "free": A free electron in a vacuum.
    "free": {
        "boundaries": [0, 5 * NM],
        "V_internal": [0],
        "m_eff": [M_E],
        "doping": [0],
        "permittivity": [EPSILON_0],
    },
    "barrier": {
        "boundaries": [
            0 * NM,
            30 * NM,
            45 * NM,
            49 * NM,
            64 * NM,
            94 * NM,
        ],
        "V_internal": [
            0 * EV,
            0 * EV,
            0.3 * EV,
            0 * EV,
            0 * EV,
        ],
        "m_eff": [
            0.065 * M_E,
            0.065 * M_E,
            0.1 * M_E,
            0.065 * M_E,
            0.065 * M_E,
        ],
        "doping": [
            1e19 / CM**3,
            0,
            0,
            0,
            1e19 / CM**3,
        ],
        "permittivity": [
            12 * EPSILON_0,
            12 * EPSILON_0,
            6 * EPSILON_0,
            12 * EPSILON_0,
            12 * EPSILON_0,
        ],
    },
}
