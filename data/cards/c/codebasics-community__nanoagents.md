# codebasics-community/nanoagents

⭐ 25 · Python · Apache-2.0 · 推送 2026-05-07 · [GitHub](https://github.com/codebasics-community/nanoagents) · 组织维护

**极简 ReACT agent 构建库：200 行内实现推理-行动循环**

Codebasics 社区维护的 Python 库，以不到 200 行纯实现 ReACT（Reason + Act）循环，处理推理、工具分发、重试与历史记录。用户自带任意 LLM 可调用对象，库本身零强制依赖，无框架绑定。Agent 支持装饰器与 add_tool 两种工具注册方式，可配置 max_steps 与 max_retries；提供四个从基础到实际场景的可运行示例（含计算器、多工具链式研究 agent）。需 Python ≥ 3.11，Apache 2.0 许可。

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

- ReACT 循环以不到 200 行纯 Python 实现，零强制依赖
- 自带 LLM callable 即可接入，无框架锁定
- 装饰器与 add_tool 两种工具注册方式，参数 schema 自动解析
- 提供 Groq/OpenAI/Anthropic/Ollama 等多 provider 适配示例与四个可运行 demo

## 适用场景

- 构建带工具调用的 ReACT agent 而不引入重型框架
- 在学习或教学场景理解 ReACT 循环的实现机制
- 快速实验自定义工具链的小型 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: `nanoagents` implements the **ReACT** (Reason + Act) loop in under 200 lines of pure Python — no framework lock-in,
> L43: The library has **zero mandatory dependencies** — bring your own LLM client.

## 星数曲线

```mermaid
xychart-beta
    title "codebasics-community/nanoagents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5dca5c01f6cd` · [字段定义](../../DATASET.md)*
