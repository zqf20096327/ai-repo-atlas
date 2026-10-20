# kyegomez/tree-of-thoughts

⭐ 4,595 · Python · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/kyegomez/tree-of-thoughts) · [官网](https://discord.gg/qUtxnK2NMf) · 个人维护

**Tree of Thoughts 推理搜索的即插即用实现**

将 Tree of Thoughts 论文方法实现为 Swarms 框架内的 TreeOfThoughts 组件：让语言模型按'生成候选步骤—打分评估—搜索剪枝—回溯'的流程推理，而非单次生成。支持 BFS 束搜索与 DFS 回溯两种算法、propose/sample 生成策略与 value/vote 评估策略，模型输出经 Pydantic schema 校验，同层调用可并发。通过 LiteLLM 接入任意支持函数调用的模型（OpenAI/Anthropic/Groq 等），pip 安装并配置 .env 中的 API key 后使用，附数学、物理、逻辑等带预期答案的示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BFS/DFS 两种搜索算法，支持剪枝与回溯
- propose/sample 生成策略与 value/vote 评估策略可组合
- 模型输出经 Pydantic schema 函数调用校验，同层调用并发
- model_name 接受任意支持函数调用的 LiteLLM 模型字符串

## 适用场景

- 让 LLM 用搜索式推理求解多步数学与逻辑题
- 在规划、调度等需要保留多条部分解的任务上提升推理质量
- 对比不同搜索/评估策略对同一问题的求解效果

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: Tree of Thoughts (ToT) makes a language model reason by search instead of in a single pass. The model proposes seve
> L18: > Tree of Thoughts now ships as part of the Swarms framework as `TreeOfThoughts`. The examples and docs below use t
> L44: `model_name` accepts any LiteLLM model that supports function calling, so you can set `ANTHROPIC_API_KEY`, `GROQ_AP

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/tree-of-thoughts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 4592 --> 4596
    line [4593, 4595, 4595]
```

2026-10-18 4,593 → 2026-10-20 4,595（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `0f40189e8eb8` · [字段定义](../../DATASET.md)*
