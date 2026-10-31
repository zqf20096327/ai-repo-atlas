# KennispuntTwente/tidyprompt

⭐ 33 · R · NOASSERTION · 推送 2026-09-29 · [GitHub](https://github.com/KennispuntTwente/tidyprompt) · [官网](https://kennispunttwente.github.io/tidyprompt/) · 组织维护

**R 语言的 LLM 提示词构建与交互逻辑框架**

面向 R 开发者的 LLM 交互框架：以可组合的 prompt wraps（类似 ggplot2 的构建块）修改提示词并同时附加抽取、验证与反馈逻辑，支持结构化输出、验证失败自动反馈重试、chain-of-thought/ReAct 推理模式、R 函数调用与 R 代码生成执行、MCP 服务器工具。定位与 ellmer/tidyllm 互补：不做 API 接口层，而是兼容 ellmer chat 对象作为 provider，provider-agnostic。通过 GitHub 与 CRAN（0.4.0）分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- prompt wraps 组合式构建提示词并附带抽取/验证/反馈函数
- 结构化输出、自动反馈重试、CoT/ReAct 推理模式
- LLM 可自主调用 R 函数（tools）并执行 R 代码，支持 MCP 工具
- 兼容 ellmer chat 对象，支持其原生结构化输出、工具与流式

## 适用场景

- 在 R 中以管道语法构造带验证逻辑的 LLM 提示词
- 让 LLM 以指定类型/格式返回结构化结果并在失败时自动重试
- 让 LLM 调用 R 包函数或 MCP 服务器工具完成检索与操作

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: ‘tidyprompt’ is an R package to easily construct prompts and associated
> L165: ‘tidyprompt’ is primarily focused on offering a framework for

## 星数曲线

```mermaid
xychart-beta
    title "KennispuntTwente/tidyprompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9fdd12ebc0e7` · [字段定义](../../DATASET.md)*
