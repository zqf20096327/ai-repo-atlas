# NetEase-Media/grps_trtllm

⭐ 161 · Python · Apache-2.0 · 推送 2025-12-08 · [GitHub](https://github.com/NetEase-Media/grps_trtllm) · 组织维护 · 中文 README

**面向开发者的纯 C++ OpenAI 协议 LLM 推理服务框架**

基于 GRPS 框架与 TensorRT-LLM 后端、Tokenizers.cpp 实现的纯 C++ LLM 服务：以 OpenAI 接口协议对外提供 chat 与 function call，支持 inflight batching、multi-GPU、paged attention、kv-cache reuse、lookahead decoding 等 TensorRT-LLM 加速技术，并通过集成 OpenCV 支持多模态 LLM（ViT 部分可自行扩展）。不同 LLM 家族的 prompt 构建/结果解析以 styler 机制扩展。部署方式为 Docker 容器内构建 TensorRT-LLM 引擎并以 grpst 工具构建部署，需 NVIDIA GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 C++ 实现 tokenizer、LLM 推理、ViT 全链路
- OpenAI 协议接口，支持 chat 与 function call
- 支持 multi-GPU、inflight batching、paged attention 等 TensorRT-LLM 加速技术
- 多模态 LLM 支持与可扩展的 LLM styler 机制

## 适用场景

- 部署兼容 OpenAI 协议的高性能 LLM 推理服务
- 多 GPU 环境下运行多模态大模型服务
- 为 AI agent（如 llama-index）提供 function call 后端

## 场景标签

`推理引擎` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4: 实现纯```C++```版，相比```vllm serve```更优性能的```OpenAI LLM```服务，支持```Chat```、```Ai-agent```、```Multi-modal```
> L26: * 通过纯```C++```实现完整```LLM```服务，包含```tokenizer```（支持`huggingface`, `sentencepiece`tokenizer）、```llm推理```
> L33:   ```TensorRT-LLM```推理加速技术。

## 星数曲线

```mermaid
xychart-beta
    title "NetEase-Media/grps_trtllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 160 --> 162
    line [161, 161]
```

2026-10-18 161 → 2026-10-26 161（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f4c025e6cd2a` · [字段定义](../../DATASET.md)*
