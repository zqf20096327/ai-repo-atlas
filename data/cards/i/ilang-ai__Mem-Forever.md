# ilang-ai/Mem-Forever

⭐ 21 · MIT · 推送 2026-09-22 · [GitHub](https://github.com/ilang-ai/Mem-Forever) · [官网](https://ilang.ai) · 个人维护 · 中文 README

**面向 AI 编程工具的 Git 原生持久记忆模板仓库**

以 GitHub 模板仓库形式提供的 AI agent 记忆层：用户 fork 模板创建私有仓库，AI 工具读取仓库内指令文件与 .ilang/ 目录下的 soul.md（行为画像）和 memory.md（决策日志），从对话中自动抽取偏好并持续更新，实现跨会话、跨工具的持久记忆。兼容 Claude Code、Cursor、Codex、Copilot、Gemini CLI 等通过文件读取配置的工具，网页端 ChatGPT/Claude 可上传 soul.md。指令文件基于 iLang v4.0 协议，数据存储在用户自己的仓库，无服务器与遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fork 模板仓库即用，零安装零配置
- soul.md 画像 + memory.md 追加式日志的 Git 原生存储
- 兼容 Claude Code/Cursor/Codex/Copilot/Gemini CLI 等工具的自动读取
- 指令规则基于 iLang v4.0 协议，支持多变体与衰减规则

## 适用场景

- 让 Claude Code、Cursor 等编程助手跨会话记住我的偏好与项目决策
- 多个项目分别维护独立的记忆仓库
- 在网页版 ChatGPT/Claude 中上传 soul.md 延续个人画像

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L23: > A persistent memory layer for AI agents, built on the iLang protocol.
> L39: **Mem-Forever** is a Git-native memory layer that lets any AI agent remember you permanently. Memories are stored a
> L79: |Tool|Auto-reads|How|

## 星数曲线

```mermaid
xychart-beta
    title "ilang-ai/Mem-Forever 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `87800c9f18bb` · [字段定义](../../DATASET.md)*
