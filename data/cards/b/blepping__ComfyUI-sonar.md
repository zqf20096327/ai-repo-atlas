# blepping/ComfyUI-sonar

⭐ 53 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/blepping/ComfyUI-sonar) · 个人维护

**ComfyUI 的 Sonar 动量采样与高级噪声工具节点集**

为 ComfyUI 提供的自定义节点集合：实现 Sonar（动量）采样，支持 Euler、Euler Ancestral、DPM++ SDE 采样器，带可选引导（guidance）配置；另含多种基础/高级噪声类型、噪声调度与合成、FreeU Extreme、Wavelet CFG 等噪声操作节点。部分节点在安装 ComfyUI_restart_sampling 等其他节点集后提供附加功能。README 声明实现与输入参数仍会频繁变动，不保证跨 git 版本的可复现生成。

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

- Sonar 动量采样支持 Euler / Euler Ancestral / DPM++ SDE
- 多种噪声类型及噪声调度、合成节点
- FreeU Extreme（自定义滤波/混合/调度）与 Wavelet CFG
- 与 ComfyUI_restart_sampling 集成提供额外节点

## 适用场景

- 在 ComfyUI 工作流中使用动量采样生成图像
- 为扩散生成配置自定义噪声类型与调度
- 对不同频段潜在特征使用不同 CFG 强度

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: A janky implementation of Sonar sampling (momentum-based sampling) for ComfyUI as well as an assortment of advanced 
> L7: Momentum based sampling currently supports Euler, Euler Ancestral, and DPM++ SDE sampling.

## 星数曲线

```mermaid
xychart-beta
    title "blepping/ComfyUI-sonar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-25 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `90fe3b0293a2` · [字段定义](../../DATASET.md)*
