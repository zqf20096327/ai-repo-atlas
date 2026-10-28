# chyra-moon/deepseek-harness-desktop

⭐ 19 · JavaScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/chyra-moon/deepseek-harness-desktop) · 个人维护 · 中文 README

**DeepSeek Harness 的 Windows 桌面适配壳：Electron 加载官方 Web 界面**

社区维护的 Electron 桌面应用，将 DeepSeek Harness 的官方 Web 前端包装为 Windows x64 桌面程序，并把本地 dsh 服务的启动、连接与恢复整合进应用：自动探测本机 3080 端口、识别已有服务后复用（与浏览器共享同一实例与会话数据）、异常时尝试恢复并重载页面。桌面层还提供托盘驻留、窗口位置记忆、单实例运行与可配置的自动更新。安装包内置运行时与官方 dsh 服务，无需另装 Node.js。面向希望以桌面方式使用 Harness 的 Windows 用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Electron 加载官方 Web 前端，内置官方 dsh 服务，无需另装 Node.js
- 自动探测/复用本机 3080 端口的已有 dsh 服务，与浏览器共享会话数据
- 托盘驻留、单实例运行、窗口位置记忆与连接异常自动恢复
- 提供安装版/解压版/单文件便携版三种发行形式

## 适用场景

- 在 Windows 桌面常驻使用 DeepSeek Harness 工作区
- 与浏览器共用同一 dsh 服务实例
- 免命令行启动本地 Harness 服务

## 场景标签

 · 领域:桌面工具/AI 应用客户端

## 证据(README 行号)

> L21: **DeepSeek Harness Desktop** 是 DeepSeek Harness 的 Windows 桌面适配版。项目使用 Electron 加载官方 Web 前端，将本地服务的启动、连接与恢复整合进桌面应用，让你从
> L23: 安装包包含运行时与官方 dsh 服务，日常启动无需另行安装 Node.js 或输入命令。桌面适配层提供窗口管理、托盘驻留和连接恢复等能力；Harness 的核心功能与工作流程由内置的官方 dsh 提供。

## 星数曲线

```mermaid
xychart-beta
    title "chyra-moon/deepseek-harness-desktop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `98b5d6448760` · [字段定义](../../DATASET.md)*
