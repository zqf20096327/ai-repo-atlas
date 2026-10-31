# bradsec/ComfyUI_ResolutionSelectorPlus

⭐ 24 · Python · MIT · 推送 2026-07-03 · [GitHub](https://github.com/bradsec/ComfyUI_ResolutionSelectorPlus) · 个人维护

**ComfyUI 自定义节点：为图像生成工作流选择分辨率与空 latent**

面向 ComfyUI 用户的自定义节点，提供按模型优化的分辨率预设（竖屏/横屏/方形）、倍率（1x-4x）、批次数与自定义宽高输入，并输出可直接接 KSampler 的空 latent，按所选模型给出正确通道数（SD 1.5/SDXL 为 4 通道，Flux/Qwen Image/Z-Image 为 16 通道）。支持 ComfyUI Manager 一键安装或 git clone 手动安装；同时导出 V1 NODE_CLASS_MAPPINGS 与 V3 comfy_entrypoint 双 API，在 ComfyUI 0.25.0 上验证。

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

- 按模型优化的分辨率预设与 1x-4x 倍率、批次数设置
- 输出符合模型通道数的空 latent（4 或 16 通道）
- 自定义宽高（0-4096，步长 8）与独立倍率
- 兼容 V1 与 V3 双 API，ComfyUI 0.25.0 验证

## 适用场景

- 在 ComfyUI 工作流中快速选定模型适配的生成分辨率
- 生成可直接接 KSampler 的空 latent
- 为 SDXL/Flux/Qwen Image 等不同模型切换正确通道数

## 场景标签

 · 领域:图像生成/ComfyUI 生态

## 证据(README 行号)

> L1: # Resolution Selector Plus - Custom node for ComfyUI
> L11: - **Empty latent output** for direct KSampler connection, with the correct latent channel count per model (4 for SD
> L79: Dual API: exports the legacy V1 `NODE_CLASS_MAPPINGS` and a V3 `comfy_entrypoint` (`comfy_api`). Verified on ComfyU

## 星数曲线

```mermaid
xychart-beta
    title "bradsec/ComfyUI_ResolutionSelectorPlus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6925c51a06f4` · [字段定义](../../DATASET.md)*
