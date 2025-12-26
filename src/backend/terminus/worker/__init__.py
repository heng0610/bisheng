# register tasks
from terminus.worker.knowledge.file_worker import file_copy_celery, parse_knowledge_file_celery, \
    retry_knowledge_file_celery
from terminus.worker.knowledge.rebuild_knowledge_worker import rebuild_knowledge_celery
from terminus.worker.telemetry.mid_table import sync_mid_user_increment, sync_mid_knowledge_increment, \
    sync_mid_app_increment, sync_mid_user_interact_dtl
from terminus.worker.test.test import add
from terminus.worker.workflow.tasks import execute_workflow, continue_workflow, stop_workflow
