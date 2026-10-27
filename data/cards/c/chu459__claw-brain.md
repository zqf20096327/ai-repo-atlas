# chu459/claw-brain

⭐ 32 · Python · AGPL-3.0 · 推送 2026-06-08 · [GitHub](https://github.com/chu459/claw-brain) · [官网](https://twitter.com/Claw_brain) · 个人维护 · 中文 README

**给 OpenClaw 加自主决策循环的决策引擎**

运行在 OpenClaw 浏览器自动化之上的自主决策引擎：每个循环执行思考→决策→执行→观察→再思考，由 LLM 驱动的 Brain 输出结构化决策，经 OpenClaw 客户端转为浏览器操作，结果与失败经验写入持久化 Memory。用户设定可度量目标（如收入目标、获客数），系统自行拆解并迭代执行。提供 FastAPI Web 控制台（实时监控、人机对话）与 CLI 两种运行方式，需 Python 3.13+、已运行的 OpenClaw 及 LLM API key。Brain 与执行层以自然语言为接口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 思考→决策→执行→观察的自校正决策循环
- 持久化 Memory 记录成功/失败经验与策略演进
- FastAPI Web 控制台：实时监控、人机对话、参数配置
- Brain 与执行层以自然语言为接口，输出结构化 JSON 决策

## 适用场景

- 设定收入或获客等目标，让系统自主调研、测试并迭代
- 让 AI 自动找出该执行什么任务，而非只按指令执行
- 通过 Web 控制台监控自主任务并在必要时人工介入

## 场景标签

`浏览器自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: OpenClaw gives AI "hands and feet" — browser automation that follows instructions. **Claw-brain gives it a "brain"*
> L100: |**Brain**|LLM-driven strategy engine. Receives context, outputs structured decisions (JSON)|
> L101: |**OpenClaw Client**|Bridge to OpenClaw. Translates Brain's natural-language decisions into browser operations|

## 星数曲线

```mermaid
xychart-beta
    title "chu459/claw-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a01ba1efd521` · [字段定义](../../DATASET.md)*
