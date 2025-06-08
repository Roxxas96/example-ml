import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px  # noqa:  F401
import plotly.graph_objs as go
import seaborn as sn


# This function uses plotly.express
def compare_personality_count_exp(preprocessed_personalities: pd.DataFrame):
    return (
        preprocessed_personalities.groupby(["Personality"])
        .mean(numeric_only=True)
        .reset_index()
    )


# This function uses plotly.graph_objects
def compare_personality_count_go(preprocessed_personalities: pd.DataFrame):
    data_frame = (
        preprocessed_personalities.groupby(["Personality"])
        .mean(numeric_only=True)
        .reset_index()
    )
    fig = go.Figure(
        [
            go.Bar(
                x=data_frame["Personality"],
                y=data_frame["Count"],
            )
        ]
    )

    return fig


def create_confusion_matrix(personalities: pd.DataFrame):
    actuals = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
    data = {"y_Actual": actuals, "y_Predicted": predicted}
    df = pd.DataFrame(data, columns=["y_Actual", "y_Predicted"])
    confusion_matrix = pd.crosstab(
        df["y_Actual"], df["y_Predicted"], rownames=["Actual"], colnames=["Predicted"]
    )
    sn.heatmap(confusion_matrix, annot=True)
    return plt
