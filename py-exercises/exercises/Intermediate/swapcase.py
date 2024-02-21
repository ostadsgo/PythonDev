"""
Information
-----------
@Copyright by Saeed Gholami 
Email: saeed.ghollami@gmail.com
Github: ostadsgo
Web: ostadsgo.github.io
Last edit: 2023-02-04


Level
-----
* Beginners
intermediate
Advanced


Description
-----------
Swape case string.

Examples
-------
>>> swapecase("Hello World!") 
hELLO wORLD!

Requirements
------------
 - Strings

Resources
---------
 - https://www.w3schools.com/python/python_strings.asp
"""


def swapecase(s):
    pass


# -----------------------------------
#    Do not touch this section
# -----------------------------------
if __name__ == "__main__":
    from tests import assert_equals

    assert_equals(swapecase, ("This",), "tHIS")
    assert_equals(swapecase, ("THIs",), "thiS")
    assert_equals(swapecase, ("123abc",), "123ABC")
    assert_equals(swapecase, ("t",), "T")
    assert_equals(swapecase, ("T",), "t")
    assert_equals(swapecase, ("",), "")
    assert_equals(swapecase, (" ",), " ")
    assert_equals(swapecase, ("tHis Is",), "ThIS iS")
