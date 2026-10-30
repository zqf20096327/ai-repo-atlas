# thevpc/naru

⭐ 16 · Java · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/thevpc/naru) · 个人维护

**面向 JVM 的持久化 actor 式 AI agent 运行时**

NARU 是基于 Java 的通用 agent 运行时与微内核式平台，可作为库嵌入或作为完整应用（Nuts 包）启动。提供持久化会话（可插拔 NaruSessionStore）、并发任务调度、可在运行中修改的例程（routine）、脚本化 REPL，以及扩展点机制用于组合领域专属 agent。LLM 接入覆盖 Ollama、llama.cpp、OpenAI、Anthropic、Gemini、Groq、DeepSeek、Qwen 等本地与云端提供方。当前自带工具偏向软件开发场景；后端 turn API 标注为早期阶段，README 列出多项未完成的必需事项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 可插拔会话存储（文件实现可替换为自有数据库）与 checkpoint 恢复
- 并发任务运行时：durable 事件、等待、例程与任务局部状态
- 本地与云端 LLM 提供方扩展（Ollama/llama.cpp/OpenAI/Anthropic/Gemini/Groq/NIM 等），支持按任务选模型与流式输出
- 微内核式组合：模型、工具、会话存储经扩展点发现

## 适用场景

- 在 JVM 项目中嵌入可持久化的多任务 agent 运行时
- 通过 REPL 与例程脚本执行多阶段软件修复/审查流程
- 组合自有工具与模型提供方构建领域专属 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A durable, actor-based AI agent runtime for the JVM.
> L53: context, and execution policy. The more useful label is **agent runtime/platform** because
> L66: LLM applications and orchestration. NARU aims to provide both an embeddable runtime and

## 星数曲线

```mermaid
xychart-beta
    title "thevpc/naru 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7f021247c9ea` · [字段定义](../../DATASET.md)*
