# Dyalwayshappy/Spice

⭐ 247 · Python · NOASSERTION · 推送 2026-06-19 · [GitHub](https://github.com/Dyalwayshappy/Spice) · [官网](https://pypi.org/project/spice-runtime/) · 个人维护 · 中文 README

**Agent 系统的决策层运行时：感知上下文、比较选项、审批后委托执行**

Spice 是面向 agentic AI 系统的决策运行时，运行 perception → state model → simulation → decision → execution → reflection 循环。它在执行前把下一步动作转为有来源、可比较、需审批的决策卡（候选、证据、取舍、审批点），再委托给 Claude Code、Codex、Hermes、OpenClaw 等执行器；感知工具只读，执行跨界需显式审批。LLM 用于候选扩展与模拟等环节，支持 OpenRouter/OpenAI/Anthropic/DeepSeek/MiMo 等提供方及 deterministic 无模型路径，另有 subprocess 本地路径。以 pip 包与源码两种方式安装，提供交互 shell 与一次性 CLI 命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 决策与执行分离：决策卡含候选、证据、取舍与审批点
- 5 种执行器委托（Codex/Claude Code/Hermes/OpenClaw/SDEP 子进程），执行需审批
- 只读感知路径：工作区/git 状态/URL/轮询/OpenChronicle MCP
- decision.md 用户可编辑的决策偏好与约束文件

## 适用场景

- 在让执行 agent 动手前先比较方案并留存审计痕迹
- 为 Claude Code/Codex 等执行器加一层审批边界的决策控制
- 通过交互 shell 询问下一步该做什么及原因

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L82: Spice is a **decision runtime for agentic AI systems**.
> L98: Spice does not replace agents like Claude Code, Codex, Hermes, or OpenClaw.
> L341: Spice separates decision from execution:

## 星数曲线

```mermaid
xychart-beta
    title "Dyalwayshappy/Spice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 247 --> 249
    line [248, 248]
```

2026-10-18 248 → 2026-10-25 248（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b99ff197ed5e` · [字段定义](../../DATASET.md)*
