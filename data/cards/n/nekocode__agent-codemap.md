# nekocode/agent-codemap

⭐ 15 · Rust · 推送 2026-02-16 · [GitHub](https://github.com/nekocode/agent-codemap) · 个人维护 · 中文 README

**为 LLM/Agent 生成源码符号索引的代码地图工具**

CLI 工具，从源码文件中抽取类、方法、函数、变量等符号及行号，输出结构化 Markdown 或 JSON 作为 LLM 上下文。支持 Python、TypeScript、Go、Rust、Java 等 14 种语言，可提取嵌套符号（类内方法等），自动遵循 .gitignore，输出到 stdout 便于管道组合。面向在代码库上工作的 AI Agent 用户：可直接在提示中让 Agent 调用，或通过 AGENTS.md/CLAUDE.md 固化使用约定。npm 全局安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抽取符号及行号，支持 14 种语言的嵌套符号提取
- 输出 Markdown 与 JSON 两种格式，stdout 管道友好
- 自动遵循 .gitignore
- 提供 AGENTS.md/CLAUDE.md 集成写法

## 适用场景

- 让 AI Agent 快速理解陌生代码库结构
- 为 LLM 提供精简的代码符号索引上下文
- 在项目说明中固化代码索引工具的使用约定

## 场景标签

 · 领域:开发工具/LLM 基础设施

## 证据(README 行号)

> L5: AI-friendly source code index generator. Extracts symbols from source files and outputs structured Markdown for LLM 
> L76: ## Usage with AI Agents

## 星数曲线

```mermaid
xychart-beta
    title "nekocode/agent-codemap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cc629c2a1146` · [字段定义](../../DATASET.md)*
