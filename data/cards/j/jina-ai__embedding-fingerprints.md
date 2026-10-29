# jina-ai/embedding-fingerprints

⭐ 23 · Python · 推送 2026-03-07 · [GitHub](https://github.com/jina-ai/embedding-fingerprints) · [官网](https://embedding-inversion-demo.jina.ai) · 组织维护

**识别嵌入向量来自哪个嵌入模型的分类工具**

输入一个嵌入向量，通过将每个浮点数格式化为 %.4f 后按字符级分解（15 词表：数字、负号、小数点、分隔符、CLS、PAD），用一个小型 transformer（默认 4 层、约 80 万参数，RoPE/RMSNorm/SwiiGLU/SDPA）对 CLS 输出做分类，判断该向量由哪个嵌入模型生成。依据是不同模型在数值分布上留下特征指纹。目前覆盖 68 个类别（25+ 嵌入模型），验证准确率约 86%。提供数据生成、训练与绘图脚本，生成训练数据需要 GPU 与嵌入模型权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 字符级 tokenization 将浮点数分解为数字序列
- 约 80 万参数小型 transformer 分类器，层数可配置
- 68 个类别（25+ 嵌入模型），约 86% 验证准确率
- 提供训练数据生成、训练与指标绘图脚本

## 适用场景

- 给定嵌入向量推断其来源模型
- 研究嵌入模型的数值指纹特征
- 对多模型嵌入做来源分类训练实验

## 场景标签

 · 领域:机器学习/嵌入模型分析

## 证据(README 行号)

> L3: Given an embedding vector, identify which model produced it.
> L14: sequence, and a small transformer classifies the CLS output into one of N

## 星数曲线

```mermaid
xychart-beta
    title "jina-ai/embedding-fingerprints 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1aa1fef4954d` · [字段定义](../../DATASET.md)*
