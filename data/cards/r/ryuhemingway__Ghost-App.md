# ryuhemingway/Ghost-App

⭐ 19 · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/ryuhemingway/Ghost-App) · [官网](https://integratedagentics.com/ghost) · 个人维护

**macOS 刘海区菜单栏 AI 工作台：八家模型、本地 RAG 与 Mac 自动化**

面向 Mac 个人用户的菜单栏 AI 工作台（⌥Space 唤起）。提示经意图分类后路由到八家提供方（LM Studio、Ollama 本地，Claude、Gemini、DeepSeek、OpenCode、OpenAI 兼容端），或复用 Claude Code/Codex 订阅。功能含本地 SQLite+FTS5 文档检索、纯 Markdown 知识库记忆、原生框架生成 DOCX/PDF 等真实文件、80 个工具四档风险分级与撤销日志、聚合 Claude Code/Codex/opencode 编码 agent 会话。隐私为默认关闭设计，macOS 14+，一次性付费应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八家提供方路由，本地模型同样接入完整工具 harness
- 本地 SQLite+FTS5 索引 30+ 格式文档，无云端嵌入/向量库
- 80 工具分四档风险，六项权限默认关闭，带撤销日志
- 统一管理 Claude Code/Codex/opencode 会话并审批其权限请求

## 适用场景

- 在任意界面按快捷键向本地或云端模型提问、处理文件
- 对本地文档做来源可回溯的问答检索
- 统一监控和审批终端里的编码 agent 及其子 agent

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L15: Every AI tool today has the same problem: you're the one doing all the context switching. ChatGPT tab, local model 
> L45: Ghost routes every prompt through an intent classifier that detects what you're actually trying to do — Answer, Res
> L79: Ghost indexes folders you approve into a local SQLite database with FTS5 full-text search — 3,500-character chunks 

## 星数曲线

```mermaid
xychart-beta
    title "ryuhemingway/Ghost-App 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3757404ac3d6` · [字段定义](../../DATASET.md)*
