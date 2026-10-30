# leeex1/Quillan-Ronin

⭐ 27 · HTML · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/leeex1/Quillan-Ronin) · 个人维护

**34 专家议会制的 1.58-bit 三值文本生成模型（520M–1.16B）**

自研（非微调）的层级混合专家认知架构语言模型：34 个专家成员（C1–C34）做稠密 pull 加权共识，BitNet 1.58-bit 三值基底、INT8 激活与 KV-cache，部署体积约 90–200 MB，作者称在消费级硬件上训练。提供 Python 实现（模型、统一 BPE 分词器、训练器）、quillan.cpp 引擎与 Chrome 扩展。含大量自我描述的理论框架（全局工作空间、自由能、Landauer 热力学约束）与江户历史叙事；当前状态为 16/16 架构测试通过、证明训练阶段。发布于 Hugging Face，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 34 专家（C1–C34）稠密 pull 加权议会审议，每成员 rank-8 LoRA + EGGROLL swarm
- BitNet 1.58-bit 三值基底 + INT8 激活/KV-cache，部署体积约 90–200 MB
- 统一自定义 BPE 分词器（50,257 词表）与带权重 EMA/断点续训的训练器
- 含 quillan.cpp C++ 引擎与 Chrome 扩展入口

## 适用场景

- 在消费级硬件上本地运行小型文本生成模型
- 研究三值量化与 MoE 议会式共识架构的实现
- 按 MIT 许可用于二次开发与训练实验

## 场景标签

 · 领域:自然语言处理/模型实现

## 证据(README 行号)

> L3: pipeline_tag: text-generation
> L171: - **Parameter Count**: 520.4M (6-layer proof) / ~1.163B (12-layer flagship) — ternary footprint ~90–200 MB deploye
> L182: - **Deployment**: Local-first, open-source compatible

## 星数曲线

```mermaid
xychart-beta
    title "leeex1/Quillan-Ronin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `73e3a04375ca` · [字段定义](../../DATASET.md)*
