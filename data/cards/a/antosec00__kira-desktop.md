# antosec00/kira-desktop

⭐ 4 · Python · MIT · 推送 2026-11-21 · [GitHub](https://github.com/antosec00/kira-desktop) · 个人维护

**本地桌面工作台：为已有 AI 模型提供项目、工具与权限管理**

基于 PySide6 的桌面应用（Linux deb 包、Windows 安装包、源码运行），为用户自选的本地或云端模型提供持久化工作空间：命名项目与聊天、带凭据回执的可审计工具调用、隔离浏览器、多 agent 团队、研究记录与跨项目搜索（Omnibox）。数据存于本地 SQLite 与私有目录，权限按项目分级（只读到完全访问）。通过 Models 面板按聊天切换 8 个提供方，支持 WSL2 运行；Claude Code 为可选扩展，不在安装包内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次工具调用留下可核验的执行回执
- 8 个本地与云端提供方，按聊天切换且不丢对话
- 隔离浏览器与多 agent 团队（可暂停/恢复）
- 项目级权限分级，数据保留在本机

## 适用场景

- 在本地管理多个 AI 提供方并按项目组织对话
- 让 agent 执行读写、命令与浏览操作并审计每一步
- 本地 Ollama 模型搭配工具调用的桌面使用

## 场景标签

`AI 助手` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  The desktop application that amplifies the AI models you already use.
> L43: - **Bring your own model.** Ollama on your computer, OpenAI Codex, your ChatGPT
> L88: |**Ollama**|Local HTTP API (`http://127.0.0.1:11434` by default)|Kira; tools verified on first use, no automatic mo

## 星数曲线

```mermaid
xychart-beta
    title "antosec00/kira-desktop 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-11-08", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-30 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `dbbf8b599e9d` · [字段定义](../../DATASET.md)*
