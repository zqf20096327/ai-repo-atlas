# outbrain-inc/outrank

⭐ 24 · Python · BSD-3-Clause · 推送 2026-03-03 · [GitHub](https://github.com/outbrain-inc/outrank) · [官网](https://dl.acm.org/doi/10.1145/3604915.3610636) · 组织维护

**稀疏分类数据的特征排序与数据质量异常检测 Python 库**

面向推荐系统等大规模稀疏、含噪分类数据的特征排序系统：采用按同基数特征噪声归一化的互信息变体度量特征相关性，并纳入特征相似性与组合相关性信息，用于识别最具信息量的特征、辅助 AutoML 模型压缩搜索与数据质量异常检测。以 Python 库形式提供，基于 Numba JIT 编译并支持多线程。有 CI、基准测试与单元测试，配套论文可引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基数感知的归一化互信息变体进行特征排序
- 特征相似性与组合相关性扩展
- 支持数据质量相关的异常检测
- Numba JIT 编译与多线程实现

## 适用场景

- 推荐系统场景下从大规模稀疏特征中筛选有效特征
- AutoML 流程中辅助搜索更紧凑的模型
- 分类数据集的数据质量异常检测

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L23: > The design of modern recommender systems relies on understanding which parts of the feature space are relevant fo
> L40: @inproceedings{10.1145/3604915.3610636,

## 星数曲线

```mermaid
xychart-beta
    title "outbrain-inc/outrank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `dcd1fc7aee5e` · [字段定义](../../DATASET.md)*
