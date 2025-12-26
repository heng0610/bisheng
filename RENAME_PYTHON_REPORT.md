# Bisheng → Terminus 重命名报告

生成时间: 2025-12-26 18:21:50
模式: 实际执行

============================================================

## 统计摘要
- 扫描文件数: 459
- 修改文件数: 459
- 错误文件数: 0

============================================================

## 修改详情

### src\backend\bisheng\main.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\run_celery.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\run_celery_beat.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\router.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\api\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng\api\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\api\services\assistant.py
状态: modified
  - `from bisheng\b` → `from terminus` (27 处)

### src\backend\bisheng\api\services\assistant_agent.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (4 处)

### src\backend\bisheng\api\services\audit_log.py
状态: modified
  - `from bisheng\b` → `from terminus` (20 处)

### src\backend\bisheng\api\services\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\services\chat_imp.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\services\component.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\api\services\dataset_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\api\services\etl4lm_loader.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\api\services\evaluation.py
状态: modified
  - `from bisheng\b` → `from terminus` (20 处)

### src\backend\bisheng\api\services\flow.py
状态: modified
  - `from bisheng\b` → `from terminus` (24 处)

### src\backend\bisheng\api\services\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (34 处)

### src\backend\bisheng\api\services\knowledge_imp.py
状态: modified
  - `from bisheng\b` → `from terminus` (28 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng\api\services\md_from_pptx.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\api\services\patch_130.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\api\services\role_group_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (19 处)

### src\backend\bisheng\api\services\tag.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\api\services\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\api\services\workflow.py
状态: modified
  - `from bisheng\b` → `from terminus` (25 处)

### src\backend\bisheng\api\services\invite_code\invite_code.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\api\services\linsight\message_stream_handle.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\api\services\linsight\sop_manage.py
状态: modified
  - `from bisheng\b` → `from terminus` (18 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (3 处)

### src\backend\bisheng\api\services\linsight\workbench_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (32 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\api\services\workstation\workstation.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)

### src\backend\bisheng\api\v1\assistant.py
状态: modified
  - `from bisheng\b` → `from terminus` (12 处)

### src\backend\bisheng\api\v1\audit.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\v1\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\api\v1\callback.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\v1\chat.py
状态: modified
  - `from bisheng\b` → `from terminus` (35 处)

### src\backend\bisheng\api\v1\component.py
状态: modified
  - `from bisheng\b` → `from terminus` (11 处)

### src\backend\bisheng\api\v1\dataset.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\api\v1\endpoints.py
状态: modified
  - `from bisheng\b` → `from terminus` (26 处)

### src\backend\bisheng\api\v1\evaluation.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\api\v1\flows.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)

### src\backend\bisheng\api\v1\invite_code.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\api\v1\linsight.py
状态: modified
  - `from bisheng\b` → `from terminus` (33 处)

### src\backend\bisheng\api\v1\mark_task.py
状态: modified
  - `from bisheng\b` → `from terminus` (11 处)

### src\backend\bisheng\api\v1\report.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\api\v1\schemas.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\api\v1\skillcenter.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\api\v1\tag.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\api\v1\usergroup.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\api\v1\validate.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\api\v1\variable.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\api\v1\workflow.py
状态: modified
  - `from bisheng\b` → `from terminus` (20 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\api\v1\workstation.py
状态: modified
  - `from bisheng\b` → `from terminus` (30 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng\api\v1\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (20 处)

### src\backend\bisheng\api\v1\schema\chat_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\api\v1\schema\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\api\v1\schema\linsight_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\chat\client.py
状态: modified
  - `from bisheng\b` → `from terminus` (19 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\chat\handlers.py
状态: modified
  - `from bisheng\b` → `from terminus` (18 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\chat\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (30 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng\chat\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\chat\clients\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\chat\clients\workflow_client.py
状态: modified
  - `from bisheng\b` → `from terminus` (13 处)

### src\backend\bisheng\chat_session\api\router.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\chat_session\domain\chat.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\common\init_data.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)

### src\backend\bisheng\common\constants\vectorstore_metadata.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\dependencies\core_deps.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\common\dependencies\user_deps.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\errcode\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\errcode\dataset.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\errcode\linsight.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\errcode\tool.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\models\config.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\common\repositories\implementations\base_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\repositories\implementations\config_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\common\repositories\interfaces\config_repository.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\common\schemas\telemetry\base_telemetry_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\common\schemas\telemetry\event_data_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\services\config_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\common\services\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\services\telemetry\telemetry_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\common\utils\markdown_cmpnt\md_to_pdf.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\utils\markdown_cmpnt\md_to_docx\markdocx.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\common\utils\markdown_cmpnt\md_to_docx\parser\md_parser.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\common\utils\markdown_cmpnt\md_to_docx\provider\docx_processor.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\common\utils\markdown_cmpnt\md_to_docx\provider\style_manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\components\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\components\custom_components\CustomComponent.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\core\logger.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\ai\rerank\rrf_rerank.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\ai\test\test.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\cache\flow.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\cache\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\cache\redis_manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\core\cache\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `'bisheng` → `'terminus'` (7 处)

### src\backend\bisheng\core\cache\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\core\config\settings.py
状态: modified
  - `"bisheng` → `"terminus` (3 处)
  - `'bisheng` → `'terminus'` (6 处)

### src\backend\bisheng\core\context\examples.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\core\context\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\core\context\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\core\database\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\core\database\alembic\env.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\core\external\http_client\http_client_manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\core\prompts\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\core\search\elasticsearch\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\core\storage\minio\minio_manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\core\storage\minio\minio_storage.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\core\vectorstore\ensemble_retriever.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\custom\customs.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\database\models\assistant.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\database\models\audit_log.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\component.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\dataset.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\evaluation.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\flow.py
状态: modified
  - `from bisheng\b` → `from terminus` (12 处)

### src\backend\bisheng\database\models\flow_version.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\group.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\group_resource.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\invite_code.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\linsight_execute_task.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\linsight_session_version.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\linsight_sop.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\database\models\mark_app_user.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\mark_record.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\mark_task.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\message.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\recall_chunk.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\database\models\report.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\database\models\role.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\database\models\role_access.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\session.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\tag.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\template.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\database\models\user_group.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\database\models\user_link.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\variable_value.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\database\models\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\field_typing\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\finetune\schemas.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\finetune\api\finetune.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\finetune\api\server.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\finetune\domain\sft_backend.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\finetune\domain\models\finetune.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\finetune\domain\models\model_deploy.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\finetune\domain\models\preset_train.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\finetune\domain\models\server.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\finetune\domain\models\sft_model.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\finetune\domain\services\finetune.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\finetune\domain\services\finetune_file.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\graph\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\graph\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\graph\edge\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\graph\graph\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\graph\graph\constants.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)

### src\backend\bisheng\graph\vertex\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\graph\vertex\types.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\interface\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\interface\custom_lists.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (3 处)
  - `'bisheng` → `'terminus'` (3 处)

### src\backend\bisheng\interface\listing.py
状态: modified
  - `from bisheng\b` → `from terminus` (19 处)

### src\backend\bisheng\interface\run.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\types.py
状态: modified
  - `from bisheng\b` → `from terminus` (19 处)

### src\backend\bisheng\interface\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\agents\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\interface\agents\custom.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\agents\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\autogenRole\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\interface\chains\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (3 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng\interface\chains\custom.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\interface\chains\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\custom\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\interface\custom\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\interface\custom\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\custom\code_parser\code_parser.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\custom\custom_component\component.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\custom\custom_component\custom_component.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\interface\custom\directory_reader\directory_reader.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\custom\directory_reader\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\document_loaders\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\interface\embeddings\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\interface\embeddings\custom.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\importing\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (17 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)
  - `'bisheng` → `'terminus'` (6 处)

### src\backend\bisheng\interface\importing\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\initialize\loading.py
状态: modified
  - `from bisheng\b` → `from terminus` (22 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng\interface\initialize\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\initialize\vector_store.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\interface\inputoutput\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\interface\llms\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\interface\llms\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\memories\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\interface\memories\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\output_parsers\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\interface\prompts\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\interface\prompts\custom.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\prompts\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\retrievers\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\interface\text_splitters\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\interface\text_splitters\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\toolkits\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\interface\tools\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\interface\tools\constants.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\tools\custom.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\interface\tools\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\utilities\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\interface\vector_store\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\interface\vector_store\constants.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\interface\vector_store\custom.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng\interface\wrappers\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\knowledge\api\dependencies.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\knowledge\api\endpoints\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (28 处)
  - `'bisheng` → `'terminus'` (4 处)

### src\backend\bisheng\knowledge\api\endpoints\qa.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\knowledge\domain\knowledge_rag.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\knowledge\domain\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\knowledge\domain\models\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\knowledge\domain\models\knowledge_file.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\knowledge\domain\repositories\implementations\knowledge_file_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\knowledge\domain\repositories\implementations\knowledge_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\knowledge\domain\repositories\interfaces\knowledge_file_repository.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\knowledge\domain\repositories\interfaces\knowledge_repository.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\knowledge\domain\schemas\knowledge_file_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\knowledge\domain\schemas\knowledge_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\knowledge\domain\services\knowledge_file_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (13 处)

### src\backend\bisheng\knowledge\domain\services\knowledge_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (11 处)

### src\backend\bisheng\knowledge\rag\elasticsearch_factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\knowledge\rag\milvus_factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\linsight\state_message_manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\linsight\task_exec.py
状态: modified
  - `from bisheng\b` → `from terminus` (15 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (3 处)
  - `"bisheng` → `"terminus` (1 处)

### src\backend\bisheng\linsight\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\linsight\worker.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\llm\api\router.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\llm\domain\const.py
状态: modified
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\llm\domain\schemas.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\llm\domain\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\llm\domain\llm\asr.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\llm\domain\llm\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\llm\domain\llm\embedding.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\llm\domain\llm\llm.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\llm\domain\llm\rerank.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\llm\domain\llm\tts.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\llm\domain\models\llm_server.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\llm\domain\services\llm.py
状态: modified
  - `from bisheng\b` → `from terminus` (17 处)

### src\backend\bisheng\mcp_manage\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\mcp_manage\clients\sse.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\mcp_manage\clients\stdio.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\mcp_manage\clients\streamable.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\mcp_manage\langchain\tool.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\open_endpoints\api\dependencies.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\open_endpoints\api\router.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\open_endpoints\api\endpoints\assistant.py
状态: modified
  - `from bisheng\b` → `from terminus` (14 处)

### src\backend\bisheng\open_endpoints\api\endpoints\chat.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\open_endpoints\api\endpoints\filelib.py
状态: modified
  - `from bisheng\b` → `from terminus` (17 处)
  - `'bisheng` → `'terminus'` (3 处)

### src\backend\bisheng\open_endpoints\api\endpoints\flow.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\open_endpoints\api\endpoints\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\open_endpoints\api\endpoints\llm.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\open_endpoints\api\endpoints\workflow.py
状态: modified
  - `from bisheng\b` → `from terminus` (15 处)

### src\backend\bisheng\open_endpoints\domain\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\pptx2md\entry.py
状态: modified
  - `import bisheng\b` → `import terminus` (1 处)
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\pptx2md\multi_column.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\pptx2md\outputter.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\pptx2md\parser.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\pptx2md\__main__.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\processing\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\processing\process.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\script\convert_sys_embeddings.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\script\knowledge_data_convert.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\script\knowledge_data_fix.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\script\sync_increment_table.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\services\deps.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\services\manager.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\services\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (19 处)

### src\backend\bisheng\services\auth\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\auth\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\auth\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\services\cache\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\services\cache\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\cache\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\cache\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `'bisheng` → `'terminus'` (3 处)

### src\backend\bisheng\services\chat\cache.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\services\chat\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\chat\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\services\chat\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\credentials\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\credentials\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\services\plugins\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\plugins\langfuse_plugin.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\services\plugins\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\services\session\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\session\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\services\session\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\settings\auth.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\services\settings\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\settings\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\store\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\services\store\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\services\store\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\task\factory.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\services\task\service.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\services\task\backends\anyio.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\services\task\backends\celery.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\share_link\api\dependencies.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\share_link\api\endpoints\share_link.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\share_link\api\schemas\share_link_schema.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\share_link\domain\models\share_link.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\share_link\domain\repositories\implementations\share_link_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\share_link\domain\repositories\interfaces\share_link_repository.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\share_link\domain\services\share_link_service.py
状态: modified
  - `from bisheng\b` → `from terminus` (6 处)

### src\backend\bisheng\telemetry\domain\mid_table\app_increment.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\telemetry\domain\mid_table\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\telemetry\domain\mid_table\knowledge_increment.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\telemetry\domain\mid_table\user_interact.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\field\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\template\frontend_node\agents.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\template\frontend_node\autogenrole.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\template\frontend_node\chains.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\template\frontend_node\custom_components.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\template\frontend_node\documentloaders.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\embeddings.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\template\frontend_node\input_output.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\template\frontend_node\llms.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)
  - `"bisheng` → `"terminus` (1 处)

### src\backend\bisheng\template\frontend_node\memories.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\template\frontend_node\output_parsers.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\prompts.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\template\frontend_node\retrievers.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\textsplitters.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\tools.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\template\frontend_node\utilities.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\vectorstores.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\wrappers.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\template\frontend_node\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\template\frontend_node\formatter\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\template\frontend_node\formatter\field_formatters.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\template\template\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\tool\api\tool.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\tool\domain\schemas.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\tool\domain\langchain\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\tool\domain\langchain\linsight_knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\tool\domain\models\gpts_tools.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\tool\domain\services\executor.py
状态: modified
  - `from bisheng\b` → `from terminus` (13 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\tool\domain\services\openapi.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\tool\domain\services\tool.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\user\api\user.py
状态: modified
  - `from bisheng\b` → `from terminus` (16 处)

### src\backend\bisheng\user\domain\models\user.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\user\domain\models\user_role.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\user\domain\repositories\implementations\user_repository_impl.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\user\domain\repositories\interfaces\user_repository.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\user\domain\services\auth.py
状态: modified
  - `from bisheng\b` → `from terminus` (7 处)

### src\backend\bisheng\user\domain\services\captcha.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\user\domain\services\user.py
状态: modified
  - `from bisheng\b` → `from terminus` (14 处)

### src\backend\bisheng\utils\constants.py
状态: modified
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng\utils\docx_temp.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\utils\http_middleware.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\utils\threadpool.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\utils\util.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\utils\validate.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng\worker\config.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\worker\main.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `'bisheng` → `'terminus'` (3 处)

### src\backend\bisheng\worker\__init__.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\worker\knowledge\file_worker.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\worker\knowledge\qa.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\worker\knowledge\rebuild_knowledge_worker.py
状态: modified
  - `from bisheng\b` → `from terminus` (9 处)

### src\backend\bisheng\worker\telemetry\mid_table.py
状态: modified
  - `from bisheng\b` → `from terminus` (14 处)

### src\backend\bisheng\worker\test\test.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\worker\workflow\redis_callback.py
状态: modified
  - `from bisheng\b` → `from terminus` (18 处)

### src\backend\bisheng\worker\workflow\tasks.py
状态: modified
  - `from bisheng\b` → `from terminus` (12 处)

### src\backend\bisheng\workflow\callback\base_callback.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\workflow\callback\llm_callback.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\workflow\common\knowledge.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\workflow\graph\graph_engine.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\workflow\graph\workflow.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)

### src\backend\bisheng\workflow\nodes\base.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\workflow\nodes\node_manage.py
状态: modified
  - `from bisheng\b` → `from terminus` (14 处)

### src\backend\bisheng\workflow\nodes\agent\agent.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng\workflow\nodes\code\code.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\workflow\nodes\condition\condition.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\workflow\nodes\condition\conidition_case.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\workflow\nodes\end\end.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\workflow\nodes\input\const.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\workflow\nodes\input\input.py
状态: modified
  - `from bisheng\b` → `from terminus` (10 处)

### src\backend\bisheng\workflow\nodes\knowledge_retriever\knowledge_retriever.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\bisheng\workflow\nodes\llm\llm.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng\workflow\nodes\output\output.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)

### src\backend\bisheng\workflow\nodes\output\output_fake.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)

### src\backend\bisheng\workflow\nodes\qa_retriever\qa_retriever.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng\workflow\nodes\rag\rag.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\workflow\nodes\report\report.py
状态: modified
  - `from bisheng\b` → `from terminus` (4 处)
  - `"bisheng` → `"terminus` (4 处)

### src\backend\bisheng\workflow\nodes\start\start.py
状态: modified
  - `from bisheng\b` → `from terminus` (8 处)

### src\backend\bisheng\workflow\nodes\tool\tool.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)

### src\backend\bisheng_langchain\agents\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\agents\chatglm_functions_agent\base.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\agents\llm_functions_agent\base.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\autogen_role\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (4 处)

### src\backend\bisheng_langchain\chains\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (9 处)

### src\backend\bisheng_langchain\chains\autogen\auto_gen.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chains\question_answering\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chat_models\host_llm.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chat_models\minimax.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chat_models\proxy_llm.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\chat_models\qwen.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\chat_models\sensetime.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chat_models\wenxin.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\chat_models\xunfeiai.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\document_loaders\custom_kv.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\document_loaders\elem_pdf.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\document_loaders\universal_kv.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\embeddings\wenxin.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\assistant.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng_langchain\gpts\auto_optimization.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\auto_tool_selected.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\load_tools.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (14 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng_langchain\gpts\utils.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (9 处)
  - `'bisheng` → `'terminus'` (7 处)

### src\backend\bisheng_langchain\gpts\agent_types\llm_functions_agent.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\agent_types\llm_react_agent.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\agent_types\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\gpts\prompts\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (6 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\base.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\firecrawl.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\jina.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\openapi.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\silicon_flow.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\tianyancha.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\api_tools\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (7 处)

### src\backend\bisheng_langchain\gpts\tools\code_interpreter\e2b_executor.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\code_interpreter\local_executor.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\code_interpreter\tool.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\bisheng_langchain\gpts\tools\dalle_image_generator\tool.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\local_file\local_file.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\message\dingding.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\message\email.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\message\feishu.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\message\wechat.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\gpts\tools\web_search\tool.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\input_output\output.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\linsight\agent.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)

### src\backend\bisheng_langchain\linsight\agent_test.py
状态: modified
  - `from bisheng\b` → `from terminus` (5 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (3 处)

### src\backend\bisheng_langchain\linsight\manage.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)

### src\backend\bisheng_langchain\linsight\react_task.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)

### src\backend\bisheng_langchain\linsight\task.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (4 处)

### src\backend\bisheng_langchain\rag\bisheng_rag_chain.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\bisheng_rag_pipeline.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)
  - `'bisheng` → `'terminus'` (4 处)

### src\backend\bisheng_langchain\rag\bisheng_rag_pipeline_v2.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (6 处)
  - `'bisheng` → `'terminus'` (5 处)

### src\backend\bisheng_langchain\rag\bisheng_rag_tool.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (5 处)
  - `'bisheng` → `'terminus'` (2 处)

### src\backend\bisheng_langchain\rag\extract_info.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\run_qa_gen_web.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\run_rag_evaluate_web.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\utils.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (9 处)
  - `'bisheng` → `'terminus'` (7 处)

### src\backend\bisheng_langchain\rag\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\rag\init_retrievers\mix_retriever.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\qa_corpus\qa_generator.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\rag\test\test_smaller_chunks.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\bisheng_langchain\retrievers\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\bisheng_langchain\sql\__init__.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)

### src\backend\test\milvus_trans.py
状态: modified
  - `from bisheng_langchain\b` → `from terminus_langchain` (2 处)

### src\backend\test\test.py
状态: modified
  - `from bisheng\b` → `from terminus` (3 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\test\test_api.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)

### src\backend\test\test_docx.py
状态: modified
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\test\test_es.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `from bisheng_langchain\b` → `from terminus_langchain` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\test\test_filelib.py
状态: modified
  - `from bisheng\b` → `from terminus` (1 处)
  - `'bisheng` → `'terminus'` (1 处)

### src\backend\test\test_gpts.py
状态: modified
  - `from bisheng\b` → `from terminus` (2 处)
  - `'bisheng` → `'terminus'` (1 处)
