# l-ramirez-lopez/resemble

⭐ 28 · R · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/l-ramirez-lopez/resemble) · [官网](http://l-ramirez-lopez.github.io/resemble/) · 个人维护

**光谱化学计量学 R 包：光谱相似度检索与局部学习建模**

R 语言包，面向复杂光谱数据的相异性分析与预测建模：提供 PCA/PLS 降维投影、多种相异性度量（PCA/PLS 空间马氏距离、相关、欧氏、余弦等）、近邻检索、经典记忆学习 mbl()（GPR/PLS/WAPLS 局部拟合）、进化子集搜索 gesearch() 与可复用局部专家模型库 liblex()。设计目标是大而异质光谱库的局部建模与库优化。从 CRAN 安装，需 C++ 编译器（Windows 装 Rtools）。README 附大量土壤光谱领域发表论文列表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记忆学习 mbl()：对每个查询用近邻拟合局部模型（GPR/PLS/WAPLS）
- gesearch() 进化算法从大光谱库选择域自适应校正子集
- liblex() 预计算局部专家模型库，免重拟合即可预测
- 6 种相异性度量构造器与 ortho_projection 降维

## 适用场景

- 我从大型光谱库检索与目标样本相似的光谱
- 我用局部建模改进大而异质光谱数据集的土壤性质预测
- 我需要从光谱库中选择最优校正子集构建特定场景模型

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L17: The `resemble` package provides computationally efficient methods for
> L19: data. Its core functionality includes memory-based learning (MBL),
> L112: - `model()`: Global PLS or GPR calibration

## 星数曲线

```mermaid
xychart-beta
    title "l-ramirez-lopez/resemble 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `880547c832c1` · [字段定义](../../DATASET.md)*
