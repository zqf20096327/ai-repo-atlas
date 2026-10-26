# dakshjain-1616/Qwen-Lens-Studio

⭐ 29 · TypeScript · 推送 2026-04-23 · [GitHub](https://github.com/dakshjain-1616/Qwen-Lens-Studio) · [官网](https://heyneo.com) · 个人维护

**多模态视觉 AI 工作台：截图转代码、票据转 JSON、图文对比**

围绕单个 Qwen 视觉语言模型构建的 Web 应用，React+Vite 前端与 FastAPI 后端，经 OpenRouter/Ollama/llama.cpp 调用模型。提供五个流式工具：视觉推理问答、多语言图像描述、发票/证件结构化 JSON 提取、UI 截图转 HTML/React/Vue/Svelte 代码、双图差异对比。附批量运行器（3 并发、CSV/JSON 导出）、localStorage 会话历史、提示模板库与逐请求 API key 覆盖；MOCK_MODE 可无 key 演示。无数据库，API key 存于浏览器 localStorage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个流式视觉工具：推理/描述/文档提取/截图转代码/双图对比
- 批量运行器：3 worker 队列，结果导出 CSV/JSON（JSON 键自动展平为列）
- 后端可插拔：OpenRouter/Ollama/llama.cpp 三种推理后端，逐请求覆盖 key/模型
- MOCK_MODE 无模型流式返回固定文本，供离线演示与 CI

## 适用场景

- 上传发票或证件图片提取结构化 JSON
- 把 UI 截图转成可预览的 HTML/React/Vue/Svelte 代码
- 对两张图片提问并获得结构化的异同对比

## 场景标签

`多模态` `文档解析` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A multimodal AI studio built around a single Qwen vision-language model, exposed through five focused tools plus a b
> L31: React + Vite + TypeScript SPA  ──►  FastAPI backend  ──►  Qwen via OpenRouter / Ollama / llama.cpp

## 星数曲线

```mermaid
xychart-beta
    title "dakshjain-1616/Qwen-Lens-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `333180356ca0` · [字段定义](../../DATASET.md)*
