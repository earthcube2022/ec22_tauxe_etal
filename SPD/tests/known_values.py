#! /usr/bin/env python

import numpy

initial_values = { "s": '0238x6011044',
           "datablock": None , # ignoring for now because it's so fucking long
           "x_Arai": numpy.array([ 0.,  0.03917767,  0.06612789,  0.1218238 ,  0.18767432, 0.21711849,  0.32091412,  0.48291503,  0.72423703,  1.03139876, 1.27786578,  1.62771574,  1.96549027,  2.50849607,  3.22408793, 3.99894094,  4.38250182]),
           "y_Arai": numpy.array([ 1.,  1.01807229,  1.,  0.98795181,  0.95783133, 0.96987952,  0.98192771,  0.93373494,  0.90361446,  0.81325301, 0.81927711,  0.70481928,  0.70481928,  0.50542169,  0.42168675, 0.13012048,  0.08253012]) ,
           "t_Arai": [273, 373.0, 423.0, 473.0, 498.0, 523.0, 548.0, 573.0, 598.0, 623.0, 648.0, 673.0, 698.0, 723.0, 748.0, 773.0, 798.0],
           "x_Arai_segment": numpy.array([ 0.1218238 ,  0.18767432,  0.21711849,  0.32091412,  0.48291503, 0.72423703,  1.03139876]),
           "y_Arai_segment": numpy.array([ 0.98795181,  0.95783133,  0.96987952,  0.98192771,  0.93373494, 0.90361446,  0.81325301]) ,
           "x_Arai_mean": 0.44086879270917517,
           "y_Arai_mean": 0.93545611015490526,
           "x_tail_check": numpy.array([ 0.1218238 ,  0.21711849,  0.48291503,  1.03139876,  1.62771574, 2.50849607,  3.99894094]),
           "y_tail_check": numpy.array([ 0.98795181,  0.98192771,  0.93373494,  0.84337349,  0.76506024, 0.58313253,  0.17349398]),
           "tail_checks_temperatures": numpy.array([ 473.,  523.,  573.,  623.,  673.,  723.,  773.]) ,
           "tail_checks_starting_temperatures": numpy.array([ 473.,  523.,  573.,  623.,  673.,  723.,  773.]) ,
           "x_ptrm_check": numpy.array([ 0.03622917,  0.10279838,  0.2177615 ,  0.49466588,  0.97717872, 1.56873716,  2.43269559]),
           "y_ptrm_check": [1.0180722891566265, 0.9879518072289156, 0.9698795180722891, 0.9337349397590361, 0.8132530120481928, 0.7048192771084337, 0.505421686746988],  # actually does NOT appear to be a numpy array.  weird.  maybe it should be, though......?
           "ptrm_checks_temperatures": numpy.array([ 373.,  473.,  523.,  573.,  623.,  673.,  723.]),
           "ptrm_checks_starting_temperatures": numpy.array([ 473.,  523.,  573.,  623.,  673.,  723.,  773.]),
           "zijdblock": [[273.0, 277.5, 79.6, 1.66e-09, 1, 'g', ''], [373.0, 277.3, 81.5, 1.69e-09, 0, 'g', ''], [423.0, 254.2, 85.6, 1.66e-09, 0, 'g', ''], [473.0, 251.7, 86.7, 1.64e-09, 1, 'g', ''], [498.0, 243.3, 86.6, 1.59e-09, 0, 'g', ''], [523.0, 236.4, 87.8, 1.61e-09, 1, 'g', ''], [548.0, 208.9, 86.3, 1.63e-09, 0, 'g', ''], [573.0, 241.3, 87.4, 1.55e-09, 1, 'g', ''], [598.0, 221.4, 87.1, 1.5e-09, 0, 'g', ''], [623.0, 228.5, 86.9, 1.35e-09, 1, 'g', ''], [648.0, 219.1, 87.2, 1.36e-09, 0, 'g', ''], [673.0, 241.2, 86.5, 1.17e-09, 1, 'g', ''], [698.0, 241.1, 86.7, 1.17e-09, 0, 'g', ''], [723.0, 235.8, 86.2, 8.39e-10, 1, 'g', ''], [748.0, 254.9, 86.4, 7e-10, 0, 'g', ''], [773.0, 264.8, 79.7, 2.16e-10, 1, 'g', ''], [798.0, 287.1, 81.3, 1.37e-10, 0, 'g', ''], [823.0, 5.5, 67.0, 1.54e-11, 1, 'g', '']],
           "z_temperatures": [273.0, 373.0, 423.0, 473.0, 498.0, 523.0, 548.0, 573.0, 598.0, 623.0, 648.0, 673.0, 698.0, 723.0, 748.0, 773.0, 798.0, 823.0], # also not a numpy array
           "start": 3,
           "end": 9,
           "pars": {'specimen_int_n': 7, 'lab_dc_field': 4e-05},
           "specimen_Data": None,
           "tmin": 473.0,
           "tmax": 623.0,
           "tmin_K": 200.,
           "tmax_K": 350.
           }

#self.stuff = ["s", "datablock", "x_Arai", "y_Arai", "t_Arai", "x_Arai_segment", "y_Arai_segment", "x_tail_check", "y_tail_check", "tail_checks_temperatures", "tail_checks_starting_temperatures", "x_ptrm_check", "y_ptrm_check", "ptrm_checks_temperatures", "ptrm_checks_starting_temperatures", "zijdblock", "z_temperatures", "start", "end", "pars", "specimen_Data", "tmin", "tmax", "tmin_K", "tmax_K"] 
 
York_Regression_values = {
    'specimen_YT': 1.0168795878275072, 
    'delta_x_prime': 0.9277422683265637, 
    'B_anc': 7.3875474081300247, 
    'count_IZ': 9, 
    'count_ZI': 8, 
    'x_err': numpy.array([-0.31904499, -0.25319447, -0.22375031, -0.11995467,  0.04204624, 0.28336824,  0.59052997]), 
    'specimen_b_sigma': 0.02400030575533443, 
    'specimen_XT': 5.5059116735192921, 
    'specimen_g_lim': 0.8333333333333334, 
    'y_prime': numpy.array([ 0.99116596,  0.9700248 ,  0.97332989,  0.96976905,  0.93071279, 0.89336783,  0.81982246]), 
    'delta_y_prime': 0.17134349974471441, 
    'x_tag': numpy.array([ 0.15662996,  0.31971781,  0.25448267,  0.18924753,  0.4501881 , 0.61327596,  1.10253953]), 
    'B_lab': 40.,
    'specimen_b_beta': 0.12995006017245725, 
    'specimen_b': -0.1846886852032506, 
    'specimen_g': 0.70027479782853574, 
    'specimen_f': 0.16849930099470078, 
    'y_tag': numpy.array([ 0.99438011,  0.98221826,  0.97678026,  0.95761038,  0.92769065, 0.8831212 ,  0.82639191]), 
    'specimen_q': 0.90800892113263332, 
    'specimen_w': 0.40607393436576267, 
    'x_prime': numpy.array([ 0.13922688,  0.25369607,  0.23580058,  0.25508082,  0.46655157, 0.66875649,  1.06696915]), 
    'y_err': numpy.array([ 0.0524957 ,  0.02237522,  0.03442341,  0.0464716 , -0.00172117, -0.03184165, -0.1222031 ])
    }
