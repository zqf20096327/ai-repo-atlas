# opisaac9001/eidos

⭐ 24 · Python · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/opisaac9001/eidos) · 个人维护

**本地优先的持续模拟人生：一个你不在线也继续生活的模拟人**

Eidos 模拟一位住在英格兰小镇 Alderwick（基于 Frome 真实街道）的虚构人物 Patrick，分钟级实时推进他的作息、工作、金钱、社交与内心活动，用户可与他对话。语言模型只负责提出 thoughts/对话/计划，仿真规则验证后才生效；所有变更是 SQLite 事件日志中的事件，可检查、重放或分叉。本地优先、无账号、无运行时依赖，离线可用确定性文字模板替代模型，也可接入任意 OpenAI 兼容服务（Ollama、LM Studio、vLLM 等），支持按角色分配模型与备份、每日预算。提供 Web Observatory、CLI 与世界包导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则层验证模型提议，事件溯源可重放/分叉全部历史
- 模型无关：离线用确定性模板，或接入 Ollama/LM Studio/vLLM/OpenAI 兼容 API
- 按角色配置模型首选与备份，失败或超预算时可见跳过而非伪造
- 可选接入真实新闻 RSS 与 Open-Meteo 天气，世界仍可全离线运行

## 适用场景

- 我想养一个持续生活、有记忆与性格演化的模拟角色并与他对话
- 在没有账号和云依赖的家用服务器或树莓派上长期运行生成式 agent
- 研究生成式 agent 的事件溯源架构与模型-规则分工

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L17: Eidos is local-first and model-agnostic. It runs fully offline with written stand-ins, or with any OpenAI-compatibl
> L30: |💭|**An inner life that never stops.** A continuous stream of passing thoughts on a small local model, moods and fe
> L97: Offline, Eidos uses deterministic stand-ins (written templates). They're fine for watching the simulation, but not 

## 星数曲线

```mermaid
xychart-beta
    title "opisaac9001/eidos 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-19 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f7f9c332b196` · [字段定义](../../DATASET.md)*
