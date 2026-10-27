# iovdin/tune

⭐ 29 · JavaScript · 推送 2026-10-26 · [GitHub](https://github.com/iovdin/tune) · 个人维护

**在文本文件中与 LLM 对话的工具与 JS SDK**

Tune 以 VSCode 扩展及 Neovim/Sublime 插件形式提供，让用户在纯文本文件中与大型语言模型对话：文件内用 @name 模板语法引用提示、图像与模型，通过中间件扩展能力（本地文件系统、S3、MCP 工具、多家模型提供商等）。核心为中间件式架构，上下文将 @name 引用解析为 text/tool/llm/processor 节点。附带 tune-sdk JavaScript SDK 用于构建应用与 agent，并提供静态 Web 服务器与 WebSocket 共享上下文，可制作复用 Tune 工具与模型的简单 Web 应用。

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

- 在文本文件中与 LLM 对话，@name 模板语法引用文件/图像/模型
- 中间件架构：tune-fs、tune-models、tune-mcp、tune-s3 等可组合扩展
- tune-sdk JavaScript SDK 可构建应用与 agent
- 静态 Web 服务器 + WebSocket，Web 应用与 Tune Chat 共享同一上下文

## 适用场景

- 在编辑器内以纯文本文件方式撰写提示并与 LLM 对话
- 通过中间件把本地文件、S3、MCP 工具接入对话上下文
- 用 JS SDK 基于同一中间件体系构建应用和 agent

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Tune is a handy extension for Visual Studio Code and and plugin for Neovim and plugin for Sublime Text that lets you
> L111: Tune core is middleware-based. A context resolves `@name` references into nodes like `text`, `tool`, `llm`, and `p

## 星数曲线

```mermaid
xychart-beta
    title "iovdin/tune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e20d600c0a9f` · [字段定义](../../DATASET.md)*
