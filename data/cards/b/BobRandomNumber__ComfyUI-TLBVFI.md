# BobRandomNumber/ComfyUI-TLBVFI

⭐ 23 · Python · 推送 2026-02-18 · [GitHub](https://github.com/BobRandomNumber/ComfyUI-TLBVFI) · 个人维护

**ComfyUI 的 TLB-VFI 视频帧插值节点包**

将 TLB-VFI（基于扩散的时间感知视频帧插值模型）封装为 ComfyUI 自定义节点：克隆到 custom_nodes 目录后，放入预训练的 vimeo_unet.pth 权重，即可在 ComfyUI 中通过节点生成两帧之间的中间帧，支持批量处理、可调扩散步数与运动分析分辨率。实现上移除了 CuPy、PyTorch-Lightning 等非标准依赖，改用原生实现。适用于 ComfyUI 工作流中的视频补帧/升帧处理。

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

- 提供 TLB-VFI 帧插值 ComfyUI 节点（times_to_interpolate/diffusion_steps/batch_size 等参数）
- 移除 CuPy、PyTorch-Lightning 等非标准依赖，改用原生实现
- 支持多帧对批量处理
- VQGAN 编码 + 布朗桥扩散 UNet + VQGAN 解码的插值流程

## 适用场景

- 在 ComfyUI 工作流中对视频做帧插值提升帧率
- 批量处理多帧对的补帧任务
- 调节扩散步数与 flow_scale 控制补帧质量与速度

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A node pack for ComfyUI that provides video frame interpolation using the **TLB-VFI** model.
> L5: This is a wrapper for the TLB-VFI: Temporal-Aware Latent Brownian Bridge Diffusion for Video Frame Interpolation pro

## 星数曲线

```mermaid
xychart-beta
    title "BobRandomNumber/ComfyUI-TLBVFI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `58caeba1a966` · [字段定义](../../DATASET.md)*
