""" Fizzbuzz Api entry file
    Fizzbuzz Api is a Restful api that provides a list as described below :
    A list of all numbers from 1 to 100, just replacing all multiples of 3 by "fizz",
    all multiples of 5 by "buzz", and all multiples of 15 by "fizzbuzz". 

    Example of output: 
    "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz".

    The purpose of this Api is to customise every variable of this simple algorithm.
    Such as the range, multiples and those replacing words
"""

from FizzbuzzApi import app, logging
import atexit

def exitHandler():
    logging.info('exiting fizzbuzz api')
    
if __name__ == '__main__':
    """ Main function
        Called when lauching from console
    """
    atexit.register(exitHandler)
    app.run()