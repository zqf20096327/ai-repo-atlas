# Lex-DRL/ComfyUI-BestResolution

⭐ 16 · Python · LGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/Lex-DRL/ComfyUI-BestResolution) · 个人维护

**ComfyUI 节点包：半自动计算扩散模型的最优采样分辨率**

ComfyUI 的自定义节点包（UX/QoL），用于半自动计算最优采样分辨率：保证宽高为像素步长（默认 48）的倍数、匹配模型训练分辨率（总像素数），并考虑后续放大（HD-fix）场景。提供 Simple、From Aspect-Ratio、From Area 三个主节点，外加一个包装内置节点的辅助放大节点和自动裁剪/填充工具节点。多数节点只计算分辨率数值、不处理图像本身。面向 ComfyUI / Stable Diffusion 工作流用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 个主节点（Simple / From Aspect-Ratio / From Area）计算最优宽高
- 像素步长（step）参数最高优先级，默认 48，可按放大链路调整
- From Area 节点按训练分辨率（SD1.5=512、SDXL=1024）匹配总像素数
- 辅助节点支持按指定倍率用放大模型缩放图像并给出范围提示

## 适用场景

- 在 ComfyUI 工作流中让模型在接近训练分辨率下采样
- 规划多次放大的初始分辨率，避免后续裁剪或外绘
- 按期望宽高比或单边长度自动推导合规分辨率

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: # `Best Resolution` ComfyUI nodes [UX/QoL]
> L7: A small modular pack — nodes for semi-automatic calculation of the best (most optimal) sampling resolution:

## 星数曲线

```mermaid
xychart-beta
    title "Lex-DRL/ComfyUI-BestResolution 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-22"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-11-08 16 → 2026-11-22 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `5042e2eba5aa` · [字段定义](../../DATASET.md)*
