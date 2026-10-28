# docusealco/rllama

⭐ 105 · Ruby · MIT · 推送 2026-07-19 · [GitHub](https://github.com/docusealco/rllama) · [官网](https://www.docuseal.com/blog/run-open-source-llms-locally-with-ruby) · 组织维护

**Ruby 的 llama.cpp 绑定：本地运行开源 LLM 做生成与嵌入**

通过 Ruby FFI 封装 llama.cpp，使 Ruby 应用可直接加载 GGUF 格式的开源模型（Gemma、Qwen、GLM、Llama 等）进行本地推理。提供文本生成（支持流式、system prompt、多轮对话、函数调用、推理阶段输出）、文本嵌入生成（默认归一化）能力；采样参数默认取自模型 GGUF 元数据。附带 rllama 命令行交互聊天工具，可从 Hugging Face 下载模型。以 Ruby gem 形式安装，MIT 许可。

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

- FFI 绑定 llama.cpp，Ruby 内本地运行 GGUF 模型
- 支持流式生成、函数调用（OpenAI 消息格式）与推理内容解析
- 生成向量嵌入，默认归一化
- rllama CLI 交互聊天，自动从 Hugging Face 下载模型

## 适用场景

- 在 Ruby/Rails 应用中集成本地 LLM 推理，不依赖外部 API
- 用 Ruby 生成文本嵌入向量
- 命令行直接与本地 GGUF 模型对话

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Ruby bindings for llama.cpp to run open-source language models locally. Run models like Gemma 4, Qwen 3.5, GLM 4.7, 
> L200: Generate vector embeddings for text using embedding models:

## 星数曲线

```mermaid
xychart-beta
    title "docusealco/rllama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-28 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2aa9ec5f2991` · [字段定义](../../DATASET.md)*
