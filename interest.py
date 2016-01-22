"""
Module for computing with interest rates.
Symbols: A is present amount, A0 is initial amount,
n counts days, and p is the interest rate per year.
Given three of these parameters, the fourth can be
computed as follows:
    A  = present_amount(A0, p, n)
    A0 = initial_amount(A, p, n)
    n  = days(A0, A, p)
    p  = annual_rate(A0, A, n)
"""
import sys
_filename = sys.argv[0]
_usage = """
Usage: %s A=10 p=5 n=730
Program computes and print(s the 4th parameter'
(A, A0, p, or n)""" % _filename

from math import log as ln

def present_amount(A0, p, n):
    return A0*(1 + p/(360.0*100))**n

def initial_amount(A, p, n):
    return A*(1 + p/(360.0*100))**(-n)

def days(A0, A, p):
    return ln(A/A0)/ln(1 + p/(360.0*100))

def annual_rate(A0, A, n):
    return 360*100*((A/A0)**(1.0/n) - 1)

def test_all_functions():
    # Compatible values
    A = 2.2133983053266699; A0 = 2.0; p = 5; n = 730
    # Given three of these, compute the remaining one
    # and compare with the correct value (in parenthesis)
    A_computed  = present_amount(A0, p, n)
    A0_computed = initial_amount(A, p, n)
    n_computed  = days(A0, A, p)
    p_computed  = annual_rate(A0, A, n)

    def float_eq(a, b, tolerance=1E-14):
        """Return True if a == b within the tolerance."""
        return abs(a - b) < tolerance

    success = float_eq(A_computed,  A)  and \
              float_eq(A0_computed, A0) and \
              float_eq(p_computed,  p)  and \
              float_eq(n_computed,  n)
    msg = """Computations failed (correct answers in parenthesis):
A=%g (%g)
A0=%g (%.1f)
n=%d (%d)
p=%g (%.1f)""" % (A_computed, A, A0_computed, A0,
                  n_computed, n, p_computed, p)
    assert success, msg

def compute_missing_parameter(init_code):
    try:
        exec(init_code)
    except SyntaxError as e:
        print( e )
        print( init_code )
        sys.exit(1)
    # Find missing parameter
    try:
        if 'A=' not in init_code:
            print( 'A =', present_amount(A0, p, n) )
        elif 'A0=' not in init_code:
            print( 'A0 =', initial_amount(A, p, n) )
        elif 'n=' not in init_code:
            print( 'n =', days(A0, A , p) )
        elif 'p=' not in init_code:
            print( 'p =', annual_rate(A0, A, n) )
    except NameError as e:
        print( e )
        sys.exit(1)
    except ValueError:
        print( 'Illegal values in input:', init_code )
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print( _usage )
    elif len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_all_functions()
    else:
        init_code = ''
        for statement in sys.argv[1:]:
            init_code += statement + '\n'
        # more elegant code:
        #init_code = '; '.join(sys.argv[1:])
        compute_missing_parameter(init_code)


__all__ = ['annual_rate', 'days', 'initial_amount', 'present_amount']

#==============================================================================
# del sys, ln, compute_missing_parameter, test_all_functions
#==============================================================================
