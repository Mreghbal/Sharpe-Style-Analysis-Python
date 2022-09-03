# Sharpe-Style-Analysis-Python
Returns the optimal weights that minimizes the tracking error between the observed series and the returns of a benchmark portfolio

 """
    
    Returns the optimal weights that minimizes the tracking error:
    
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
