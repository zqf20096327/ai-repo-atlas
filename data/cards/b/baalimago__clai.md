# baalimago/clai

⭐ 148 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/baalimago/clai) · 个人维护

**命令行 AI 上下文工具：向任意 LLM 查询并注入 shell 上下文**

用 Go 编写的命令行 context-feeder，将 shell 上下文通过可配置模板注入系统提示词，支持管道输入输出与多种 LLM 供应商（OpenRouter、Ollama、HuggingFace、Mistral、OpenAI、DeepSeek、Gemini、Anthropic 等）。支持会话导入、Agent Skills、预提示 Profiles、MCP 客户端，并可作为 Go 库嵌入以获得带类型的结构化输出。提供安装脚本、go install 与 Nix flake 三种安装方式，测试覆盖率 91.5%。

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

- shell 上下文注入系统提示词（可配置模板）
- 支持十余家 LLM 供应商（OpenRouter/Ollama/OpenAI/Gemini/Anthropic 等）
- MCP 客户端支持与 Agent Skills 导入
- 可作为 Go 库嵌入，支持类型化结构化输出

## 适用场景

- 在终端中直接向 LLM 提问并携带 shell 上下文
- 通过管道将命令输出送入 AI 处理
- 用预置 Profiles 定制工作流与 agent

## 场景标签

`AI 助手` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10:  <code>clai</code> ( /klaɪ/ , like "cli" in " cli mate") is a command line context-feeder for any ai task.
> L62: - **Shell context injection** - Inject shell context into the system prompt via configurable templates.

## 星数曲线

```mermaid
xychart-beta
    title "baalimago/clai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 147 --> 149
    line [148, 148]
```

2026-10-18 148 → 2026-10-25 148（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6c233faad9f9` · [字段定义](../../DATASET.md)*
