# MaxDevv/Un-LOCC

⭐ 74 · Python · 推送 2026-02-03 · [GitHub](https://github.com/MaxDevv/Un-LOCC) · 个人维护

**把长文本渲染成图像以压缩 LLM 上下文的研究与评测**

受 DeepSeek-OCR 启发的研究项目：将大段文本渲染为图像，利用 VLM 图像输入 token 固定的特性压缩上下文，最高达 2.8:1 压缩比并保持 93% 以上检索准确率。提出 Optical Needle in a Haystack（O-NIH）评测方法：在大段文本中注入唯一代码，考察模型仅做检索而非生成，并用 Levenshtein 距离做容错评分。README 记录 90 余组实验，覆盖图像尺寸、字号、字体、颜色对比度等变量。限制：仅测试感知检索而非深度推理，存在图像内提示注入风险。Python 实现在独立仓库 Un-LOCC-Wrapper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本渲染为图像的上下文压缩，最高 2.8:1 且保持 93%+ 检索准确率
- O-NIH 评测方法：注入唯一代码、检索式打分、OCR 容错归一化
- 90 余组实验记录图像尺寸/字号/字体/对比度等变量的影响
- 可应用于现有模型而无需微调

## 适用场景

- 为 VLM 应用的历史上下文做有损压缩以降低推理成本
- 评估不同视觉语言模型对图像化文本的检索能力
- 在有限显存的边缘设备上扩展 agent 记忆长度

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L8: The quadratic computational complexity of the Transformer attention mechanism makes large context LLM inferences pro
> L40: The core challenge of this research was to create a reliable method for testing a model’s text processing capabilit
> L81: *A raw log of every experiment performed during the optimization process. The same prompt was used for every call (

## 星数曲线

```mermaid
xychart-beta
    title "MaxDevv/Un-LOCC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-28 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a081810529ab` · [字段定义](../../DATASET.md)*
