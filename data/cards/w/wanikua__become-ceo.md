# wanikua/become-ceo

⭐ 64 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/wanikua/become-ceo) · 个人维护 · 中文 README

**在 Discord 上搭建 7 个 AI 高管 agent 组成虚拟团队**

基于 OpenClaw/Clawdbot 的 Discord 多 agent 团队方案：一条脚本在 Linux/macOS 服务器上部署 7 个各有独立 bot 的专职 agent（工程、财务、市场、DevOps、法务、管理、幕僚长），通过 @mention 对话派活。机制包括：持久记忆、60+ 工具（GitHub/Notion/浏览器/cron/TTS）、sessions_spawn 子 agent 委派、按 agent 分级选模型控制成本、可选 Docker 沙箱隔离、Discord 语音转文字+TTS 语音会议。需手动创建 7 个 Discord bot，API 费用约 $15–30/月。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条脚本 5 分钟部署 7 个专职 AI agent（各有独立 Discord bot 与人格）
- sessions_spawn 子 agent 委派机制与 allowAgents 权限白名单
- 60+ 内置工具：GitHub、Notion、浏览器、cron、TTS
- Discord 语音频道语音对话（内置语音转文字 + TTS 语音回应）

## 适用场景

- 在 Discord 上以 CEO 身份用对话指挥 AI 团队写代码、管预算、发内容
- 7×24 定时任务：每日站会、成本告警、部署
- 通过语音频道开 AI 团队会议并让 agent 语音汇报

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: > **TL;DR** — Run `bash <(curl -fsSL https://raw.githubusercontent.com/wanikua/become-ceo/main/setup.sh)` on any Li
> L28: - 🤖 **7 specialized AI agents**, each with their own Discord bot, personality, and expertise

## 星数曲线

```mermaid
xychart-beta
    title "wanikua/become-ceo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 62 --> 65
    line [63, 64, 64]
```

2026-10-18 63 → 2026-10-29 64（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d67c273187a7` · [字段定义](../../DATASET.md)*
