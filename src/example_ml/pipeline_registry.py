"""Project pipelines."""

from kedro.pipeline import Pipeline

from .pipelines.personality import (
    data_processing as dp,
)
from .pipelines.personality import (
    data_science as ds,
)
from .pipelines.personality import (
    reporting as rp,
)


def register_pipelines() -> dict[str, Pipeline]:
    # Individual pipelines
    data_processing = dp.create_pipeline()
    data_science = ds.create_pipeline()
    reporting = rp.create_pipeline()

    personality = Pipeline(
        data_processing + data_science + reporting, namespace="personality"
    )

    return {
        "personality.data_processing": data_processing,
        "personality.data_science": data_science,
        "personality.reporting": reporting,
        "personality": personality,
        "__default__": personality,
    }
