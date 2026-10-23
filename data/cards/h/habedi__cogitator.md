# habedi/cogitator

⭐ 191 · Python · MIT · 推送 2026-07-05 · [GitHub](https://github.com/habedi/cogitator) · 个人维护

**实验链式思考提示策略的 Python 工具库，供研究与集成**

提供统一同步/异步 API 的 Python 工具库，用于在 LLM 上实验和使用链式思考（CoT）提示方法，内置 Self-Consistency CoT、Automatic CoT、Least-to-Most、Tree of Thoughts、Graph of Thoughts 等多种策略实现，支持 OpenAI、Ollama、OpenRouter 作为 LLM 提供方，结构化输出经 Pydantic 校验，并附带可在 GSM8K、StrategyQA 等数据集上评估 CoT 策略的基准框架。面向研究者和希望将 CoT 策略集成进 AI 应用的开发者，以 PyPI 包或源码（Poetry）方式安装。

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

- 统一 sync/async API 调用多种 CoT 策略
- 支持 OpenAI、Ollama、OpenRouter 作为 LLM 提供方
- Pydantic 校验的结构化模型输出
- 内置可扩展基准框架（GSM8K、StrategyQA 等数据集）

## 适用场景

- 在我的研究中对比不同 CoT 提示策略的效果
- 为 AI 应用集成 Least-to-Most 或 Tree of Thoughts 等推理策略
- 在本地 Ollama 模型上运行 Self-Consistency CoT 示例

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L17: Cogitator is a Python toolkit for experimenting and working with
> L23: The toolkit aims to make it easier to use popular CoT strategies and frameworks for research or integrating them in

## 星数曲线

```mermaid
xychart-beta
    title "habedi/cogitator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 190 --> 192
    line [191, 191]
```

2026-10-18 191 → 2026-10-23 191（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b40daaa4a9b4` · [字段定义](../../DATASET.md)*
