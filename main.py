import numpy as np

import func2

z = func2.create_complex_ndarray((-5, 5), (-5, 5), 500)
w: np.ndarray = ((z ** 2 - 1) * (z - 2 - 1j) ** 2) / (z ** 2 + 2 + 2j)
# w = np.sin(z)
func2.domain(z, w,'w')
