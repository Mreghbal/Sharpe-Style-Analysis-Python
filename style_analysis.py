######################################################################################################

import pandas as pd
import numpy as np
import scipy.optimize as so

######################################################################################################

def style_analysis(dependent_variable, explanatory_variables):
    
    """
    
    Returns the optimal weights that minimizes the Tracking error:
    
    1- Find the weights that minimize the square of the difference between the observed series
       and the returns of a benchmark portfolio that holds the explanatory building blocks in
       those same weights. This is equivalent to minimizing the tracking error between the two
       return series.
    
    2- The coefficients of performing style analysis on the observed return of a manager can
       be interpreted as weights in a portfolio of building blocks that together, mimic that
       return series.
    
    3- Style analysis also contributes to the CAPM. It can be regarded as a constrained form
       of the factor model, and it has been applied to the analysis of the performance of
       active managers. Sharpe took what looked like a factor model without effectively
       using factors but some kind of explanatory variables.
    
    4- The "tracking_error" function returns the tracking error between the two return series.
    
    5- The "portfolio_tracking_error" function returns the tracking error between the
       reference returns and a portfolio of building block returns held with given weights.
    
    """
######################################################################################################

    def tracking_error(return_series_a, return_series_b):
        return np.sqrt(((return_series_a - return_series_b) ** 2).sum())
    
    def portfolio_tracking_error(weights, reference_returns, building_block_returns):
        return tracking_error(reference_returns, (weights * building_block_returns).sum(axis = 1))

    n = explanatory_variables.shape[1]
    init_guess = np.repeat(1/n, n)
    bounds = ((0.0, 1.0),) * n # an N-tuple of 2-tuples!
    # construct the constraints
    weights_sum_to_1 = {'type': 'eq',
                        'fun': lambda weights: np.sum(weights) - 1
    }
    solution = so.minimize(portfolio_tracking_error, init_guess,
                       args=(dependent_variable, explanatory_variables,), method='SLSQP',
                       options={'disp': False},
                       constraints=(weights_sum_to_1,),
                       bounds=bounds)
    weights = pd.Series(solution.x, index=explanatory_variables.columns)
    return weights