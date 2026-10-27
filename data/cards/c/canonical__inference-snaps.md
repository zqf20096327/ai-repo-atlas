# canonical/inference-snaps

⭐ 53 · 推送 2026-10-23 · [GitHub](https://github.com/canonical/inference-snaps) · [官网](https://documentation.ubuntu.com/inference-snaps) · 组织维护

**Canonical 出品的 snap 打包本地模型推理与 API 服务方案**

Canonical 维护的 Inference Snaps 项目：将生成式模型及其运行时打包为 snap 包，单条命令安装即可在本地运行模型并暴露标准 API。每个 snap 打包全部依赖，并根据本机硬件（CPU/GPU/NPU）自动选择优化后的运行时与模型权重；安装后可完全离线运行，环境在各 Linux 发行版间保持一致。收录 DeepSeek R1、Gemma、Qwen、GLM、Nemotron 等 20 余个开源模型 snap，文档托管于 Ubuntu documentation。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条 snap 命令安装预优化模型运行时并启动本地 API
- 按硬件（CPU/GPU/NPU）自动选择优化运行时与权重
- 打包全部依赖，离线可用，跨 Linux 发行版环境一致
- 收录 20 余个开源模型（DeepSeek R1/Gemma/Qwen/GLM/Nemotron 等）

## 适用场景

- 在 Linux 机器上一键部署本地 LLM 推理 API 端点
- 避免手工处理模型依赖与硬件优化配置
- 在离线或隔离环境中运行开源模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L26: - **Plug-and-play AI models**: Each snap bundles a range of optimized model weights and runtimes.
> L28: - **API-first design:** Exposes local standard APIs for integration.

## 星数曲线

```mermaid
xychart-beta
    title "canonical/inference-snaps 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-27 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2cbfd0bef4e6` · [字段定义](../../DATASET.md)*
