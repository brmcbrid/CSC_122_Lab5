# Tests for Lab5
# Falling Distance Calculator

import os.path
import sys
from Lab5 import main
from tud_tests import *

def test_Lab5():

    try:
        exists = os.path.exists("Lab5.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input([0,200,20])
    main()
    output = get_display_output()

    assert output == [
        "Falling Distance Calculator\n",
        "Enter the start time: ",
        "Enter the end time: ",
        "Enter the time interval: ",
        "\n   Seconds   Speed   Distance",
        "   -------   -----   --------",
        "      0          0          0",
        "     20        196       1960",
        "     40        392       7840",
        "     60        588      17640",
        "     80        784      31360",
        "    100        980      49000",
        "    120       1176      70560",
        "    140       1372      96040",
        "    160       1568     125440",
        "    180       1764     158760",
        "    200       1960     196000"
        ]

    # Test 2
    set_keyboard_input([10,100,15])
    main()
    output = get_display_output()

    assert output == [
        "Falling Distance Calculator\n",
        "Enter the start time: ",
        "Enter the end time: ",
        "Enter the time interval: ",
        "\n   Seconds   Speed   Distance",
        "   -------   -----   --------",
        "     10         98        490",
        "     25        245       3062",
        "     40        392       7840",
        "     55        539      14823",
        "     70        686      24010",
        "     85        833      35402",
        "    100        980      49000"
        ]