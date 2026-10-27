# Saganaki22/ComfyUI-sol-attn

⭐ 155 · Python · Apache-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/Saganaki22/ComfyUI-sol-attn) · [官网](https://nvlabs.github.io/Sana/Sol-Attn/) · 个人维护 · 中文 README

**ComfyUI 稀疏注意力 Triton 内核补丁，面向消费级 NVIDIA GPU 视频扩散**

围绕 NVIDIA Sol-Attn Triton 参考内核构建的 ComfyUI 自定义节点集，针对消费级 Blackwell（SM120/RTX 50 系列）及 SM86–SM121 架构调优。提供通用逐模型 Sol-Attn 补丁节点和四个 MiniMax H3 专用节点：零拷贝注意力、调度式稀疏 tau 与图预览、位精确调制融合、前馈分块降峰值显存。内核约束：head_dim 须为 128、bf16、无注意力掩码，不满足时回退常规后端。安装方式为 git clone 到 custom_nodes，除 torch/Triton 外无新增依赖。README 附带 RTX 5090 与 DGX Spark 的基准数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SM86–SM121 六种 NVIDIA 架构支持（pointer/TMA 两种前向路径）
- MiniMax H3 零拷贝注意力：直接读取融合 qkv 视图，无连续拷贝
- 前馈分块降低 MLP 峰值显存，输出位相同
- 不支持的形状/GPU 回退常规注意力后端并记录原因

## 适用场景

- 在 RTX 50 系等消费级显卡上降低 MiniMax H3 视频扩散的显存峰值
- 通过 ComfyUI 节点为任意模型接入 Sol-Attn 稀疏注意力
- 按采样进度调度稀疏度（早期稀疏、后期稠密）

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L14: Sparse attention and memory patches for video diffusion in ComfyUI, built around NVIDIA's **Sol-Attn** Triton refer
> L59: - **Two Sol-Attn integration paths** — a generic hook-based node for any model, and a MiniMax H3 node that feeds th

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-sol-attn 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-27"]
    y-axis "stars" 153 --> 156
    line [155, 154, 155, 155]
```

2026-10-18 155 → 2026-10-27 155（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b63593f9bb32` · [字段定义](../../DATASET.md)*
