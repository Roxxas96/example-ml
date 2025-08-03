from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project


class KedroOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        package_name: str,
        pipeline_name: str,
        node_name: str | list[str],
        project_path: str | Path,
        env: str,
        conf_source: str,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.package_name = package_name
        self.pipeline_name = pipeline_name
        self.node_name = node_name
        self.project_path = project_path
        self.env = env
        self.conf_source = conf_source

    def execute(self, context):
        configure_project(self.package_name)
        with KedroSession.create(self.project_path, env=self.env, conf_source=self.conf_source) as session:
            if isinstance(self.node_name, str):
                self.node_name = [self.node_name]
            session.run(self.pipeline_name, node_names=self.node_name)

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "__default__"
project_path = Path.cwd()
package_name = "example_ml"
conf_source = "" or Path.cwd() / "conf"


# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    dag_id="example-ml",
    start_date=datetime(2023,1,1),
    max_active_runs=3,
    # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    schedule_interval="@once",
    catchup=False,
    # Default settings applied to all tasks
    default_args=dict(
        owner="airflow",
        depends_on_past=False,
        email_on_failure=False,
        email_on_retry=False,
        retries=1,
        retry_delay=timedelta(minutes=5)
    )
) as dag:
    tasks = {
        "personality-create-confusion-matrix-personality-personalities-personality-dummy-confusion-matrix": KedroOperator(
            task_id="personality-create-confusion-matrix-personality-personalities-personality-dummy-confusion-matrix",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.create_confusion_matrix([personality.personalities]) -&gt; [personality.dummy_confusion_matrix]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-preprocess-personalities-node": KedroOperator(
            task_id="personality-preprocess-personalities-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.preprocess_personalities_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-create-confusion-matrix-starter-companies-starter-dummy-confusion-matrix": KedroOperator(
            task_id="starter-create-confusion-matrix-starter-companies-starter-dummy-confusion-matrix",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.create_confusion_matrix([starter.companies]) -&gt; [starter.dummy_confusion_matrix]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-preprocess-companies-node": KedroOperator(
            task_id="starter-preprocess-companies-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.preprocess_companies_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-preprocess-shuttles-node": KedroOperator(
            task_id="starter-preprocess-shuttles-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.preprocess_shuttles_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp": KedroOperator(
            task_id="personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.compare_personality_count_exp([personality.preprocessed_personalities]) -&gt; [personality.personality_count_plot_exp]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go": KedroOperator(
            task_id="personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.compare_personality_count_go([personality.preprocessed_personalities]) -&gt; [personality.personality_count_plot_go]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-split-data-node": KedroOperator(
            task_id="personality-split-data-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.split_data_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp": KedroOperator(
            task_id="starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.compare_passenger_capacity_exp([starter.preprocessed_shuttles]) -&gt; [starter.shuttle_passenger_capacity_plot_exp]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go": KedroOperator(
            task_id="starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.compare_passenger_capacity_go([starter.preprocessed_shuttles]) -&gt; [starter.shuttle_passenger_capacity_plot_go]",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-create-model-input-table-node": KedroOperator(
            task_id="starter-create-model-input-table-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.create_model_input_table_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-train-model-node": KedroOperator(
            task_id="personality-train-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.train_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-split-data-node": KedroOperator(
            task_id="starter-split-data-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.split_data_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "personality-evaluate-model-node": KedroOperator(
            task_id="personality-evaluate-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="personality.evaluate_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-train-model-node": KedroOperator(
            task_id="starter-train-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.train_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        ),
        "starter-evaluate-model-node": KedroOperator(
            task_id="starter-evaluate-model-node",
            package_name=package_name,
            pipeline_name=pipeline_name,
            node_name="starter.evaluate_model_node",
            project_path=project_path,
            env=env,
            conf_source=conf_source,
        )
    }
    tasks["personality-preprocess-personalities-node"] >> tasks["personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp"]
    tasks["personality-preprocess-personalities-node"] >> tasks["personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go"]
    tasks["personality-preprocess-personalities-node"] >> tasks["personality-split-data-node"]
    tasks["starter-preprocess-shuttles-node"] >> tasks["starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp"]
    tasks["starter-preprocess-shuttles-node"] >> tasks["starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go"]
    tasks["starter-preprocess-companies-node"] >> tasks["starter-create-model-input-table-node"]
    tasks["starter-preprocess-shuttles-node"] >> tasks["starter-create-model-input-table-node"]
    tasks["personality-split-data-node"] >> tasks["personality-train-model-node"]
    tasks["starter-create-model-input-table-node"] >> tasks["starter-split-data-node"]
    tasks["personality-train-model-node"] >> tasks["personality-evaluate-model-node"]
    tasks["personality-split-data-node"] >> tasks["personality-evaluate-model-node"]
    tasks["starter-split-data-node"] >> tasks["starter-train-model-node"]
    tasks["starter-train-model-node"] >> tasks["starter-evaluate-model-node"]
    tasks["starter-split-data-node"] >> tasks["starter-evaluate-model-node"]