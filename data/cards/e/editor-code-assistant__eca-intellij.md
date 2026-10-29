# editor-code-assistant/eca-intellij

⭐ 19 · Clojure · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/editor-code-assistant/eca-intellij) · [官网](https://plugins.jetbrains.com/plugin/28289-eca) · 组织维护

**为 IntelliJ 接入 ECA 的 AI 结对编程插件客户端**

JetBrains 平台插件，作为 Editor Code Assistant (ECA) 的 IntelliJ 客户端：连接外部 eca 服务器进程，提供交互式聊天、代码建议与上下文管理等功能。插件自身会自动下载并管理 eca 进程；详细功能与配置在 ECA 服务端文档中说明。用户通过 JetBrains Marketplace 安装 ECA 插件，设置入口位于 Preferences > Tools > ECA。开发者可用 bb 命令本地构建 webview 与插件 zip 并安装到本地 IntelliJ。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接外部 eca 服务器进程提供聊天、代码建议与上下文管理
- 自动下载并管理 eca 进程
- 通过 JetBrains Marketplace 安装
- 提供 bb 命令的本地开发与生产构建流程

## 适用场景

- 在 IntelliJ 中使用 ECA 进行 AI 结对编程
- 开发者本地构建并调试插件 webview

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: ECA (Editor Code Assistant) IntelliJ is an AI-powered pair-programming client for IntelliJ.
> L10: It connects to an external `eca` server process to provide interactive chat, code suggestions, context management a

## 星数曲线

```mermaid
xychart-beta
    title "editor-code-assistant/eca-intellij 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7a0a06630450` · [字段定义](../../DATASET.md)*
