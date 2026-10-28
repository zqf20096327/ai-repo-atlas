# Scottcjn/exo-cuda

⭐ 94 · Python · GPL-3.0 · 推送 2026-09-26 · [GitHub](https://github.com/Scottcjn/exo-cuda) · [官网](https://rustchain.org) · 个人维护

**exo 的 CUDA 分支：用 tinygrad 在多块 NVIDIA GPU 上分布式运行 LLM**

exo 的社区分支，通过 tinygrad 后端恢复对 NVIDIA CUDA 的支持，可跨多节点/多 GPU 运行 Llama、Qwen、Mistral 等模型，节点经 UDP 广播自动发现，也可用 peers.json 手动配置。提供 ChatGPT 兼容 API（/v1/chat/completions）。要求 Ubuntu/Debian、Python 3.10+、NVIDIA 驱动 525+、CUDA 12.0+、每节点 GPU 显存 8GB+；已在 Tesla V100/M40、RTX 3090 上验证。GPL-3.0，由 Elyan Labs 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tinygrad 后端实现 NVIDIA CUDA 推理，替代原 exo 的 MLX 路径
- 多节点集群通过 UDP 广播自动发现，支持手动 peers.json 配置
- 提供 ChatGPT 兼容 API 端点
- 在 Tesla V100/M40、RTX 3090 及多节点集群上验证

## 适用场景

- 在多块 NVIDIA GPU 服务器上分布式运行大语言模型
- 用 ChatGPT 兼容 API 接入自有模型服务
- 把旧 Tesla 计算卡组成集群跑 LLM

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: **First verified working NVIDIA CUDA distributed inference for exo**
> L17: The original exo focuses on Apple Silicon (MLX). This fork restores **full NVIDIA CUDA support** via tinygrad:
> L71: exo --inference-engine tinygrad --chatgpt-api-port 8001 --disable-tui


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9d7aeb20b3c7` · [字段定义](../../DATASET.md)*
