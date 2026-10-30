# Extraltodeus/Skimmed_CFG

⭐ 234 · Python · Apache-2.0 · 推送 2026-08-01 · [GitHub](https://github.com/Extraltodeus/Skimmed_CFG) · 个人维护

**ComfyUI 节点集：抑制高 CFG 下的图像烧灼伪影**

面向 ComfyUI 的 latent diffusion 自定义节点集，插在模型加载器之后，通过过滤/替换/线性插值等五种算法处理正负预测之间的冲突值，允许在 CFG 6-100 的范围内使用更高 CFG 尺度并减少烧灼伪影。README 记录了各节点的行为差异、skimming scale 推荐值（2-3 抗烧灼、5-7 风格化）、与 SDE 采样器的搭配注意事项及副作用清单。以 SD3.5 turbo 做过测试。未在 README 中给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个节点变体：基础版、replace、线性插值、双尺度线性插值、Difference CFG、Timed flip
- skimming scale 可调，示例展示 CFG 100 下的输出
- 首个节点附带 full_skim_negative 与 disable_flipping_filter 选项
- 附带 'Support empty uncond' 节点用于超高 CFG 场景配合 ConditioningSetTimestepRange 使用

## 适用场景

- 在使用高 CFG 尺度生成时减少烧灼伪影
- 配合 SDE 采样器提升图像质量与随机性
- 在 ComfyUI 工作流中调整正负预测冲突以增强提示词遵循

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: A powerful anti-burn allowing much higher CFG scales for latent diffusion models (for ComfyUI)
> L8: Simply plug after the model loader (same for all the fours nodes):

## 星数曲线

```mermaid
xychart-beta
    title "Extraltodeus/Skimmed_CFG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 233 --> 235
    line [234, 234]
```

2026-10-18 234 → 2026-10-30 234（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bc13c7e836b3` · [字段定义](../../DATASET.md)*
