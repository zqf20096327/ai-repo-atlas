# huggingface/huggingface.js

⭐ 2,616 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/huggingface/huggingface.js) · [官网](https://hf.co/docs/huggingface.js) · 组织维护

**面向 JS 开发者的 Hugging Face API 客户端库集合**

一组带 TypeScript 类型的 JavaScript 库，用于与 Hugging Face API 交互：@huggingface/hub 创建/删除仓库、提交与下载文件；@huggingface/inference 通过 Inference Providers 或专用 Inference Endpoints 调用 100,000+ 机器学习模型；另有 MCP 客户端、GGUF/DDUF 解析器、LeRobot 数据集读取、Jinja 模板、tiny-agents 等 12 个子包。运行环境要求现代浏览器或 Node.js >= 18 / Bun / Deno，通过 NPM 或 CDN 导入使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个子包覆盖 Hub 仓库管理与推理调用
- @huggingface/inference 支持 serverless Inference Providers 与专用 Inference Endpoints
- 内置 TS 类型，支持浏览器/Node.js>=18/Bun/Deno
- 提供 MCP 客户端与模型无关的 tiny-agents 库

## 适用场景

- 在 JS 应用中上传/下载模型与数据集文件
- 从浏览器或 Node 调用 Hugging Face 托管的推理模型
- 构建可使用工具的 AI agent（mcp-client / tiny-agents）

## 场景标签

 · 领域:AI 基础设施/SDK

## 证据(README 行号)

> L12: This is a collection of JS libraries to interact with the Hugging Face API, with TS types included.
> L15: - @huggingface/inference: Use all supported (serverless) Inference Providers or switch to Inference Endpoints (dedi

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/huggingface.js 星数(近 22 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 2576 --> 2620
    line [2581, 2584, 2586, 2587, 2588, 2589, 2591, 2593, 2579, 2602, 2605, 2607, 2608, 2609, 2612, 2611, 2612, 2613, 2615, 2616, 2617, 2616]
```

2026-10-26 2,581 → 2026-11-28 2,616（+35）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a09b8538f199` · [字段定义](../../DATASET.md)*
