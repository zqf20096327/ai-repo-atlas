# Temaki-AI/clawd-control

⭐ 114 · HTML · MIT · 推送 2026-02-28 · [GitHub](https://github.com/Temaki-AI/clawd-control) · [官网](https://clawdcontrol.com) · 组织维护

**监控管理 Clawdbot AI agent 集群的实时仪表盘**

面向运行 Clawdbot agent 的用户的单屏 Web 仪表盘：通过 SSE 实时展示 agent 状态、健康指标、会话/频道/配置详情，自动发现本机 agent，支持远程 agent 手动配置接入；附带 agent 创建向导、主机 CPU/RAM/磁盘指标、密码会话认证与键盘快捷键。实现为单个 Node.js 服务器（Node 18+），无构建步骤，仅一个依赖 ws，前端为原生 HTML/JS。需先安装 Clawdbot 才能使用。

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

- SSE 实时监控 agent 集群状态与健康指标
- 本机 agent 自动发现，远程 agent 经 agents.json 接入
- 单 Node.js 服务器实现，无构建步骤，仅 1 个依赖（ws）
- 首次运行自动生成密码的会话认证

## 适用场景

- 一屏查看我运行的多个 Clawdbot agent 的状态与指标
- 深入排查某个 agent 的会话、频道与配置
- 监控运行 agent 的主机 CPU/RAM/磁盘资源

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: Clawd Control gives you a single-screen view of your entire AI agent fleet. If you run Clawdbot agents, this is you
> L91: Yes — Clawd Control is a dashboard *for* Clawdbot agents. Install Clawdbot first: `npm install -g clawdbot`

## 星数曲线

```mermaid
xychart-beta
    title "Temaki-AI/clawd-control 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 113 --> 116
    line [115, 114, 114]
```

2026-10-18 115 → 2026-10-26 114（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `207effc10c90` · [字段定义](../../DATASET.md)*
