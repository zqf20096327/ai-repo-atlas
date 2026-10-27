# tommyguolin/openclaw-soul

⭐ 22 · TypeScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/tommyguolin/openclaw-soul) · [官网](https://clawhub.ai/plugins/openclaw-soul-plugin) · 个人维护 · 中文 README

**给 OpenClaw 助手加自主思考、长期记忆与自我改进的插件**

面向 OpenClaw 的插件，为 AI 助手增加后台自主思考循环、跨重启的长期记忆、主动消息与自主行动能力：通过消息钩子记录交互、提取用户画像，以激活驱动的记忆机制生成想法，经价值门控后主动发送；支持 analyze-problem、run-agent-task、observe-and-improve 等行动，写操作需 autonomousActions 显式开启。模型、搜索与消息通道（Telegram/Discord/飞书等）均从 OpenClaw 配置自动检测，通过 git clone 或 ClawHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台自主思考循环（对话回放、问题检测、兴趣学习、五类情感需求驱动）
- 持久化长期记忆：交互记忆、知识库、用户画像与记忆关联图
- 自主行动与自我改进：读日志分析根因、可实施修复并汇报（写操作需显式授权）
- 证据感知学习与跨重启的思维日志（thought-cycles.jsonl）

## 适用场景

- 让已有的 OpenClaw 助手在对话之外自主调查问题并主动汇报结论
- 为聊天机器人积累跨会话的用户画像与长期记忆
- 让助手基于对话中提到的 bug 自主分析并尝试修复代码

## 场景标签

`Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8: > An autonomous thinking, memory, and self-improvement plugin for OpenClaw
> L49: Soul runs a background thought service that generates thoughts based on:
> L155: |Hook|What Soul Does|

## 星数曲线

```mermaid
xychart-beta
    title "tommyguolin/openclaw-soul 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `20b63c9aa07c` · [字段定义](../../DATASET.md)*
