# MoonshotAI/WorldVQA

⭐ 123 · Python · 推送 2026-02-04 · [GitHub](https://github.com/MoonshotAI/WorldVQA) · 组织维护

**评测多模态大模型视觉世界知识的 VQA 基准（3,500 题）**

MoonshotAI 发布的多模态大语言模型基准数据集：以 3,500 个 VQA 对覆盖 9 个类别，将视觉知识检索与推理能力解耦，测量模型对视觉实体的指认与命名等原子世界知识，关注语言与文化多样性。配套评估代码通过 OpenAI API 调用被评测模型与裁判模型（默认 Kimi-K2.5 / gpt-oss-120b），结果输出到 results 目录，并附排行榜。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3,500 个 VQA 对、9 个类别的基准数据集
- 解耦知识检索与推理，测量模型记忆的原子世界知识
- 提供评估脚本，通过 API 配置被评测模型与裁判模型
- 附排行榜，涵盖头部类别到长尾稀有实体

## 适用场景

- 评测多模态大模型的视觉百科知识与幻觉率
- 在研究论文中作为视觉事实性基准引用
- 比较不同模型在长尾视觉实体识别上的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: We introduce WorldVQA, a benchmark designed to evaluate the atomic vision-centric world knowledge of Multimodal Larg
> L13: **WorldVQA** is a meticulously curated benchmark designed to evaluate atomic vision-centric world knowledge in Mult
> L55: |`MODEL_NAME`|`Kimi-K2.5`|Model to evaluate|

## 星数曲线

```mermaid
xychart-beta
    title "MoonshotAI/WorldVQA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-26 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `c85b41b70180` · [字段定义](../../DATASET.md)*
