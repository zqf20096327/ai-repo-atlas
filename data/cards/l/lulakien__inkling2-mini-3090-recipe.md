# lulakien/inkling2-mini-3090-recipe

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/lulakien/inkling2-mini-3090-recipe) · 个人维护

**在 1-2 张 RTX 3090 上运行 Inkling-2-Mini 的 vLLM 配方**

提供小型文件 overlay（以只读方式挂载到官方 vLLM 镜像上，无需重建）与启动脚本，使 `thinkingmachines/Inkling-2-Mini` 能在 sm_86 消费级 Ampere GPU 上运行；不含模型权重，需自行下载。给出 1 卡（128K 或 FP8 KV 下 262K）与 2 卡（262K，可选 512K/1M profile）的配置、280W 功耗上限下的吞吐与 MMLU 数据，附测试套件、原始结果与精度说明表。要求 Linux、Docker、NVIDIA Container Toolkit、支持 CUDA 13 的驱动。

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

- overlay 方式使官方 vLLM 镜像在 sm_86 上运行，不重建镜像
- 2 卡支持 262K 上下文，可选 512K (bf16 KV) / 1M (FP8 KV) profile
- 附带覆盖 API、并发、needle 检索、MMLU 的测试套件与原始结果
- 利用 checkpoint 内置 DSpark 投机草稿解码

## 适用场景

- 在消费级 RTX 3090 上本地部署 Inkling-2-Mini 推理服务
- 复现长上下文与并发吞吐的基准数据
- 以 OpenAI 兼容 API 接入 agent 工作流

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # Inkling 2 Mini on RTX 3090s: a vLLM recipe for 1 or 2 consumer Ampere GPUs
> L8: The official `vllm/vllm-openai:inkling-2-mini` image only supports Hopper/Blackwell. This repo has small file
> L118: Requirements: Linux, Docker with the NVIDIA Container Toolkit, an NVIDIA driver that supports CUDA 13


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `ab7e24d8121d` · [字段定义](../../DATASET.md)*
