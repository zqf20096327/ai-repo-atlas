# chara-codes/chara

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-06-10 · [GitHub](https://github.com/chara-codes/chara) · 组织维护

**面向前端开发的 AI 开发环境，聚合多模型编码助手**

Chara Codes 是一个 AI 驱动的开发环境，面向前端开发者，提供网页版分栏聊天/预览界面、实时代码编辑、进程管理与隧道分享。核心机制：接入 9+ AI 提供商（OpenAI、Anthropic、DeepSeek、Ollama、LM Studio 等）、MCP 协议集成、15+ 内置工具（文件操作、终端执行、代码分析），以及可嵌入任意网页的 AI Widget 模式（点击选取页面元素作为上下文获得代码建议）。以 npm CLI 全局安装为主，monorepo 含 8+ 包，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 9+ AI 提供商，含 Ollama/LM Studio 本地模型运行
- MCP 协议集成：自动发现 MCP 服务器，支持 resources/tools/prompts/sampling
- AI Widget 模式：选取页面 DOM 元素作为上下文获取代码生成与调试建议
- monorepo 结构，含 CLI/server/agents/web/widget 等 8+ 包

## 适用场景

- 在前端开发中通过对话界面获得代码生成与调试帮助
- 在网页内选取 UI 元素直接获取样式修改或代码生成建议
- 通过隧道向他人分享本地开发环境演示

## 场景标签

`编码 Agent` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L17: The platform combines multiple AI providers, Model Context Protocol (MCP) integration, real-time collaboration, and
> L22: - Support for 9+ AI providers (OpenAI, Anthropic, Google, DeepSeek, Ollama, and more)
> L54: - Embeddable AI coding agent that integrates into any webpage

## 星数曲线

```mermaid
xychart-beta
    title "chara-codes/chara 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `11ad8e786d7a` · [字段定义](../../DATASET.md)*
