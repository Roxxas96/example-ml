import logging
import typing as t

import mlflow
from kedro.framework.hooks import hook_impl

logger = logging.getLogger(__name__)


class ExtraMLflowHooks:
    @hook_impl
    def before_pipeline_run(self, run_params: dict[str, t.Any]):
        logger.info("Logging extra metadata to MLflow")
        mlflow.set_tags(
            {
                "pipeline": run_params["pipeline_name"] or "__default__",
                "custom_version": "0.1.0",
            }
        )
