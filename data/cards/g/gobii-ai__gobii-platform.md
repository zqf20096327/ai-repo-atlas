# gobii-ai/gobii-platform

⭐ 496 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/gobii-ai/gobii-platform) · [官网](https://gobii.ai) · 组织维护

**面向团队的自托管持久自主 agent（AI 员工）运行平台**

开源的 Gobii Platform，用于自托管部署和开发持久运行的自主 agent：每个 agent 可持续运行、由日程与事件（邮件/SMS/Webhook/API）唤醒、操作真实浏览器、调用外部系统并与其他 agent 点对点协调；可像员工一样通过专属邮件/短信端点联系。基于 browser-use，提供 SQLite 运行态存储、加密密钥、代理管控出口与 Kubernetes/gVisor 沙箱支持。通过安装脚本或 git clone + docker compose 部署，另有托管版 Gobii Cloud 与远程 MCP 服务（16 个工具）。模型接入在初始化时选择 OpenAI/OpenRouter/Anthropic/Fireworks 或自定义端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 具备专属邮件/SMS/Web 端点，可被直接联系并 7x24 运行
- 基于 browser-use 的有头浏览器运行时，持久化配置与代理感知路由
- 加密密钥、代理管控出口、Kubernetes/gVisor 沙箱计算等安全控制
- Gobii Cloud 兼作远程 MCP 服务器，提供 16 个工具供 Codex/Claude Code/Cursor/VS Code 等客户端接入

## 适用场景

- 团队自托管常驻 agent 承接日程驱动与事件驱动的自动化工作
- 通过邮件或短信给 agent 派活并接收回复
- 从 MCP 客户端创建、管理和协调持久 agent

## 场景标签

`Agent 框架` `浏览器自动化` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L23: Gobii is an AI employee platform for running durable autonomous agents in production.
> L25: Each agent can run continuously, wake from schedules and events, use real browsers, call external systems, and coor

## 星数曲线

```mermaid
xychart-beta
    title "gobii-ai/gobii-platform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 495 --> 497
    line [496, 496]
```

2026-10-18 496 → 2026-10-22 496（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b0e9e0758960` · [字段定义](../../DATASET.md)*
