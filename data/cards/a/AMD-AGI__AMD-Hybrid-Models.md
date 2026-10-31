# AMD-AGI/AMD-Hybrid-Models

⭐ 14 · Python · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/AMD-AGI/AMD-Hybrid-Models) · [官网](https://arxiv.org/abs/2505.17272) · 组织维护

**AMD 官方的 LLM 注意力/Mamba 混合模型训练推理代码库**

AMD 发布的官方仓库，收录两个研究项目：X-EcoMLA 将预训练注意力改造为多头潜在注意力（MLA）以实现极致 KV 缓存压缩；Zebra-Llama 提供混合 MLA + Mamba2 模型家族，以最少重训练获取效率。面向进行 LLM 架构研究与实验的科研人员，各项目在独立子目录中实现训练与推理工作流，面向 AMD GPU 平台。仓库附 arXiv 论文引用信息，Apache 2.0 许可，未在 README 中给出安装与运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- X-EcoMLA：将预训练注意力升级回收为 MLA，实现极端 KV 缓存压缩
- Zebra-Llama：混合 MLA + Mamba2 模型家族，最少重训练
- 提供训练与推理工作流，面向 AMD GPU

## 适用场景

- 研究 KV 缓存压缩与潜在注意力方法
- 复现 X-EcoMLA / Zebra-Llama 论文实验
- 构建混合注意力+Mamba2 架构的 LLM

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: |`x-eco-mla/`|Implements **X-EcoMLA**: a method for upcycling attention into Multi-head Latent Attention (MLA) for 
> L13: |`zebra-llama/`|Implements **Zebra-Llama**: a family of hybrid MLA + Mamba2 models with minimal retraining and maxi

## 星数曲线

```mermaid
xychart-beta
    title "AMD-AGI/AMD-Hybrid-Models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0644083f80b8` · [字段定义](../../DATASET.md)*
