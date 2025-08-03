from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

# Kedro settings required to run your pipeline
env = "local"
pipeline_name = "__default__"
project_path = Path.cwd()
package_name = "example_ml"
conf_source = "" or Path.cwd() / "conf"

NAMESPACE = "airflow"
DOCKER_IMAGE = "harbor.internal.roxxas96.net/example-ml/kedro-pipeline"

# Using a DAG context manager, you don't have to specify the dag property of each task
with DAG(
    dag_id="example-ml",
    start_date=datetime(2023, 1, 1),
    max_active_runs=3,
    # https://airflow.apache.org/docs/stable/scheduler.html#dag-runs
    catchup=False,
    # Default settings applied to all tasks
    default_args=dict(
        owner="airflow",
        depends_on_past=False,
        email_on_failure=False,
        email_on_retry=False,
        retries=1,
        retry_delay=timedelta(minutes=5),
    ),
) as dag:
    tasks = {
        "dvc-pull": KubernetesPodOperator(
            task_id="dvc-pull",
            name="dvc-pull",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["dvc"],
            arguments=[
                "pull",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-create-confusion-matrix-personality-personalities-personality-dummy-confusion-matrix": KubernetesPodOperator(
            task_id="personality-create-confusion-matrix-personality-personalities-personality-dummy-confusion-matrix",
            name="personality-create-confusion-matrix-personality-personalities-personality-dummy-confusion-matrix",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.create_confusion_matrix([personality.personalities]) -&gt; [personality.dummy_confusion_matrix]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-preprocess-personalities-node": KubernetesPodOperator(
            task_id="personality-preprocess-personalities-node",
            name="personality-preprocess-personalities-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.preprocess_personalities_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-create-confusion-matrix-starter-companies-starter-dummy-confusion-matrix": KubernetesPodOperator(
            task_id="starter-create-confusion-matrix-starter-companies-starter-dummy-confusion-matrix",
            name="starter-create-confusion-matrix-starter-companies-starter-dummy-confusion-matrix",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.create_confusion_matrix([starter.companies]) -&gt; [starter.dummy_confusion_matrix]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-preprocess-companies-node": KubernetesPodOperator(
            task_id="starter-preprocess-companies-node",
            name="starter-preprocess-companies-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.preprocess_companies_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-preprocess-shuttles-node": KubernetesPodOperator(
            task_id="starter-preprocess-shuttles-node",
            name="starter-preprocess-shuttles-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.preprocess_shuttles_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp": KubernetesPodOperator(
            task_id="personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp",
            name="personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.compare_personality_count_exp([personality.preprocessed_personalities]) -&gt; [personality.personality_count_plot_exp]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go": KubernetesPodOperator(
            task_id="personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go",
            name="personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.compare_personality_count_go([personality.preprocessed_personalities]) -&gt; [personality.personality_count_plot_go]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-split-data-node": KubernetesPodOperator(
            task_id="personality-split-data-node",
            name="personality-split-data-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.split_data_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp": KubernetesPodOperator(
            task_id="starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp",
            name="starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.compare_passenger_capacity_exp([starter.preprocessed_shuttles]) -&gt; [starter.shuttle_passenger_capacity_plot_exp]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go": KubernetesPodOperator(
            task_id="starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go",
            name="starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.compare_passenger_capacity_go([starter.preprocessed_shuttles]) -&gt; [starter.shuttle_passenger_capacity_plot_go]",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-create-model-input-table-node": KubernetesPodOperator(
            task_id="starter-create-model-input-table-node",
            name="starter-create-model-input-table-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.create_model_input_table_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-train-model-node": KubernetesPodOperator(
            task_id="personality-train-model-node",
            name="personality-train-model-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.train_model_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-split-data-node": KubernetesPodOperator(
            task_id="starter-split-data-node",
            name="starter-split-data-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.split_data_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "personality-evaluate-model-node": KubernetesPodOperator(
            task_id="personality-evaluate-model-node",
            name="personality-evaluate-model-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=personality.evaluate_model_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-train-model-node": KubernetesPodOperator(
            task_id="starter-train-model-node",
            name="starter-train-model-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.train_model_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
        "starter-evaluate-model-node": KubernetesPodOperator(
            task_id="starter-evaluate-model-node",
            name="starter-evaluate-model-node",
            namespace=NAMESPACE,
            image=DOCKER_IMAGE,
            cmds=["kedro"],
            arguments=[
                "run",
                "--nodes=starter.evaluate_model_node",
            ],
            get_logs=True,
            is_delete_operator_pod=True,  # Cleanup after execution
            in_cluster=False,  # Set to True if Airflow runs inside the Kubernetes cluster
            do_xcom_push=False,
            image_pull_policy="Always",
        ),
    }
    tasks["dvc-pull"] >> tasks["personality-preprocess-personalities-node"]
    tasks["dvc-pull"] >> tasks["starter-preprocess-shuttles-node"]
    tasks["dvc-pull"] >> tasks["starter-preprocess-companies-node"]
    (
        tasks["personality-preprocess-personalities-node"]
        >> tasks[
            "personality-compare-personality-count-exp-personality-preprocessed-personalities-personality-personality-count-plot-exp"
        ]
    )
    (
        tasks["personality-preprocess-personalities-node"]
        >> tasks[
            "personality-compare-personality-count-go-personality-preprocessed-personalities-personality-personality-count-plot-go"
        ]
    )
    (
        tasks["personality-preprocess-personalities-node"]
        >> tasks["personality-split-data-node"]
    )
    (
        tasks["starter-preprocess-shuttles-node"]
        >> tasks[
            "starter-compare-passenger-capacity-exp-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-exp"
        ]
    )
    (
        tasks["starter-preprocess-shuttles-node"]
        >> tasks[
            "starter-compare-passenger-capacity-go-starter-preprocessed-shuttles-starter-shuttle-passenger-capacity-plot-go"
        ]
    )
    (
        tasks["starter-preprocess-companies-node"]
        >> tasks["starter-create-model-input-table-node"]
    )
    (
        tasks["starter-preprocess-shuttles-node"]
        >> tasks["starter-create-model-input-table-node"]
    )
    tasks["personality-split-data-node"] >> tasks["personality-train-model-node"]
    tasks["starter-create-model-input-table-node"] >> tasks["starter-split-data-node"]
    tasks["personality-train-model-node"] >> tasks["personality-evaluate-model-node"]
    tasks["personality-split-data-node"] >> tasks["personality-evaluate-model-node"]
    tasks["starter-split-data-node"] >> tasks["starter-train-model-node"]
    tasks["starter-train-model-node"] >> tasks["starter-evaluate-model-node"]
    tasks["starter-split-data-node"] >> tasks["starter-evaluate-model-node"]
