# edwardcapriolo/reckoning

⭐ 45 · Java · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/edwardcapriolo/reckoning) · 个人维护

**Java 实现的 LLM 推理引擎：本地生成、嵌入与分类**

用 Java 编写的 LLM 推理引擎，支持文本生成、文本分类与嵌入计算，可嵌入应用内运行或以 HTTP 服务形式提供 OpenAI 风格的 /chat/completions 接口。支持 gemma2、llama、mistral、mixtral、qwen2/qwen3、gpt2 等模型。性能层面组合 safetensors 加载、内存映射存储、Project Panama 向量运算、原生 SIMD 内核、JQ4 量化与 WebGPU/Dawn 输出投影加速；支持张量并行、前缀缓存、KVCache2 与引导解码。较大模型磁盘占用 4GB–100GB，需较快磁盘与充足内存；部分 chat 接口功能尚不完整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持生成、嵌入、文本分类三种推理类型，可嵌入 Java 应用或以 HTTP 服务运行
- 多模型支持：gemma2、llama、mistral、mixtral、qwen2/qwen3、gpt2、Granite 4.0 等
- Panama/SIMD/原生 C/GPU 多档张量运算后端与 JQ4 量化
- 引导生成（choice/regex/JSON）、张量并行、KVCache2 与前缀缓存

## 适用场景

- 在 Java 应用中嵌入本地 LLM 推理，无需外部服务
- 以 Docker 部署 OpenAI 风格的本地推理 HTTP 服务
- 本地运行量化小模型做语义搜索与 RAG 嵌入

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Reckoning is a Java inference engine, capable of generating text, tokenizing input, computing embeddings, and more.
> L73: #### Embedded inference engine usage (ml-ops)
> L127: #### HTTP enabled inference engine (inference as a service)

## 星数曲线

```mermaid
xychart-beta
    title "edwardcapriolo/reckoning 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-22"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-11-10 44 → 2026-11-22 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `fa1baaa57bed` · [字段定义](../../DATASET.md)*
