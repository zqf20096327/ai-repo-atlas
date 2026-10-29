# nomie7/nano-banana-slides-prompter

⭐ 70 · TypeScript · GPL-3.0 · 推送 2026-01-10 · [GitHub](https://github.com/nomie7/nano-banana-slides-prompter) · [官网](https://slides.jo3.ai) · 个人维护 · 中文 README

**为 Nano Banana Pro Slides 生成优化 AI 提示词的 Web 应用**

前后端分离的 Web 应用：用户输入内容或上传 CSV/URL，由可配置的 LLM 后端分析内容，从 50+ 模板中选择幻灯片类型，并生成含动态角色（8 种渲染风格、24 种组合）、24 类视觉风格与 200+ 视觉词库的提示词，用于 Nano Banana Pro Slides 生成幻灯片。前端 React/TypeScript，后端 Bun+Hono，支持 OpenAI/OpenRouter/Ollama 等 OpenAI 兼容后端；提供中英双语界面、会话管理、Docker Compose 部署与 GHCR 预构建镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 分析内容并从 50+ 模板中选择幻灯片类型
- 动态角色生成：8 种渲染风格、24 种组合、支持非人类角色
- 可配置 LLM 后端（OpenAI/OpenRouter/Ollama 等），用户可在浏览器内覆盖 API 配置
- 中英双语界面与多会话保存管理

## 适用场景

- 为 Nano Banana Pro Slides 批量生成幻灯片提示词
- 上传 CSV 数据生成数据驱动的演示文稿提示词
- 从 URL 提取内容自动生成演示结构与视觉风格提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Generate optimized prompts for Nano Banana Pro Slides - Generate slides using AI.
> L13: - 🧠 **Content-Aware Slide Types** - LLM analyzes your content and selects optimal slide types from 50+ templates
> L136: - Configurable LLM backend (OpenAI, OpenRouter, Ollama, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "nomie7/nano-banana-slides-prompter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-29 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b28f88d6b93c` · [字段定义](../../DATASET.md)*
