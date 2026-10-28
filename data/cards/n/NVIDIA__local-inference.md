# NVIDIA/local-inference

⭐ — · [GitHub]() · 组织维护

**面向 NVIDIA SM120/121 GPU 的本地推理服务器（研究原型）**

Flare 是 NVIDIA 开源的本地推理服务器，面向 SM120/SM121 GPU 工作站及 DGX Spark 等紧凑系统，设计目标为长对话、编码 agent 与重复工具调用场景下的内存、带宽与计算利用。机制上分两阶段：Ignition 用 PyTorch/Transformers/FlashInfer 加载模型、调优内核、编译前向并捕获 CUDA 图生成运行时包；Rust 运行时 Helios 无 Python 地提供服务。明确声明为研究原型，且不替代 vLLM 等生产推理引擎，模型与部署模式覆盖面收窄以换取专注的本地服务契约。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 构建期用 PyTorch/Transformers/FlashInfer 编译并捕获 CUDA 图，服务期由 Rust 运行时 Helios 无 Python 执行
- 将 KV 缓存与循环状态等对话状态作为整体管理，支持复用、分支与恢复
- 针对 SM120/SM121 GPU 与 DGX Spark 等本地工作负载的专用推理服务

## 适用场景

- 在 DGX Spark 等本地 NVIDIA 工作站上运行编码 agent 的长会话推理
- 研究本地推理服务中内存与状态管理的工程方案
- 为技术协作与早期反馈参与研究原型试用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Flare is a local inference server for NVIDIA SM120/SM121 GPUs, built for
> L18:  Helios, the Rust runtime, serves that package without Python. Compilation and


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4d04f943c5a5` · [字段定义](../../DATASET.md)*
