# ai4protein/VenusX

⭐ 25 · Python · NOASSERTION · 推送 2026-04-10 · [GitHub](https://github.com/ai4protein/VenusX) · [官网](https://ai4protein.github.io/venusx/) · 组织维护

**蛋白质功能残基/片段预测的大规模基准（ICLR 2026）**

面向细粒度蛋白质功能理解的大规模基准：定义三个任务——残基级功能位点二分类、片段级生物角色多分类、无监督功能相似性配对打分。提供按 50% 片段相似度聚类划分的数据集（托管于 Hugging Face），覆盖序列、序列-结构、结构三类共 20 余个基线模型，并附训练与嵌入提取脚本。实验在 16 块 RTX 4090 上完成，更大模型可能需要更多资源。许可为 CC-BY-NC-NC-ND 系的 CC-BY-NC-ND-4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三任务：残基级二分类、片段级多分类、无监督功能相似性配对
- 覆盖序列/序列-结构/结构三类 20 余个基线模型
- 数据集按片段相似度聚类划分训练/验证/测试集，托管于 Hugging Face
- 提供训练与蛋白质/片段嵌入提取示例脚本

## 适用场景

- 评测蛋白质语言模型在细粒度功能任务上的表现
- 训练功能残基识别或片段分类模型
- 做功能相似蛋白配对的无监督评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **VenusX** is a large-scale benchmark for fine-grained protein functional annotation and pairing at residue, fragmen
> L18: VenusX benchmarks fine-grained protein understanding across multiple subprotein levels through three tasks:

## 星数曲线

```mermaid
xychart-beta
    title "ai4protein/VenusX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `26e1f497dee1` · [字段定义](../../DATASET.md)*
