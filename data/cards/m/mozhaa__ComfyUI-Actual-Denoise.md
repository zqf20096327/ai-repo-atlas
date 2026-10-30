# mozhaa/ComfyUI-Actual-Denoise

⭐ 21 · Python · GPL-3.0 · 推送 2026-02-26 · [GitHub](https://github.com/mozhaa/ComfyUI-Actual-Denoise) · 个人维护

**ComfyUI 自定义节点：img2img 中设定实际噪声量，换调度器行为一致**

为 ComfyUI 提供的一组自定义节点（Custom Nodes），用于在 img2img 工作流中直接设定实际加入的噪声量（actual_denoise），并根据所选调度器自动换算 denoise 值。原因是 KSampler 的 denoise 含义随调度器不同而变化，固定 denoise 在切换调度器时会产生不同噪声量。提供 Actual Denoise、Actual Denoise Inverse 及配合 KSampler (Advanced) 的 (Step) 版本节点。安装方式为 ComfyUI-Manager 的 Git URL 安装或手动克隆到 custom_nodes/ 目录，无外部依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 actual_denoise 指定实际噪声量，跨调度器行为一致
- 提供 Inverse 节点将常用 denoise 映射为 actual_denoise
- 提供 (Step) 版本节点适配 KSampler (Advanced) 的 start_at_step/end_at_step

## 适用场景

- img2img 时切换调度器而保持相同噪声效果
- 避免换调度器后手动调整 denoise 的试错
- 在细节修复与添加特效时精确控制图像改动幅度

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # ComfyUI-Actual-Denoise
> L2: Simple ComfyUI nodes to set the actual amount of noise in img2img, ensuring consistent behavior when changing schedu
> L5: + Use `Custom Nodes Manager > Install via Git URL` in ComfyUI-Manager

## 星数曲线

```mermaid
xychart-beta
    title "mozhaa/ComfyUI-Actual-Denoise 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0dd0ee1e41a0` · [字段定义](../../DATASET.md)*
