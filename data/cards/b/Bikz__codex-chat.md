# Bikz/codex-chat

⭐ 32 · Swift · MIT · 推送 2026-06-08 · [GitHub](https://github.com/Bikz/codex-chat) · 个人维护

**macOS 原生 SwiftUI Codex 客户端，本地 Markdown 对话记录**

基于 SwiftUI 的 macOS 桌面应用，作为本地 codex 运行时（codex app-server）的图形客户端：以对话为核心操作真实项目文件夹，对话与项目上下文以本地可编辑 Markdown 文件存储。提供 Skills 与 Mods 的工作流自动化和 UI 定制、内置多 shell 终端工作区、沙箱/审批策略/网络访问等显式安全控制，API 密钥经 Keychain 管理。要求 macOS 14+ Apple Silicon 与本地 codex CLI（验证窗口 codex 0.114.x），通过签名 DMG 发布，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话持久化为本地自有 Markdown 文件
- Skills 与 Mods 支持工作流自动化与 UI 定制
- 沙箱、审批策略、网络访问等显式安全控制
- Keychain 管理 API 密钥，内置多 shell 终端工作区

## 适用场景

- 在原生 macOS 应用中通过对话驱动 Codex agent 操作项目
- 以本地 Markdown 文件保留和编辑对话历史
- 在受控沙箱与审批策略下运行 agent 工作流

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: CodexChat is an open-source, local-first, macOS-native Codex client built with SwiftUI.
> L4: It integrates with the local `codex app-server` runtime and is designed for safe, reviewable agent workflows against
> L17: - Requires a local `codex` CLI install with `codex app-server` available on `PATH`

## 星数曲线

```mermaid
xychart-beta
    title "Bikz/codex-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-31 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3fd6e65b608a` · [字段定义](../../DATASET.md)*
