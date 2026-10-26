# BinaryBananaLLC/WhipDesk

⭐ 34 · TypeScript · AGPL-3.0 · 推送 2026-10-01 · [GitHub](https://github.com/BinaryBananaLLC/WhipDesk) · [官网](https://WhipDesk.com) · 组织维护

**从手机浏览器远程监控控制开发机上 AI 编码代理的工具**

面向开发者的远程访问工具：在开发机安装 agent，通过手机浏览器端到端加密地查看完整桌面、操控 AI 编码代理（Claude Code、Codex、Cursor 等）、测试改动、审查代码。提供 agent 卡住/完成提醒、定时提示词、提示词库、桌面自动化录制等功能。局域网可直连无需账号；跨网络使用 WhipDesk.com 做设备发现与中继。支持 npm 安装或各平台安装包，macOS 需授予屏幕录制与辅助功能权限，Wayland 需 xdg-desktop-portal。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手机浏览器端到端加密远程控制整台开发机（WebRTC，PIN 配对）
- 自动检测 Claude Code、Codex、Aider 等 8 种代理状态并推送提醒
- 定时提示词、提示词库（Whipository）、桌面自动化（LashStash）
- 局域网直连无需账号与云端依赖，agent 端无分析追踪

## 适用场景

- 离开电脑时用手机查看并控制正在运行的 AI 编码代理
- 定时在会话限额重置时自动发送提示词继续任务
- 把常用的重复指令存成提示词库一键发送
- 代理完成或卡住时收到手机推送通知

## 场景标签

`GUI 自动化` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L16: WhipDesk is a **remote access tool for developers** who need to monitor and control AI coding agents running on the
> L18: The agent you install on your dev machine and the controller that runs in your browser are both open source, and th
> L161: While WhipDesk is built mobile-first and optimized for managing AI agents, it's also useful for general remote acc

## 星数曲线

```mermaid
xychart-beta
    title "BinaryBananaLLC/WhipDesk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-26 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d223a4bdb299` · [字段定义](../../DATASET.md)*
