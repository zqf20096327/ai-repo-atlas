# iammrduncan/tensorless

⭐ 3 · C++ · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/iammrduncan/tensorless) · [官网](https://tensorless.dev) · 个人维护

**面向 Tesla P100 显卡的一命令量化 LLM 推理引擎**

为 NVIDIA Tesla P100（16 GB，sm_60/Pascal 架构）提供量化模型推理的工具链：引擎为 llama.cpp 的分支，附带针对 Pascal 编写的内核；配套自定义 3-bit 权重格式（PN）与调优模型。启动器检测 GPU、按配方选择引擎镜像与模型文件、拉取校验并启动 OpenAI 兼容服务器，推理通过容器镜像（podman/docker）运行。Apache-2.0 许可，模型权重保留各自许可。

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

- 单命令启动：tensorless run 检测 GPU、选配方、拉取镜像与模型并启动服务
- 针对 P100/Pascal 编写内核的 llama.cpp 分支引擎，发布按 digest 固定的容器镜像
- 自带 3-bit PN 权重格式的 Qwen3.8-27B 量化模型，附实测吞吐数据（docs/receipts）
- 启动 OpenAI 兼容 API 服务器，并提供 tensorless bench/models 命令

## 适用场景

- 在手持的 Tesla P100 上以单命令跑量化大模型
- 通过 OpenAI 兼容端点将 P100 接入本地推理服务
- 按配方复现实测的推理吞吐并与基准收据对比

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13: Custom engine + quant inference for P100s. A ~$100 GPU card, and we will make it fly.
> L21: The first target is the NVIDIA Tesla P100 (16 GB, sm_60), running Qwen3.8-27B-PN3: a 3-bit quantization of Qwen3.8-
> L65: - **Engine** (`engine/`): the inference engine source, a llama.cpp fork, published at each release.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `009c7f27d4fc` · [字段定义](../../DATASET.md)*
