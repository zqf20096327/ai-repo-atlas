# vllm-project/vllm-gr

⭐ 137 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/vllm-project/vllm-gr) · 组织维护 · 中文 README

**vLLM 的生成式推荐模型推理扩展，产出排序物品ID**

vLLM-GR 是 vLLM 的独立扩展，将 vLLM 从自回归文本生成扩展到生成式推荐场景：以用户交互历史（浏览、点击）作为输入，模型生成按似然排序的候选物品 ID（如语义 ID）。工程机制包括整段 beam search 单次提交、BeamAttn 与 KV cache 复用、异步调度、设备端 beam 后处理；同一 gr 配置可复用于离线 Python 推理、OpenAI 兼容 HTTP 服务与实验性 gRPC 服务。目前聚焦推理，候选集打分排序仍在规划中。当前支持 OneRec-1.7B，需从源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 整段 beam search 单次提交 EngineCore，一次响应返回排序候选与得分
- BeamAttn 与 beam KV cache 复用，跨请求前缀缓存跳过重复 prefill
- 同一 gr 配置复用于离线推理、OpenAI 兼容 HTTP 与实验性 gRPC 服务
- 复用 vLLM 平台抽象，支持 CUDA GPU 与昇腾 NPU

## 适用场景

- 用 OneRec-1.7B 为用户交互历史生成排序候选物品列表
- 通过 OpenAI 兼容 HTTP 接口在线提供生成式推荐服务
- 在昇腾 NPU 环境部署生成式推荐模型推理

## 场景标签

`推理引擎` `推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L3:  vLLM-GR brings generative recommendation models to vLLM.
> L16: large language models that generate text autoregressively. vLLM-GR extends
> L23: - **Model architectures.** The current implementation focuses on inference
> L56: - Reuse vLLM's platform abstraction to support CUDA GPUs and Ascend NPUs with


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `347ee2f3bd18` · [字段定义](../../DATASET.md)*
