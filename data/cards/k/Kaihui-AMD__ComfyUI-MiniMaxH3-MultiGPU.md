# Kaihui-AMD/ComfyUI-MiniMaxH3-MultiGPU

⭐ 16 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/Kaihui-AMD/ComfyUI-MiniMaxH3-MultiGPU) · 组织维护 · 中文 README

**在 ComfyUI 中用两块 AMD GPU 序列并行推理 MiniMax H3**

面向 AMD ROCm 平台的 ComfyUI 自定义节点：将 MiniMax H3 视频生成任务的 transformer 序列与注意力头拆分到两块 GPU 上并行计算，采用受 DeepSpeed Ulysses 论文启发的序列并行实现，不增加 CFG 分支、不减少采样步数、不跳过 transformer 块或引入近似缓存。在 2×Radeon AI PRO R9700 上实测端到端加速 1.76 倍。要求 Linux、ROCm 与 RCCL 版 PyTorch，通过 git clone 安装到 custom_nodes 目录，无需额外 Python 包。仅支持并验证两块 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- H3 序列与 56 头注意力按 28 头/GPU 分片的双卡并行
- 与单卡 INT8 ConvRot 注意力数值完全一致（max_abs=0）
- 提供 CPU 数学测试、RCCL 传输测试与基准脚本
- loader 预留激活显存并支持分布式 rendezvous 端口配置

## 适用场景

- 有两块 AMD GPU 的用户加速 MiniMax H3 视频生成
- 在 32GB 显存单卡不足时跨两卡分摊显存运行 H3
- 在 AMD ROCm 环境的 ComfyUI 中复现双卡基准测试

## 场景标签

`视频生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L5: Clean-room, AMD-focused multi-GPU inference for MiniMax H3 in ComfyUI.
> L7: The current release is optimized and validated for **two GPUs**. It accelerates
> L75: cd ComfyUI/custom_nodes

## 星数曲线

```mermaid
xychart-beta
    title "Kaihui-AMD/ComfyUI-MiniMaxH3-MultiGPU 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7d437f50ef28` · [字段定义](../../DATASET.md)*
