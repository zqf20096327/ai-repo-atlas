# aiDAPTIV-Phison/aiDAPTIV

⭐ 21 · Apache-2.0 · 推送 2026-04-06 · [GitHub](https://github.com/aiDAPTIV-Phison/aiDAPTIV) · [官网](https://phisonaidaptiv.com/) · 组织维护

**用 NVMe SSD 扩展 GPU 显存的 LLM 训练/推理中间件**

Phison Pascari 的 aiDAPTIV 存储加速平台：以高性能 NVMe SSD（aiDAPTIV cache memory）作为 GPU VRAM 的快速扩展层，在本地硬件上运行更大的模型与更长上下文，减少显存不足问题。aiDAPTIVLink 2 支持LoRA与全参数微调、CPU Adam、多GPU/多节点与VLM；KV-cache offload 属于 aiDAPTIVLink 3。仅支持 Linux（Ubuntu 24.04.3、CUDA 13.0），需购买 aiDAPTIV cache memory SSD 随附分发，提供试用与高校通道。注意其目的是解除显存瓶颈而非加速微调核心计算。

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

- NVMe SSD 分层（VRAM+RAM+SSD）扩展可用内存
- 支持 LoRA/全参数微调、多 GPU（1/2/4/8）与多节点训练
- 与现有 PyTorch 工作流集成，改动最小化
- 提供 GPU/CPU/SSD 兼容性清单与 VRAM 需求表

## 适用场景

- 在有限显存的工作站上微调更大参数量的模型
- 本地部署运行 LLM 推理而无需云端
- 延长现有 GPU 硬件上可处理的上下文窗口

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L12: aiDAPTIV is a storage-accelerated AI infrastructure platform designed to remove GPU memory bottlenecks during large
> L25: **aiDAPTIV memory management middleware** is Phison’s middleware layer in the **aiDAPTIV** stack that lets you trai
> L27: > This middleware version (aiDAPTIVLink 2 series) is primarily focused on post-training and fine-tuning workflows. 

## 星数曲线

```mermaid
xychart-beta
    title "aiDAPTIV-Phison/aiDAPTIV 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5c238500cf4b` · [字段定义](../../DATASET.md)*
