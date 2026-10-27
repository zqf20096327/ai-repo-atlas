# al1-nasir/codegraph-cli

⭐ 27 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/al1-nasir/codegraph-cli) · 个人维护

**终端代码智能 CLI：语义搜索、影响分析、对话式编码与多 agent 改码**

名为 cg 的命令行工具：用 tree-sitter 解析代码库为依赖图存入 SQLite 并生成嵌入向量（LanceDB），提供语义搜索、多跳影响分析、ASCII/HTML 图可视化、浏览器代码浏览器。支持六种 LLM 提供商的对话式编码会话，可选 CrewAI 四 agent 流水线执行文件读写、打补丁与回滚（每次修改自动备份）。另含 DOCX 文档导出与 AI 生成 README 的自动入职功能。Python 3.9+，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter 解析为语义依赖图，SQLite + LanceDB 存储
- 六种 LLM 提供商（Ollama/Groq/OpenAI/Anthropic/Gemini/OpenRouter）可切换
- CrewAI 四 agent 流水线：协调者、文件工程师、开发者、代码分析员，文件修改自动备份可回滚
- 五种可配置嵌入模型（hash 默认零依赖至 qodo-1.5b）

## 适用场景

- 重构前做多跳依赖影响分析
- 在终端与 LLM 对话式编码并让多 agent 自动改文件
- 为新项目自动生成 README 与 DOCX 架构文档
- 可视化浏览代码库依赖关系

## 场景标签

`语义搜索` `编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: CodeGraph CLI (`cg`) parses your codebase into a semantic graph, then exposes that graph through search, impact ana
> L20: - **Conversational Chat** — natural language coding sessions with RAG context
> L21: - **Multi-Agent System** — CrewAI-powered agents for code generation, refactoring, and analysis

## 星数曲线

```mermaid
xychart-beta
    title "al1-nasir/codegraph-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `42ffce614af2` · [字段定义](../../DATASET.md)*
