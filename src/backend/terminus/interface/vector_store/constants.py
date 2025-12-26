from terminus.interface.vector_store.custom import MilvusWithPermissionCheck, ElasticsearchWithPermissionCheck

CUSTOM_VECTORSTORE = {
    'MilvusWithPermissionCheck': MilvusWithPermissionCheck,
    'ElasticsearchWithPermissionCheck': ElasticsearchWithPermissionCheck
}
