# EricRollei/HYPIR-ComfyUI

⭐ 16 · Python · NOASSERTION · 推送 2025-11-18 · [GitHub](https://github.com/EricRollei/HYPIR-ComfyUI) · [官网](https://historic.camera) · 个人维护

**在 ComfyUI 中运行 HYPIR 图像修复与放大节点的自定义扩展**

为 ComfyUI 提供的自定义节点，封装基于 Stable Diffusion 2.1 与 LoRA 的 HYPIR 图像修复方法，支持输入图像修复、1-8 倍放大、分块潜空间处理与 VAE 平铺解码以降低显存占用；可选接入 OpenAI 兼容的 LM Studio 实例做提示词增强。安装经 ComfyUI Manager 或手动 git clone 到 custom_nodes，需自行下载 HYPIR 权重与 SD2.1 diffusers 权重。上游 HYPIR 仅限非商业使用，本仓库采用 Eric Hiss 双许可模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HYPIR LoRA + SD2.1 图像修复节点，支持 1-8 倍放大
- 分块处理与 VAE 平铺解码以支持高分辨率输入
- 可选 LM Studio（OpenAI 兼容）提示词增强
- 增强强度、细节增强、patch/stride 等修复控制参数

## 适用场景

- 在 ComfyUI 工作流中修复老照片或胶片扫描件
- 对高分辨率扫描图做修复与放大处理
- 借助 LM Studio 自动润色修复提示词

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Custom ComfyUI nodes that embed the **HYPIR** image restoration method for
> L35: 1. After installation, the node will appear in ComfyUI under `Hyper Image Restoration/HYPIR`.

## 星数曲线

```mermaid
xychart-beta
    title "EricRollei/HYPIR-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b0fe49e5d757` · [字段定义](../../DATASET.md)*
