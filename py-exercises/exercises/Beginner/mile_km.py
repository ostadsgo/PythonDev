"""
Information
-----------
@Copyright by Saeed Gholami 
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io
Last edit: 2023-02-21


Level
-----
* Beginners
intermediate
Advanced


Description
-----------
Conver Mile to Kilometer
Return result rounded by 3 digits
If Mile were negative or zero return 0

Examples
-------
>>> mile_to_km(1)
1.609
>>> km_to_mile(0)
0.0
>>> km_to_mile(-1)
0.0


Requirements
------------
 - Arithmetic operators

Resources
---------
 - https://www.w3schools.com/python/python_numbers.asp
 - https://www.w3schools.com/python/python_operators.asp

"""


def mile_to_km(mile):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(mile_to_km, (1,), 1.609)
    assert_equals(mile_to_km, (5,), 8.045)
    assert_equals(mile_to_km, (0,), 0.0)
    assert_equals(mile_to_km, (-10,), 0.0)
