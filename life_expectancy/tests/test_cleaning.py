"""Tests for the cleaning module"""

from pathlib import Path
from tempfile import NamedTemporaryFile

import pandas as pd

from life_expectancy.cleaning import clean_data, save_data


def test_clean_data(pt_life_expectancy_expected, raw_loaded_data):
    """Run the `clean_data` function and compare the output to the expected output"""
    df = clean_data(raw_loaded_data)
    with NamedTemporaryFile() as tmpf:
        p = Path(tmpf.name)

        save_data(df, path=p)
        pt_life_expectancy_actual = pd.read_csv(p)
        pd.testing.assert_frame_equal(
            pt_life_expectancy_actual, pt_life_expectancy_expected
        )
