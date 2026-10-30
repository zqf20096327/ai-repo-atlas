# kyegomez/VLM-Mamba

⭐ 16 · Python · MIT · 推送 2026-01-05 · [GitHub](https://github.com/kyegomez/VLM-Mamba) · [官网](https://discord.gg/jM3Z6M9uMq) · 个人维护

**完全基于 Mamba 状态空间模型的视觉-语言模型实现（研究原型）**

由 Kye Gomez 开发的视觉-语言模型研究项目：用 Mamba（SSM）架构完全替换注意力机制，包含 VisionMamba 编码器、轻量 Fuyu 式处理器、纯 Mamba 语言模型与 BridgerFFN 多模态桥接三个模块。标准配置约 37M 参数，支持 LoRA 微调，README 给出内存占用下降与推理加速的理论结果及 COCO/VQA 任务描述。以 git clone 源码方式安装，需 Python 3.10+、PyTorch 2.0+ 与 mamba-ssm；标题自标 WIP（进行中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三模块架构：VisionMamba/Fuyu 双模式视觉处理 + LanguageMamba + BridgerFFN 桥接
- 标准配置约 37M 参数，支持 LoRA 参数高效微调
- 线性复杂度（O(n)）序列处理，Pydantic 类型安全配置系统

## 适用场景

- 研究 SSM 架构在视觉-语言任务中的可行性
- 实验注意力替代方案的内存与推理特性
- 基于模块化组件定制多模态模型结构

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L8: > *The first-ever Vision-Language Model (VLM) built entirely on State Space Models (SSMs), eliminating the need for 
> L12: We introduce **VLM-Mamba**, the first Vision-Language Model built entirely on State Space Models (SSMs), specifical
> L33: - **LanguageMamba**: A pure Mamba-based language model that processes text tokens sequentially

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/VLM-Mamba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `76054280d103` · [字段定义](../../DATASET.md)*
