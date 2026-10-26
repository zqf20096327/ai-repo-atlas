# amzn/pecos

⭐ 556 · Python · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/amzn/pecos) · [官网](https://libpecos.org/) · 组织维护

**大规模输出空间的机器学习框架：极端多标签分类/排序与 ANN 检索**

Amazon 开源的模块化机器学习框架，面向巨大输出空间问题：X-Linear 递归线性模型沿层次标签树预测 top-k 标签（C++ 实时推理、支持约一亿量级输出空间）；XR-Transformer 在多分辨率目标上微调 Hugging Face 预训练 Transformer；另含实现 HNSW 算法的近似最近邻检索模块（稀疏/稠密特征、SIMD 优化、多线程）。以 Python 库（libpecos）提供，输入输出用 SciPy CSR 矩阵表示。支持平台仅列出 Ubuntu 20.04/22.04 与 Amazon Linux 2，Python 3.9-3.12。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- X-Linear 层次标签树线性模型，C++ 快速实时推理，可处理 100MM 输出空间
- XR-Transformer 多分辨率微调 Hugging Face 预训练 Transformer
- HNSW 近似最近邻检索模块，支持稀疏/稠密特征与 SIMD 优化
- 以 pip 安装的 Python 库形式提供，附玩具数据与 API 示例

## 适用场景

- 为极端多标签分类/排序任务训练 top-k 预测模型
- 在大规模候选集中做检索或近似最近邻搜索
- 微调预训练 Transformer 生成任务感知嵌入

## 场景标签

`向量数据库` `微调` · 领域:知识与检索

## 证据(README 行号)

> L6: PECOS is a versatile and modular machine learning (ML) framework for fast learning and inference on problems with la
> L9: Given an input, PECOS identifies a small set (10-100) of relevant outputs from amongst an extremely large (~100MM) c

## 星数曲线

```mermaid
xychart-beta
    title "amzn/pecos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 555 --> 557
    line [556, 556]
```

2026-10-18 556 → 2026-10-26 556（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `80a697115f4c` · [字段定义](../../DATASET.md)*
