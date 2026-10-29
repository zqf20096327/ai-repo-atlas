# syndicalt/llmff

⭐ 46 · Rust · 推送 2026-07-07 · [GitHub](https://github.com/syndicalt/llmff) · 个人维护

**声明式 YAML 的 LLM 推理流水线 CLI，可离线对接 Ollama/OpenAI 兼容服务**

Rust 编写的命令行与库工具，把 LLM 推理流程表达为 FFmpeg 风格的类型化流水线图：用 YAML manifest 或内联图语法声明 load/retrieve/rerank/infer/repair/write 等阶段，按依赖序执行，输出 JSONL trace、inspect 校验报告与稳定退出码。内置 OpenAI 兼容后端（/v1/chat/completions）与 Ollama 接入（--ollama），提供确定性 mock 后端用于离线测试，支持插件扩展 stage/backend/tool transport。面向需要可复现、可检查 LLM 流水线的开发者和 CI 场景；通过 cargo 安装，非原生推理内核或 agent 框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML manifest 与内联图语法声明类型化流水线，inspect 支持干跑校验
- OpenAI 兼容后端与 --ollama 本地后端适配，含确定性 mock 模型
- JSONL trace/事件流、JSON 校验修复、稳定退出码
- 插件机制扩展 stage、backend、tool transport 与采样器

## 适用场景

- 以声明式 YAML 构建 CI 中可复现的 LLM 推理流水线
- 离线对接本地 Ollama 或任意 OpenAI 兼容服务运行推理
- 本地文档检索（lexical/embedding 策略）嵌入流水线

## 场景标签

`RAG` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: `llmff` is an FFmpeg-shaped command-line and library tool for LLM inference pipelines. llmff focuses on a typed pipe
> L129: - `llmff run <manifest>` executes a pipeline manifest.
> L141: - An OpenAI-compatible backend exists in the core crate for `/v1/chat/completions` servers.

## 星数曲线

```mermaid
xychart-beta
    title "syndicalt/llmff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-29 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0a1f5cdd0a90` · [字段定义](../../DATASET.md)*
