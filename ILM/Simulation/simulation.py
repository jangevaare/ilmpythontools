# Main simulation file
# Justin Angevaare
# September 2014

import numpy as np
import pandas as pd

def init_infect(indvs, n):
    """Create `n` initial infections (i.e. at time 0) within your described population (e.g. individuals generated by `unif_indvs`)"""
    return np.random.choice(indvs.index, size=n, replace=False))

# Loop population update functions as desired

# Output histories in CSV file
