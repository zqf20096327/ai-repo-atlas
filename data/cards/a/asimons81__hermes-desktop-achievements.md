# asimons81/hermes-desktop-achievements

⭐ 16 · JavaScript · MIT · 推送 2026-08-06 · [GitHub](https://github.com/asimons81/hermes-desktop-achievements) · 个人维护

**Hermes Agent 桌面端的成就系统插件：成就页、状态栏积分与解锁通知**

面向 Hermes Agent 桌面应用（v0.19+）的桌面插件，提供完整成就页面（积分头、分层筛选、进度条、重扫）、侧边栏入口、状态栏实时积分条与 ⌘K 命令。通过插件 API 轮询（每 15 秒）现有 hermes-achievements 后端插件的 /achievements 接口做解锁检测，不新增后端。含解锁通知（toast/音效/彩带）、Discord webhook 公告、自定义徽章、Markdown/JSON 导出与分享图生成。安装方式为将 plugin.js 复制到 ~/.hermes/desktop-plugins/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 成就页含积分头、分层筛选、进度条、解锁时间线与每周统计
- 解锁通知：toast、触觉反馈、音效与彩带，Gold 及以上有号角音效
- 每 15 秒轮询插件 API 检测解锁，基线持久化避免重启后重放
- 自定义成就、Markdown/JSON 导出、1200×630 分享图生成

## 适用场景

- 在 Hermes 桌面端追踪并展示我的 Agent 使用成就
- 解锁成就时收到通知并同步到 Discord 服务器
- 定义个人自定义徽章并导出成就记录

## 场景标签

 · 领域:AI Agent 桌面应用/插件

## 证据(README 行号)

> L7: by the `hermes-achievements` dashboard plugin that ships with Hermes Agent.
> L48: 1. **Backend (required):** the Hermes Agent install already ships

## 星数曲线

```mermaid
xychart-beta
    title "asimons81/hermes-desktop-achievements 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4b2c2ffb1b3d` · [字段定义](../../DATASET.md)*
