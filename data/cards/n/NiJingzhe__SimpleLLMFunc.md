# NiJingzhe/SimpleLLMFunc

⭐ 78 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/NiJingzhe/SimpleLLMFunc) · [官网](https://simplellmfunc.cn) · 个人维护 · 中文 README

**Python LLM 应用框架：以装饰器把 LLM 调用写成带类型的函数**

面向开发者的 LLM 应用/Agent 开发框架，核心是把 LLM 调用封装为带类型标注的 Python 函数：@llm_function 返回 Pydantic 模型或基础类型，@llm_chat 构建多轮 Agent，DocString 即系统提示词。上下文通过 9 种 mutation 在编译边界变更，SelfRef 允许 Agent 读写自身上下文（记忆/压缩/分叉）。支持 OpenAI/DeepSeek/Anthropic/火山方舟/千帆/Ollama/vLLM 等接口，内置 PyRepl、文件工具集、TUI、多 Key 负载均衡与限流。pip 安装，异步原生。

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

- @llm_function/@llm_chat/@tool/@tui 装饰器体系，DocString 即系统提示
- 9 种 mutation 驱动的上下文演化与 SelfRef 自编辑（记忆/压缩/Fork）
- 内置 PyRepl 持久 IPython 子进程与工作区文件工具集
- 多 API Key 最小堆负载均衡、令牌桶限流、Langfuse 可观测集成

## 适用场景

- 用类型安全函数封装 LLM 调用做数据抽取或批量分类
- 30 行代码搭建带 REPL、文件工具与自我反思的编码 Agent
- 多供应商 API Key 池化与流量控制场景

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L30: |**LLM is Function**|An LLM call is indistinguishable from a Python function call: signature, type hints, return va
> L92: │  L1. Decorator Layer          @llm_function / @llm_chat / @tool         │

## 星数曲线

```mermaid
xychart-beta
    title "NiJingzhe/SimpleLLMFunc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-26 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `51f3861f26ae` · [字段定义](../../DATASET.md)*
