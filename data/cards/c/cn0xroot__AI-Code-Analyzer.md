# cn0xroot/AI-Code-Analyzer

⭐ 25 · Vue · 推送 2026-09-20 · [GitHub](https://github.com/cn0xroot/AI-Code-Analyzer) · [官网](https://www.sistudiohq.com) · 个人维护 · 中文 README

**AI 驱动的代码分析系统：生成项目摘要与 Mermaid 架构图**

面向开发者的自部署 Web 应用：从 GitHub/GitLab/Gitee 克隆或上传代码，经 tree-sitter 解析多语言 AST，调用 OpenAI、Anthropic、通义千问或 OpenAI 兼容接口，生成项目概述、函数分析、逻辑流程等维度的报告与 Mermaid 图表（架构图/类图/时序图等），SSE 实时流式输出，SQLite 持久化历史。前后端分离（FastAPI + Vue 3），需分别安装 Python 与 npm 依赖并配置 API Key 后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter 解析 10+ 语言（语言包支持 305+）
- 支持 OpenAI/Anthropic/通义千问/OpenAI 兼容四种 AI 提供方
- SSE 流式输出 + Markdown/Mermaid 实时渲染
- SQLite 历史持久化与任务超时/僵尸任务恢复

## 适用场景

- 克隆或上传代码仓库，让 AI 生成项目摘要与架构图
- 快速理解陌生项目的函数结构、调用关系与执行逻辑
- 将分析结果导出为文档或 SVG 图表用于汇报

## 场景标签

 · 领域:开发者工具/代码智能

## 证据(README 行号)

> L3: An intelligent code analysis system powered by AI large language models that automatically generates project summari
> L11: - **Multiple AI Providers**: OpenAI, Anthropic (Claude), Alibaba Qwen, OpenAI-compatible services
> L216: ## Supported AI Providers

## 星数曲线

```mermaid
xychart-beta
    title "cn0xroot/AI-Code-Analyzer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [26, 25, 25]
```

2026-10-18 26 → 2026-10-30 25（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3f3b487f411f` · [字段定义](../../DATASET.md)*
