from terminus.workflow.common.node import NodeType
from terminus.workflow.nodes.agent.agent import AgentNode
from terminus.workflow.nodes.code.code import CodeNode
from terminus.workflow.nodes.condition.condition import ConditionNode
from terminus.workflow.nodes.end.end import EndNode
from terminus.workflow.nodes.input.input import InputNode
from terminus.workflow.nodes.knowledge_retriever.knowledge_retriever import KnowledgeRetriever
from terminus.workflow.nodes.llm.llm import LLMNode
from terminus.workflow.nodes.output.output import OutputNode
from terminus.workflow.nodes.qa_retriever.qa_retriever import QARetrieverNode
from terminus.workflow.nodes.rag.rag import RagNode
from terminus.workflow.nodes.report.report import ReportNode
from terminus.workflow.nodes.start.start import StartNode
from terminus.workflow.nodes.tool.tool import ToolNode

NODE_CLASS_MAP = {
    NodeType.START.value: StartNode,
    NodeType.END.value: EndNode,
    NodeType.INPUT.value: InputNode,
    NodeType.OUTPUT.value: OutputNode,
    NodeType.TOOL.value: ToolNode,
    NodeType.RAG.value: RagNode,
    NodeType.REPORT.value: ReportNode,
    NodeType.QA_RETRIEVER.value: QARetrieverNode,
    NodeType.CONDITION.value: ConditionNode,
    NodeType.AGENT.value: AgentNode,
    NodeType.CODE.value: CodeNode,
    NodeType.LLM.value: LLMNode,
    NodeType.KNOWLEDGE_RETRIEVER.value: KnowledgeRetriever,
}


class NodeFactory:
    @classmethod
    def get_node_class(cls, node_type: str) -> 'BaseNode':
        return NODE_CLASS_MAP.get(node_type)

    @classmethod
    def instance_node(cls, node_type: str, **kwargs) -> 'BaseNode':
        node_class = cls.get_node_class(node_type)
        if node_class is None:
            raise Exception(f'未知的节点类型：{node_type}')
        return node_class(**kwargs)
