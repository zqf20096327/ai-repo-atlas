# hekmon/comfyui-openai-api

⭐ 54 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/hekmon/comfyui-openai-api) · [官网](https://registry.comfy.org/nodes/openai-api) · 个人维护

**ComfyUI 节点：通过 OpenAI API 标准调用 LLM 与 VLM**

面向 ComfyUI 的自定义节点集合，仅实现 chat completions 端点（含视觉支持），使 LLM/VLM 可接入 ComfyUI 工作流。默认 base_url 指向官方 OpenAI 端点，可改为任意 OpenAI 兼容服务器（Ollama、vLLM、SGLang 等）。API key 从 OPENAI_API_KEY 环境变量在执行时读取，禁止在工作流内输入以防随图片元数据泄露。支持批量图像输入与 seed/temperature 等请求参数链式定制。仅 1 个外部依赖（openai 库）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅实现 chat completions 端点（含视觉），1 个外部依赖
- 通过改 base_url 兼容 Ollama/vLLM/SGLang 等 OpenAI 兼容服务器
- API key 仅从环境变量读取，避免随 ComfyUI 元数据泄露
- Extra body 节点可注入任意请求键值对

## 适用场景

- 在 ComfyUI 工作流中调用 LLM/VLM 处理文本或批量图像
- 接入本地 Ollama/vLLM 等兼容服务器做推理
- 用预设节点调整 temperature/max_tokens 等生成参数

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository contains ComfyUI nodes that integrates with the OpenAI API: it allows you to use language models and
> L15: The default `base_url` parameter value targets the official OpenAI API endpoint by default but by changing it, you 

## 星数曲线

```mermaid
xychart-beta
    title "hekmon/comfyui-openai-api 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27", "2026-10-28"]
    y-axis "stars" 50 --> 55
    line [51, 52, 54, 54]
```

2026-10-18 51 → 2026-10-28 54（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3461ef4e4057` · [字段定义](../../DATASET.md)*
