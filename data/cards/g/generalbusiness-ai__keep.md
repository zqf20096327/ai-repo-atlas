# generalbusiness-ai/keep

⭐ 41 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/generalbusiness-ai/keep) · [官网](https://docs.keepnotes.ai/guides/quickstart/) · 组织维护

**给 AI agent 的反思式记忆系统：语义存储与检索基础设施**

面向 AI agent 的记忆工具：将笔记、文件、URL、PDF、音视频等内容摄取后自动摘要、嵌入、打标签，支持语义相似度、BM25 全文与图遍历三种检索；带 `_inverse` 声明的标签可转为图的边（如 speaker/author/cites），形成可导航的知识图。以 CLI 与 MCP 接口提供，含引导 agent 反思实践（行动前中后检查意图、记录学习）的技能指令。可完全本地运行（MLX/Ollama）或使用 API 供应商，另有托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄取时自动摘要、嵌入、打标签，支持文本/PDF/Office/音频/图像等多格式
- 边标签机制：标签可转为带反向链接的图关系，支持图遍历深搜
- CLI 与 MCP 接口，集成 Claude Code/Copilot/LangChain/OpenClaw 等十余种 agent 工具
- 完全本地可运行（Ollama/MLX），无需 API key

## 适用场景

- 为我的 coding agent 配置跨会话记忆与反思实践
- 把项目文档、笔记、git 提交建成可语义检索的知识库
- 通过 MCP 让任意 agent 客户端接入统一记忆存储

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: It includes skill instructions for reflective practice, and a powerful semantic memory system with command-line and 
> L40: keep is designed as a skill for AI agents — a practice, not just a tool. The skill instructions teach agents to ref
> L61: |**Any MCP client**|Stdio server with 3 tools (`keep_flow`, `keep_prompt`, `keep_help`)|

## 星数曲线

```mermaid
xychart-beta
    title "generalbusiness-ai/keep 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-26 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `146adbe31ef8` · [字段定义](../../DATASET.md)*
