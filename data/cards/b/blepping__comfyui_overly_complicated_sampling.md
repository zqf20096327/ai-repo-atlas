# blepping/comfyui_overly_complicated_sampling

⭐ 31 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/blepping/comfyui_overly_complicated_sampling) · 个人维护

**ComfyUI 扩展采样节点包：多种采样器与子步调度实验**

为 ComfyUI 提供的自定义采样节点集，包含 30 余种采样器（euler、heun、DPM++ 系列、RK4、Diffrax/torchdiffeq/torchode/torchsde 求解器后端等），支持按时间条件分组调度采样器、CFG++、Restart sigmas、自定义噪声与不可混合噪声，以及内置安全表达式语言在采样过程中过滤和操纵参数。作者自述状态为实验性且数学上不可靠，可能频繁破坏工作流，面向高级用户；对 Flux 等 RF 模型有若干限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 30 余种采样器，含 Diffrax/torchdiffeq/torchode/torchsde 求解器后端
- 按步数/时间条件分组切换采样器的调度机制
- 7 种子步合并策略（simple/divide/overshoot/lookahead/pingpong 等）
- 内置安全表达式语言，可在采样中动态操纵参数

## 适用场景

- 在 ComfyUI 工作流中按步骤切换不同采样器
- 实验子步拆分与合并等非常规采样策略
- 通过表达式在采样过程中动态调整参数

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Experimental and mathematically unsound (but fun!) sampling for ComfyUI.
> L70: ### `OCS Sampler`

## 星数曲线

```mermaid
xychart-beta
    title "blepping/comfyui_overly_complicated_sampling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5490b4240948` · [字段定义](../../DATASET.md)*
