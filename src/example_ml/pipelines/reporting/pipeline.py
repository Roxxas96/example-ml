from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    compare_personality_count_exp,
    compare_personality_count_go,
    create_confusion_matrix,
)


def create_pipeline(**kwargs) -> Pipeline:
    """This is a simple pipeline which generates a pair of plots"""
    return pipeline(
        [
            node(
                func=compare_personality_count_exp,
                inputs="preprocessed_personalities",
                outputs="personality_count_plot_exp",
            ),
            # node(
            #     func=compare_personality_count_go,
            #     inputs="preprocessed_personalities",
            #     outputs="personality_count_plot_go",
            # ),
            node(
                func=create_confusion_matrix,
                inputs="personalities",
                outputs="dummy_confusion_matrix",
            ),
        ]
    )
