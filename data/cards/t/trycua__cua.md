# trycua/cua

⭐ 30,105 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/trycua/cua) · [官网](https://cua.ai) · 组织维护

**给 AI agent 提供可操作的完整桌面环境与自动化工具**

Cua 是一套面向 computer-use agent 的基础设施：Cua Spaces 提供运行于自有 Mac/机器/云账号上的 macOS 与 Linux 桌面 Space，支持应用 Teleport 与人机多人协作；Cua Driver 提供 CLI/MCP/多语言 SDK 驱动 macOS、Windows、Linux 原生应用与浏览器；Lume 基于 Virtualization.Framework 在 Apple Silicon 上管理本地 VM；另含 CUA-S1 小型决策模型（研究发布，权重在 Hugging Face）与 Cua Bench 任务评测框架。主体 MIT 许可，Spaces 与部分 Bench 为 FSL-1.1-MIT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 100,149 位贡献者
- 涨星:近 1 天 **+107**(自 20261016 起算)
- 安装:pypi 包 `cua` 月下载 11,861
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP

## 能力要点

- Cua Driver 支持 macOS/Windows/Linux 桌面自动化，经 CLI、MCP 或类型化 SDK 接入
- Lume 用 Apple Virtualization.Framework 在 Apple Silicon 上管理 macOS/Linux VM
- SDK 覆盖 Python/TypeScript/Swift/Kotlin，含 gVisor 容器沙箱与 cua-spacesd 守护进程
- Cua Bench 可构建任务、评测 agent 并导出训练轨迹

## 适用场景

- 让 agent 在隔离虚拟桌面中操作图形界面完成任务
- 为 computer-use agent 构建评测任务并导出轨迹用于训练
- 在自有 Mac 或云主机上托管供 agent 使用的桌面环境

## 场景标签

`GUI 自动化` `模型评测` · 领域:效率与自动化

## 证据(README 行号)

> L7:  Give AI agents computers they can use. Cua Spaces gives your agents full desktops on your Mac and on machines you o
> L69: Give your agent tools to inspect and operate native desktop apps and browsers on macOS, Windows, and Linux. Connect
> L141: - **SDK:** the same API in Python (`pip install cua`), TypeScript (`@trycua/cua`), Swift (`Cua`) and Kotlin (gener

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `4b8978a2bc24` · [字段定义](../../DATASET.md)*
