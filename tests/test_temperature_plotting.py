import pytest
import pandas as pd
import os, sys

import temperature_plotting as tpl

@pytest.mark.skip(reason="Test is bad")
def test_compute_mean_bad():
    calc = tpl.compute_mean([1, 2, 3])
    assert calc == 5


def test_compute_mean():
    ### first test something expected
    calc = tpl.compute_mean(range(1,11))
    expected = 5.5
    assert calc==expected
    
    ## You can keep asserting, figure out edge-cases
    calc = tpl.compute_mean([10,-10])
    expected = 0
    assert calc==expected
    assert type(calc) == float
    
    ## Be clever about assertions, define what matters
    calc = tpl.compute_mean([0,10,0])
    expected = 3.333
    assert round(calc, 3) == expected
    
    ## check different input formats
    pandas_series = pd.Series([1,2,3])
    calc = tpl.compute_mean(pandas_series)
    assert calc == 2
    
    ## Error messages are also testable
    with pytest.raises(TypeError):
        tpl.compute_mean(["a", "b", "c"])


# integration test
def test_main():
    tpl.main()
    assert os.path.exists("plot_25.png")
