# PavelShaura/review_ducktective

⭐ 19 · Python · MIT · 推送 2026-09-21 · [GitHub](https://github.com/PavelShaura/review_ducktective) · 个人维护 · 中文 README

**自托管 LLM 代码评审平台：可离线运行，findings 附代码证据**

自托管的代码评审平台：输入 commit 或 revision 区间，输出按严重度分级、锚定到具体行号的结构化 findings，每条 finding 必须引用被评审版本中真实存在的代码片段，否则被 evidence gate 丢弃。内部机制包括 LangGraph agentic loop（13 个代码图工具）、tree-sitter AST 解析、符号/调用图、nomic-embed-text 本地嵌入 + pgvector 混合检索、LiteLLM 网关路由本地（Ollama/LM Studio/vLLM）或云端模型，标记 local_only 的仓库不产生任何外发请求。技术栈为 Python 3.12、FastAPI、PostgreSQL、Redis、Keycloak。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- evidence gate：finding 必须引用被评审版本中的真实代码，未通过即丢弃并计数
- tree-sitter 符号图 + 13 个工具的 agentic loop（find_callers/get_definition 等）
- pgvector 混合检索与按 git 内容哈希的增量索引
- LiteLLM 网关路由 Ollama/LM Studio/vLLM 及云端模型，local_only 仓库零外发请求
- 人工 verdict（confirmed/false trail/dismissed）反馈到后续评审

## 适用场景

- 对不能离开内网的代码库做离线 LLM 代码评审
- 评审结果需要逐条附代码证据以降低幻觉
- 通过 MCP server 让 Claude Code/Cursor 等外部 agent 复用代码导航索引

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L24: **review_ducktective** is a self-hosted code review platform. Give it a commit or a
> L31: It is built for codebases that cannot leave the building. Everything from parsing to
> L56:  versions · encrypted provider connections · local inference on Ollama / LM Studio

## 星数曲线

```mermaid
xychart-beta
    title "PavelShaura/review_ducktective 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ad5c8c2a65f4` · [字段定义](../../DATASET.md)*
