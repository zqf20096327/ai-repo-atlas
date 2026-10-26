# klemensgc/modular-context-obsidian-plugin

⭐ 99 · TypeScript · 推送 2026-10-15 · [GitHub](https://github.com/klemensgc/modular-context-obsidian-plugin) · 个人维护

**Obsidian 插件：把 vault 变成 LLM 知识库并暴露 25 个 Google Workspace MCP 工具**

两合一的 Obsidian 插件：其一将 Obsidian vault 按 Sources → Wiki → Schema 结构化为 LLM 可读知识库，内嵌多终端（最多 8 会话）运行 Claude Code 与 Codex，附技能侧栏与 agent 状态跟踪；其二作为多账号 G-Suite MCP 服务器，把 Gmail、Calendar、Drive、Docs、Sheets、Slides 共 25 个工具暴露给 Claude Code，OAuth 2.0 + PKCE 认证，token 经 OS keychain 加密本地存储，零遥测。安装需 Obsidian ≥ 0.15 与 macOS，Linux/Windows 未测试；MCP server 二进制（约 100MB）在首次连接时自动安装。Quick Connect 路径需申请测试用户，BYO 路径需自建 GCP OAuth 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个 MCP 工具覆盖 Gmail/Calendar/Drive/Docs/Sheets/Slides 六个产品，支持无限多账号并行
- vault 结构化为 Sources → Wiki → Schema（Karpathy 式框架），LLM 作为一等上下文读取
- token 经 Electron safeStorage 加密（macOS Keychain / Windows DPAPI / Linux libsecret），零遥测、本地优先
- 多终端布局（最多 8 会话）+ Claude Code / Codex 供应商切换 + 技能侧栏

## 适用场景

- 在 Obsidian 内直接通过 Claude Code 操作 Gmail、日历与 Google 文档
- 把个人笔记 vault 结构化后作为 LLM 的知识上下文
- 多 Google 账号统一接入单一 MCP 服务器进行邮件清扫与日程分析

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L18: 2. **G-Suite MCP Server** — Multi-account Google Workspace (Gmail, Calendar, Drive, Docs, Sheets, Slides) exposed a
> L5: > *Your Obsidian vault as LLM-native knowledge base + multi-account Google Workspace (Gmail, Calendar, Drive, Docs, 

## 星数曲线

```mermaid
xychart-beta
    title "klemensgc/modular-context-obsidian-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 98 --> 100
    line [99, 99]
```

2026-10-18 99 → 2026-10-26 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d5b3eea9f8a3` · [字段定义](../../DATASET.md)*
