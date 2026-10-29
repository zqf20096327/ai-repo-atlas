# nshkrdotcom/DSPex

⭐ 21 · Elixir · MIT · 推送 2026-09-27 · [GitHub](https://github.com/nshkrdotcom/DSPex) · 组织维护

**把 DSPy 框架带入 Elixir 的声明式 LLM 编程库**

通过 SnakeBridge 生成的 Dspy.* 绑定与轻量 DSPex FFI 封装两层接口，将 Stanford NLP 的 DSPy 3.4.0（Signature、Predict、ChainOfThought、优化器等）完整暴露给 Elixir 开发者，经 gRPC 桥与 Python 进程池通信。支持 LiteLLM 兼容的 100+ LLM 提供商，内置面向 ML 推理的超时档位（默认 10 分钟），全部函数返回 {:ok/:error} 元组。安装依赖 Elixir 1.18+、Python 3.9+ 与 uv，mix snakebridge.setup 自动创建托管 venv 并安装 dspy-ai。附带 20 个示例（含 RAG、GEPA、RLM 数据提取）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SnakeBridge 生成的 Dspy.* 绑定镜像 DSPy 包结构，覆盖完整 API
- 支持 LiteLLM 兼容的 100+ LLM 提供商（OpenAI/Anthropic/Google/Ollama）
- 面向 ML 推理工作负载的超时档位（默认 ml_inference 10 分钟）
- 20 个示例，含 NYC 311 五万条真实记录的 RLM 数据提取实验

## 适用场景

- 在 Elixir/BEAM 应用中用 DSPy 的 Signature 与模块编写 LLM 程序
- 对提示程序执行 BootstrapFewShot/GEPA 等优化
- 在 Erlang VM 上构建具备 Python 互操作的数据提取与分析流水线

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  DSPy for Elixir via SnakeBridge
> L13: DSPex brings DSPy — Stanford NLP's framework for programming language models — to Elixir. It ships with SnakeBridge
> L20: - **Full DSPy access** — Signatures, Predict, ChainOfThought, optimizers, and more

## 星数曲线

```mermaid
xychart-beta
    title "nshkrdotcom/DSPex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `53c14c8dc9d8` · [字段定义](../../DATASET.md)*
