# vllm-project/bart-plugin

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/vllm-project/bart-plugin) · 组织维护

**让 vLLM 推理引擎支持 BART/Florence-2 的模型插件**

面向 vLLM 0.24.0+ 的模型插件，通过 vllm.general_plugins 入口点将 BART（编码器-解码器架构）与 Florence-2 视觉语言模型注册进 vLLM 的 ModelRegistry，使其可在 vLLM 推理引擎中运行。实现包含交叉注意力、多模态处理管线集成、量化兼容与张量并行支持。通过 uv 从源码安装，vLLM 启动时自动发现并加载插件；BART 家族为 MRV2-only。给需要在 vLLM 中部署 BART/Florence-2 模型的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 entry point 机制将 BART/Florence-2 注册进 vLLM ModelRegistry
- 支持张量并行分布式推理与 vLLM 量化特性
- 支持 Florence-2 视觉语言模型（需 trust_remote_code=True 与独立 tokenizer）
- 提供编码器批处理 padding 优化开关（VLLM_BART_ENCODER_MAX_SEQ_PADDING）

## 适用场景

- 在 vLLM 推理服务中运行 BART 摘要/翻译模型
- 用 vLLM 引擎部署 Florence-2 视觉语言模型
- 在 CNN/DailyMail 上评估 BART 摘要效果（ROUGE）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: This plugin adds support for BART (Bidirectional and Auto-Regressive Transformers) and Florence-2 models to vLLM's i
> L70: 1. **Entry Point**: Registered via the `vllm.general_plugins` entry point in the package metadata
> L71: 2. **Registration Function**: `register_bart_model()` in `__init__.py` registers the model with vLLM's ModelRegistr

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/bart-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c43a9a6d5a6f` · [字段定义](../../DATASET.md)*
