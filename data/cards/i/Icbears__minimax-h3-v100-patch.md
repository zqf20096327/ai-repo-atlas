# Icbears/minimax-h3-v100-patch

⭐ 40 · Python · GPL-3.0 · 推送 2026-09-06 · [GitHub](https://github.com/Icbears/minimax-h3-v100-patch) · 个人维护 · 中文 README

**在 NVIDIA V100 上加速 MiniMax H3 推理的 ComfyUI 混合精度补丁节点**

ComfyUI 自定义节点（ZIP 解压至 custom_nodes），为 MiniMax H3 在 CUDA 计算能力 7.0（V100）上提供 FP16 混合精度运行时补丁：FP16 权重与 attention/MLP 分支，FP32 保留残差、归一化、SwiGLU、Token Refiner 与最终 heads 等安全岛。v0.1.4 修复 ComfyUI 0.34.5 下参数数量不匹配的 TypeError。面向在 V100 显卡上运行 MiniMax H3 的 ComfyUI 用户；限制为仅支持计算能力 7.0，v0.1.4 的验证为本地结构/参数/数据流校验，性能数据为 v0.1.3 的历史记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- FP16 权重加载与 DiT attention/MLB FP16 分支
- FP32 安全岛（残差/归一化/SwiGLU/Token Refiner/最终 heads）
- v0.1.4 修复 ComfyUI 0.34.5 的参数数量 TypeError
- CUDA 计算能力 7.0 限制与重复扩展检测

## 适用场景

- 在 V100 显卡的 ComfyUI 中以 FP16 运行 MiniMax H3 降低显存占用
- 修复旧版 H3 扩展在 ComfyUI 0.34.5 下的报错
- 无需 --fp16-unet 标志即可使用混合精度推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: 3. Extract `minimax-h3-v100-v0.1.4.zip` into the active `custom_nodes` directory. The ZIP has one top-level folder:
> L24: - Native FP16 weights through ComfyUI loading, prefetch and offload.
> L29: - CUDA compute capability 7.0 restriction, duplicate-extension checks and no lazy `weight.data` conversion remain i

## 星数曲线

```mermaid
xychart-beta
    title "Icbears/minimax-h3-v100-patch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-30 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b3db8d6e3755` · [字段定义](../../DATASET.md)*
