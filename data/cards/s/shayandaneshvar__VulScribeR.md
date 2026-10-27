# shayandaneshvar/VulScribeR

⭐ 29 · Java · 推送 2025-12-09 · [GitHub](https://github.com/shayandaneshvar/VulScribeR) · 组织维护

**论文官方仓库：用 RAG+LLM 生成漏洞样本做数据增强**

论文 VulScribeR: Exploring RAG-based Vulnerability Augmentation with LLMs 的官方代码与数据仓库。基于 RAG 检索与 LLM 生成易受攻击代码样本，用于深度学习漏洞检测（DLVD）模型的数据增强；生成样本含过滤与未过滤版本（后者附带生成所用的 clean_vul 配对与漏洞行元数据），并提供检索器输出与训练数据集（Bigvul/Reveal/Devign/PrimeVul，VGX/Vulgen 作为基线）。使用方法与各模型训练说明分别指向外部链接与 models 目录内的独立 README。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 检索 + LLM 生成漏洞样本并经验证阶段过滤
- 提供未过滤数据集（含生成配对来源与漏洞行元数据）
- 覆盖 Bigvul/Reveal/Devign/PrimeVul 数据集与检索器输出
- models 目录含各 DLVD 模型的训练说明

## 适用场景

- 复现论文中的漏洞增强实验
- 获取增强后的漏洞检测训练数据
- 训练与评估深度学习漏洞检测模型

## 场景标签

`RAG` `网络安全` · 领域:知识与检索

## 证据(README 行号)

> L3: Official repository for our paper:
> L34: ### Our Generated Vulnerable Samples

## 星数曲线

```mermaid
xychart-beta
    title "shayandaneshvar/VulScribeR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f74e9dade2b9` · [字段定义](../../DATASET.md)*
