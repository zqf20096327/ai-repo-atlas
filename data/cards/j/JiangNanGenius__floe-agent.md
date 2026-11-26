# JiangNanGenius/floe-agent

⭐ 489 · Swift · MPL-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/JiangNanGenius/floe-agent) · [官网](https://www.floe-agent.com/) · 个人维护 · 中文 README

**面向 iPadOS 的开源设备端 AI 工作台与 Agent 应用**

Floe Agent 是覆盖 iOS/iPadOS/Android/Mac 的开源 AI Agent 应用，核心是设备端持久 Linux 环境，可在任务中运行 shell、Python、Node、Git 与本地 Web 服务，并聚合笔记、Office 编辑、2D/3D 建模、画布媒体、语音会议与 Skill Hub 等工作台。AI 采用 BYOK：用户配置自己的云厂商 API key，iOS/iPadOS 可使用 Apple 系统模型或下载的本地模型（Beta），Android 目前仅用云厂商。通过 App Store、TestFlight、GitHub IPA 与 Android Full APK 分发，支持从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端持久 Linux 环境，任务内可运行 shell/Python/Node/Git
- BYOK 接入自有云模型，iOS 支持系统模型与下载的本地模型（Beta）
- 工作台覆盖 Notes/Office、2D/3D、画布媒体、语音与会议转写、Skill Hub/MCP
- 提供 App Store、TestFlight、GitHub IPA、Android APK 多渠道分发

## 适用场景

- 在 iPad 上用 Apple Pencil 完成 3D/绘图与文档处理并叠加 AI 助手
- BYOK 方式在设备端跑自己的模型处理文档与代码任务
- 移动设备上完成语音会议转写与笔记整理
- 通过 Skill Hub 管理技能与 MCP 自动化服务

## 场景标签

`AI 助手` `知识库管理` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L3:  An on-device AI workspace for iOS, iPadOS and Android.
> L63: For AI, connect your own cloud provider using an API key (**BYOK: bring your own key**). Supported iOS/iPadOS devic

## 星数曲线

```mermaid
xychart-beta
    title "JiangNanGenius/floe-agent 星数(近 21 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 287 --> 507
    line [305, 315, 326, 338, 355, 363, 374, 386, 392, 410, 315, 448, 452, 454, 455, 456, 457, 458, 461, 477, 489]
```

2026-10-24 305 → 2026-11-26 489（+184）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c951739c9c51` · [字段定义](../../DATASET.md)*
