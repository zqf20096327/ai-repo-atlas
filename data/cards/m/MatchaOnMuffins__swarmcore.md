# MatchaOnMuffins/swarmcore

⭐ 15 · Python · MIT · 推送 2026-06-20 · [GitHub](https://github.com/MatchaOnMuffins/swarmcore) · 个人维护

**Python 多智能体编排库：将 AI agent 组合为串并行工作流**

以 Python 库形式提供的多智能体编排框架：用 `>>`（串行）与 `|`（并行）算子把 agent 组合成流程，分支经 asyncio.gather 并发执行；内置 researcher/analyst/writer/editor/summarizer 五种 agent 工厂。上下文在步骤间自动传递——上一步给全量输出、更早步骤给摘要，agent 可按需展开。任意 LiteLLM 兼容模型可用（默认 anthropic/claude-opus-4-6，需 API key），工具用普通 Python 函数传入。面向构建 AI 工作流的开发者。

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

- `>>` 串行 / `|` 并行算子自由组合流程，分支并发执行
- 上一步全量输出+更早步骤摘要的自动上下文传递，可按需展开
- 5 个预置 agent 工厂（researcher/analyst/writer/editor/summarizer）
- 任意 LiteLLM 兼容模型，含 Ollama 本地免 key 路径

## 适用场景

- 把研究、分析、写作等角色串成自动化内容生产流水线
- 并行分支分别处理后由后续 agent 汇总合成
- 在本地 Ollama 模型上跑多 agent 流程避免 API 费用

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Multi-agent orchestration for Python. Compose AI agents into sequential and parallel flows with automatic context sh
> L39: - **Any model** — works with any LiteLLM-compatible provider (Anthropic, OpenAI, Gemini, Groq, Ollama, etc.)
> L141: Any LiteLLM-compatible model. Set the API key for your provider:

## 星数曲线

```mermaid
xychart-beta
    title "MatchaOnMuffins/swarmcore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1c457b2343ea` · [字段定义](../../DATASET.md)*
