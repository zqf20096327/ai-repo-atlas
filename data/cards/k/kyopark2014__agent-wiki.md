# kyopark2014/agent-wiki

⭐ 15 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/kyopark2014/agent-wiki) · 个人维护

**把对话语料自动编译成知识图谱的 Web Agent 应用**

基于 FastAPI + React 的本地 Web Agent：LangGraph ReAct 循环执行聊天任务，支持 MCP 工具与 Skill（graphify、websearch、wiki、graph memory 等），响应 SSE 流式输出并写入 tasks.db。核心机制是两条独立图谱管线：从对话 DB 导出语料，经 LLM 语义抽取节点/边（含 EXTRACTED/INFERRED/AMBIGUOUS 置信度标签），Leiden/Louvain 聚类后生成 graph.json 并以三种 vis-network 模式（Force Atlas / Neo4j Explore / Holistic View）发布为 HTML，附文档检索面板；实现 Karpathy 提出的无向量 DB 的 LLM Wiki 思路，图谱查询走 graph.json 遍历而非嵌入索引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph ReAct Agent + MCP/Skill，SSE 流式响应
- 对话→语料→LLM 抽取→graph.json→HTML 的自动知识图谱管线
- 边带 EXTRACTED/INFERRED/AMBIGUOUS 置信度标签
- 三种图谱可视化模式与基于 graph.json 遍历的文档检索

## 适用场景

- 把积累的 Agent 对话沉淀为可浏览、可检索的知识图谱
- 用 Wiki Graph 组织本地文档并供 Agent 通过 recall_wiki 检索
- 在无向量 DB 的环境下以知识图谱方式查询本地语料

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: OpenAI 공동 창업자이자 Tesla 전 AI 리드인 **Andrej Karpathy**는 구조화된 Markdown을 이용해 로컬에서 LLM Wiki를 활용하여 데이터를 조회하는 방법을 제안하였습니다. RA
> L7: Web UI는 **FastAPI + React**이며, Agent는 **같은 프로세스**의 LangGraph로 실행합니다. 별도 AgentCore Runtime 없이 로컬에서 동작합니다.
> L302: |3. 시맨틱 추출|run_extract.py → semantic.py|**있음**|corpus chunk(기본 8파일)를 LLM에 넘겨 nodes/edges/hyperedges JSON 추출. LLM은 

## 星数曲线

```mermaid
xychart-beta
    title "kyopark2014/agent-wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e99bda9e28c9` · [字段定义](../../DATASET.md)*
