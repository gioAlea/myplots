"lhcb" folder readme
=======================

This folder englobes MAD-X code, it's output and the python scripts that treats the output. It simulates LHC operation at injection and collision at IP8 (LHCb experiment). The final result of the simulations are different plots listed below.

MAD-X
-----

The MAD-X code generating the data for collision is found in __"lhcb/Collision/madx"__, and for injection in __"lhcb/Injection/madx"__ .

The code is commented explaining each block.

Python Plots
------------

* __coll_elements_IP8.py__ currently plots both beams on collision with 5 sigma enveloppes, neutral cones issued from collision with a 100 murad fan, and the elements chosen (see the __"elements"__ folder for that, this script reads from it). Will add the apertures soon.

* __coll_params_IP8.py__ currently plots x,y, beta functions and effective angle vs s(m). Be sure to see where your data starts (IP8 or IP1) and what the script thinks.

* __elements.py__ not working.