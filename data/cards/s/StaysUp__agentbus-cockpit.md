# StaysUp/agentbus-cockpit

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-11-17 · [GitHub](https://github.com/StaysUp/agentbus-cockpit) · [官网](https://agentbus.art) · 个人维护

**AgentBus 的自托管浏览器驾驶舱：查看会话、轮次与模型调用成本**

基于 React/TypeScript 的 AgentBus 前端驾驶舱，展示 agent 会话、每轮对话、每次模型调用及其成本，仅调用 AgentBus 公开 API。随 AgentBus 内置发布（agentbus up 自带服务），本仓库供开发者基于 dev server 修改驾驶舱本身。支持管理 Claude Code/Codex/Antigravity 等 harness 的 agent 配置、订阅与 OpenRouter 密钥接入、Runners 机器管理与每轮权限设置。开发需 Node.js 20.19+/22.12+ 与同版本运行中的 AgentBus。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 展示每个会话、每轮结果与每次模型调用及其成本
- 仅使用 AgentBus 公开 API，自有程序可读取同样数据
- 管理 agent 配置、订阅登录与 OpenRouter 密钥（密钥仅存于 control 端）
- 支持 ?recorded 参数离线打开录制示例

## 适用场景

- 查看多 agent 会话中每轮的模型调用与花费
- 管理多台 Runner 机器与每轮的沙箱/权限策略
- 二次开发定制 AgentBus 的前端界面

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: It shows your agents' sessions, every turn, every model call and its cost. It uses only the public
> L16: **The cockpit ships inside AgentBus.** `agentbus up` serves it on its own address and opens it
> L29: You need Node.js 20.19 or later in the 20 line, or 22.12 or later (Vite needs one of these), and a

## 星数曲线

```mermaid
xychart-beta
    title "StaysUp/agentbus-cockpit 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-18"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-11-10 18 → 2026-11-18 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `6dd0b3e51aa2` · [字段定义](../../DATASET.md)*
