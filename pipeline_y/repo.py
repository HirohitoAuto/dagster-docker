from dagster import FilesystemIOManager, graph, op, repository, schedule
from dagster_docker import docker_executor


@op
def hello_y():
    return 1


@op
def goodbye_y(foo):
    if foo != 1:
        raise Exception("Bad io manager")
    return foo * 2


@graph
def my_graph():
    goodbye_y(hello_y())


my_job = my_graph.to_job(name="my_job")

my_step_isolated_job = my_graph.to_job(
    name="my_step_isolated_job",
    executor_def=docker_executor,
    resource_defs={
        "io_manager": FilesystemIOManager(base_dir="/tmp/io_manager_storage")
    },
)


@schedule(cron_schedule="* * * * *", job=my_job, execution_timezone="US/Central")
def my_schedule_y(_context):
    return {}


@repository
def deploy_docker_repository_y():
    return [my_job, my_step_isolated_job, my_schedule_y]
