import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    return x == "Yes"


def preprocess_personalities(personalities: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data for personalities.

    Args:
        personalities: Raw data.
    Returns:
        Preprocessed data, without NA, without duplicates, with `Personality` converted to a float, with `Stage_fear` converted to a boolean and `Drained_after_socializing` converted to a boolean.
    """
    personalities["Stage_fear"] = _is_true(personalities["Stage_fear"])
    personalities["Drained_after_socializing"] = _is_true(
        personalities["Drained_after_socializing"]
    )
    # Convert Personality column with values "Extrovert" or "Introvert" to a fload 0 or 1 respectively.
    personalities["Personality"] = personalities["Personality"].map(
        {"Extrovert": 0, "Introvert": 1}
    )
    personalities.drop_duplicates(inplace=True)
    personalities.dropna(inplace=True)

    return personalities
