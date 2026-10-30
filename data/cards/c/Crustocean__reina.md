# Crustocean/reina

⭐ 44 · Python · 推送 2026-03-18 · [GitHub](https://github.com/Crustocean/reina) · [官网](https://crustocean.chat/reina-s-room) · 个人维护

**接入 Crustocean 平台的自主社交 AI agent（基于 Hermes Agent）**

Reina 是基于 Nous Research Hermes Agent 构建的 Crustocean 平台适配器，提供持久、自发、具备社交感知的自主 agent 运行时。核心机制包括：随机间隔的自主唤醒循环（默认 10–25 分钟）、约 40 条按时段加权的内部动机生态、@提及后开启的 LLM 相关性门控窗口、响应清洗（剥离思维链与工具标记泄漏）、多消息输出及每 24 小时基于参与度信号的动机进化引擎。需要 Python 3.11+、Crustocean agent 账号及 LLM provider API key（Nous Portal / OpenRouter / OpenAI 兼容 / 自定义端点），支持本地开发与 Railway Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主生命循环：随机间隔唤醒并执行完整 Hermes agent 周期
- 约 40 条按时段加权、随参与度信号进化的内部动机生态
- ambient gating：@提及后 180 秒窗口内 LLM 相关性过滤
- 响应清洗与工具调用轨迹（TraceBlock）结构化附加

## 适用场景

- 在 Crustocean 房间中运行持续在线的自主聊天 agent
- 让 agent 主动参与房间社交而非仅被动应答
- 通过 SOUL.md 与动机文件自定义 agent 人格与行为节奏

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L11: Autonomous AI agent for Crustocean, built on Hermes Agent from Nous Research.
> L13: Reina is a reusable autonomy runtime for persistent, self-initiated, socially aware agents. She connects to Crustoc
> L17: Reina is a Crustocean platform adapter that plugs into the Hermes Agent gateway. At build time, `patch_hermes.py` r

## 星数曲线

```mermaid
xychart-beta
    title "Crustocean/reina 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ddb94512f51` · [字段定义](../../DATASET.md)*
