# dorringel/epsiclaw

⭐ 51 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/dorringel/epsiclaw) · [官网](https://dorringel.github.io/epsiclaw/) · 个人维护

**教学用极简个人 agent：515 行 Python 复现 OpenClaw 核心循环**

将 OpenClaw 的核心算法精简为 515 行 Python、6 个文件、单一依赖（httpx）的教学实现，风格仿 Karpathy 的 micrograd/nanoGPT。包含四个组件：消息通道、markdown 文件记忆、LLM 决策加工具执行的 agent 循环、定时提醒 cron。运行需 OpenAI API key 与 Telegram bot token，可选 Tavily 做网页搜索。作者明确声明非生产软件：无鉴权、无沙箱、无限流，单用户单模型单通道。

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

- 515 行 Python、6 文件、单一依赖实现 agent 核心循环
- 组件拆分：channel / memory / agent / cron
- markdown 文件作为可读写的持久记忆
- 明确声明非生产软件、非框架、单用户设计

## 适用场景

- 学习个人 agent 的最小可行算法结构
- 阅读源码理解 LLM 决策加工具执行的循环
- 以 Telegram 为通道跑通一个单用户 agent demo

## 场景标签

`AI 助手` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L3: The same algorithm that runs inside OpenClaw (522K LOC) - stripped to ε. 515 lines of Python, 6 files, one dependenc
> L22: - An **agent** - LLM decides, tools execute, repeat (`agent.py` + `llm.py` + `tools.py`, 334 lines)

## 星数曲线

```mermaid
xychart-beta
    title "dorringel/epsiclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-26 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1e92c1fbc333` · [字段定义](../../DATASET.md)*
