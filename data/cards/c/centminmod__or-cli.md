# centminmod/or-cli

⭐ 21 · 推送 2025-12-28 · [GitHub](https://github.com/centminmod/or-cli) · 个人维护

**通过 OpenRouter/Cloudflare/Ollama 调用 AI 模型的命令行工具**

单文件 Python 命令行工具 or-cli.py，通过四条路径与 LLM 交互：OpenRouter 直接 API、经 Cloudflare AI Gateway 的代理缓存、Cloudflare Workers AI、以及本地 Ollama（含 --ollama/--vllm 参数）。面向命令行文本处理场景，功能含多模态输入、网页转 Markdown（支持 JS 渲染）、PDF 提取（py-zerox）、多模型对比/互评（--multi/--eval）、OpenAI 兼容 tool calling、LinkUP/Brave 联网搜索与 txtai RAG 存储、可选 Microsoft LLMLingua 提示压缩。配置依赖 API key 环境变量与多个 pip 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四条调用路径：OpenRouter 直连、Cloudflare AI Gateway 代理、Cloudflare Workers AI、本地 Ollama
- 多模型对比与互评模式（--multi/--eval）
- 网页/PDF 提取、联网搜索与 txtai RAG 向量库存储
- 可选 Microsoft LLMLingua 提示压缩与 Opik 追踪

## 适用场景

- 在命令行批量调用 LLM 做文本摘要与转换
- 对比多个模型的回答或让模型互评
- 将网页/PDF 内容提取后交给模型处理并存入 RAG 库

## 场景标签

`RAG` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A versatile Python command-line tool for interacting with AI models through the OpenRouter API, supporting direct AP
> L13: `or-cli.py` is a powerful command-line interface (CLI) tool designed to communicate with AI language models through
> L18: 4. **Local Ollama API** for on-premise model inference - <https://ollama.com> and use self-hosted LLM models from H

## 星数曲线

```mermaid
xychart-beta
    title "centminmod/or-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7a6cd5984e17` · [字段定义](../../DATASET.md)*
