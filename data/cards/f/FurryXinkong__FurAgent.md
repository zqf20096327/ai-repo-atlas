# FurryXinkong/FurAgent

⭐ 4 · Kotlin · Apache-2.0 · 推送 2026-11-15 · [GitHub](https://github.com/FurryXinkong/FurAgent) · 个人维护 · 中文 README

**跑在自有设备上的双端 Tool-Using Agent（Android+Windows）**

基于 Kotlin Multiplatform 的本地优先 Agent：通过用户自备的 OpenAI 兼容 API Key 直连大模型，可调用系统 API 操作手机与电脑。提供分层工具系统（tool_search/tool_load 动态加载）、最多 4 个并行子代理、cron/环境条件触发的定时任务、跨会话长期记忆与行级 patch 回档。Android 端经无障碍服务与 Shizuku 操作屏幕 UI，桌面端用 UIA 控制窗口并本地生成 Word/Excel/PPT；两端可经局域网互调工具与传文件。Android 需 11+/arm64，Windows 端内嵌 JRE；作者声明为自用项目，不按生产级预期维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- BYOK 模式直连 OpenAI 兼容接口，会话/记忆/配置全部本地存储
- 分层工具系统与最多 4 个并行子代理
- Android 无障碍服务+Shizuku、Windows UIA 的平台深度集成
- 局域网双端互联、文件流式传输与 Wake-on-LAN 唤醒

## 适用场景

- 在手机/电脑上运行本地优先的工具调用 Agent
- 让 Agent 自动操作 Android 屏幕 UI 或 Windows 窗口
- 手机远程唤醒并控制局域网内电脑执行任务
- 用 cron 与电量/网络条件触发自动化工作流

## 场景标签

`工作流自动化` `AI 助手` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: FurAgent 是一个基于 Kotlin Multiplatform (KMP) 开发的、跑在你自己设备上的 Tool-Using Agent。它不只停留在对话层面，而是能实际调用系统 API 操作你的手机和电脑。
> L13: 它不依赖云端沙盒：所有推理通过你自己的 API Key 直连大模型，所有数据（会话、记忆、配置、文件）都完全存储在你的本地设备上。
> L31: - **Android**：基于无障碍服务 (Accessibility Service) 直接读取与操作屏幕 UI 树；通过 Shizuku 调用 ADB 级权限；媒体播放控制与通知捕获。

## 星数曲线

```mermaid
xychart-beta
    title "FurryXinkong/FurAgent 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-29 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `359d71e3186a` · [字段定义](../../DATASET.md)*
