from pathlib import Path

import pandas as pd

DATA_FOLDER = Path(__file__).parent / "data"


def load_data():
    df = pd.read_csv(DATA_FOLDER / "eu_life_expectancy_raw.tsv", sep="\t")

    BIG_COLUMN = "unit,sex,age,geo\\time"
    NEW_COLS = ["unit", "sex", "age", "region"]

    df[NEW_COLS] = pd.DataFrame(df[BIG_COLUMN].apply(lambda x: x.split(",")).tolist())

    df = (
        df[df["region"] == "PT"]
        .drop(columns=[BIG_COLUMN])
        .melt(id_vars=NEW_COLS, var_name="year", value_name="value")
    )
    df["year"] = df["year"].apply(lambda x: int(x.rstrip()))

    return df


def clean_data(df: pd.DataFrame):

    def _safe_float_cast(x):
        for c in [" ", "e", "p", "b", ":"]:
            x = x.replace(c, "")

        if x == "":
            return pd.NA

        return float(x)

    df["value"] = df["value"].apply(_safe_float_cast).astype("Float64")
    df.dropna(subset=["value"], inplace=True)

    return df


def save_data(df: pd.DataFrame, path=DATA_FOLDER / "pt_life_expectancy.csv"):
    df.to_csv(path, index=False)
