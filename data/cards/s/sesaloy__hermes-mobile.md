# sesaloy/hermes-mobile

⭐ 50 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/sesaloy/hermes-mobile) · 个人维护

**在 Android 上本地运行 Hermes Agent 的自包含移动应用**

将 Hermes Agent 运行时、本地 Dashboard、Node/TUI 运行时与 ARM64 原生库打包为一个自包含 Android 应用，无需 Termux 或远程服务器即可在手机上运行 Agent。提供移动聊天、会话持久化、文件访问、自动化、集成、记忆、Skills Hub 与模型设置等功能，并以流式卡片展示推理与工具执行过程。当前版本 1.1 处于活跃开发阶段，仅构建 ARM64 debug APK，发布签名与升级迁移尚未完成，仅支持 arm64-v8a 架构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 无需 Termux 或远程服务器，在 Android 上本地运行 Hermes Agent
- 内置 Python、Dashboard、Node/TUI 运行时与 ARM64 原生库
- 移动端聊天、会话持久化、记忆、Skills Hub 与模型设置
- 应用内无线调试页面与 android_debug 工具用于配对设备诊断

## 适用场景

- 在 Android 手机上本地使用 Hermes Agent 进行对话与自动化任务
- 通过手机查看 Agent 的流式推理与工具执行过程
- 在无 Termux 环境的设备上运行与调试 Agent

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Hermes Mobile packages the Hermes Agent runtime, local Dashboard, Node/TUI runtime, and an Android mobile interface 
> L9: - Runs Hermes Agent locally on Android without requiring Termux or a remote server.
> L11: - Provides mobile chat, session persistence, file access, automation, integrations, remote instance status, memory,

## 星数曲线

```mermaid
xychart-beta
    title "sesaloy/hermes-mobile 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 46 --> 51
    line [47, 49, 50]
```

2026-10-18 47 → 2026-10-25 50（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1d2601f17ebd` · [字段定义](../../DATASET.md)*
