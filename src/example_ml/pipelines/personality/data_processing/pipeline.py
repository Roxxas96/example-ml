from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    preprocess_personalities,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_personalities,
                inputs="personalities",
                outputs="preprocessed_personalities",
                name="preprocess_personalities_node",
            ),
        ]
    )
