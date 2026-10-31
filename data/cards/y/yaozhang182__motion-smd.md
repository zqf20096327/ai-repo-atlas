# yaozhang182/motion-smd

⭐ 19 · Python · MIT · 推送 2026-04-24 · [GitHub](https://github.com/yaozhang182/motion-smd) · [官网](https://yaozhang182.github.io/motion-smd/) · 组织维护

**把人体动作序列转为结构化文本，让 LLM 免编码器做动作问答与描述**

论文配套代码库：SMD 用确定性规则把关节位置序列（T,22,3）转为 26 个生物力学角度、时序分段与全局轨迹组成的结构化文本（约1K-4K tokens），使任意 LLM 无需动作编码器或对齐模块即可直接处理动作数据，仅用 LoRA 微调即可完成动作问答（BABEL-QA/HuMMan-QA）与动作描述（HumanML3D）。提供预生成数据与适配器下载、训练/评测脚本、注意力热力图分析及 MotionGPT3 编码器基线复现。训练在单张 H200 上约需 7-20 GPU 小时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则式 SMD 转换：关节角度+时序分段+轨迹→结构化文本
- 无需动作编码器，任意 LLM+LoRA 即可处理动作，跨 Qwen2.5/Qwen3/Gemma3/LLaMA-3.1/GLM-4 骨干验证
- 提供 HuggingFace 预生成数据与 LoRA 适配器，可跳过生成与训练直接评测
- 注意力热力图分析 SMD 各节段的模型关注（可解释性）

## 适用场景

- 复现论文中动作问答与动作描述的结果
- 用自己的 LLM 骨干做动作理解微调实验
- 分析模型对结构化动作描述各部分的注意力

## 场景标签

`微调` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L11: This repository contains the code for converting human motion sequences into Structured Motion Descriptions (SMD) a
> L15: SMD is a deterministic, rule-based conversion from joint position sequences to structured natural language text. By
> L22:     → Structured Motion Description (text, ~1K-4K tokens)
> L23:     → Any LLM + LoRA → QA Answer / Caption

## 星数曲线

```mermaid
xychart-beta
    title "yaozhang182/motion-smd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2dc755973051` · [字段定义](../../DATASET.md)*
