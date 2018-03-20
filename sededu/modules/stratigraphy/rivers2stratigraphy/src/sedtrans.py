# sediment transport function

import numpy as np


def taubfun(H, S, g, rho):
    # depth slope product
    return (rho * g * H * S)


def qsEH(D50, Cf, taub, conR, cong, conrhof):
    # engelund-hansen with traditional coeffs
    term1 = np.sqrt(conR * cong * D50) * D50
    term2 = 0.05 / Cf
    term3 = (taub / (conrhof * conR * cong * D50))**2.5
    qs = term1 * term2 * term3
    return qs
