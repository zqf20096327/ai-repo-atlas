# daggerhashimoto/openclaw-nerve

⭐ 873 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/daggerhashimoto/openclaw-nerve) · [官网](https://nerve.zone) · 个人维护

**OpenClaw 的自托管 Web 驾驶舱：语音对话与多 agent 运营界面**

面向 OpenClaw 网关的自托管 Web 控制台：提供流式对话、语音输入（本地 Whisper 转写、多 TTS 提供方）、多 agent 舰队管理（每个 agent 可有独立 workspace/记忆/身份/技能）、会话树、cron、看板工作流、提案收件箱、图表与 token 用量/成本追踪。前端 React 19 + Vite，后端 Hono on Node.js，默认绑定 127.0.0.1，可密码认证暴露到网络。需要 Node.js 22+ 与一个 OpenClaw 网关。

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

- 单一控制面运行多 agent，支持子 agent 与逐 agent workspace/记忆
- 语音交互：push-to-talk、唤醒词、本地 Whisper 转写、多 TTS 提供方
- 运营层：cron、会话树、看板、review 流程、提案收件箱、模型覆盖
- 可观测性：token 用量、成本追踪、上下文压力计、agent/事件日志

## 适用场景

- 在浏览器里集中操作和监控多个 OpenClaw agent
- 用语音与 agent 对话并实时浏览编辑其工作区文件
- 把 cron 自动化、看板委派与用量成本放进同一界面管理

## 场景标签

`多智能体` `语音合成` `语音识别` `语音 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L38: Run multiple agents from one place. Each agent can have its own workspace, subagents, memory, identity, soul, and s
> L124: Nerve sits in front of the gateway and gives you a richer operating surface in the browser.
> L127: Browser ─── Nerve (:3080) ─── OpenClaw Gateway (:18789)

## 星数曲线

```mermaid
xychart-beta
    title "daggerhashimoto/openclaw-nerve 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-29"]
    y-axis "stars" 868 --> 874
    line [869, 871, 873, 873]
```

2026-10-18 869 → 2026-10-29 873（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9de3414bfb9a` · [字段定义](../../DATASET.md)*
