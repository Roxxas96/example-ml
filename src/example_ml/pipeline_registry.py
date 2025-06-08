"""Project pipelines."""

from kedro.pipeline import Pipeline

from .pipelines.personality import (
    data_processing as pdp,
)
from .pipelines.personality import (
    data_science as pds,
)
from .pipelines.personality import (
    reporting as pr,
)
from .pipelines.starter import (
    data_processing as sdp,
)
from .pipelines.starter import (
    data_science as sds,
)
from .pipelines.starter import (
    reporting as sr,
)


def register_pipelines() -> dict[str, Pipeline]:
    personality = Pipeline(
        pdp.create_pipeline() + pds.create_pipeline() + pr.create_pipeline(),
        namespace="personality",
    )

    starter = Pipeline(
        sdp.create_pipeline() + sds.create_pipeline() + sr.create_pipeline(),
        namespace="starter",
    )

    return {
        "personality": personality,
        "starter": starter,
        "__default__": personality + starter,
    }
