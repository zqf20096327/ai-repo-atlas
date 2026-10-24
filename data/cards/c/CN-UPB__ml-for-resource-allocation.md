# CN-UPB/ml-for-resource-allocation

⭐ 59 · Jupyter Notebook · 推送 2026-10-23 · [GitHub](https://github.com/CN-UPB/ml-for-resource-allocation) · 组织维护

**用机器学习回归预测 NFV 虚拟网络功能资源需求的研究代码与数据集**

学术研究仓库（NetSoft 2020 论文配套）：包含来自 SNDZoo 的真实 VNF 性能数据、在数据上训练 ML 回归模型的代码，以及训练完成可直接使用的已保存模型。模型可集成进 B-JointSP 等 VNF 放置算法，为新实例分配合适资源或动态调整已部署实例的资源。代码以 Jupyter notebook 形式提供，可选对比 TabPFN（经 Prior Labs API，数据会上传）与 AutoGluon。需 Python 3.6+，pip 安装依赖。

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

- 包含真实 VNF 性能测量数据与已训练模型
- 训练并对比多个 ML 回归模型（按 RMSE 评估）
- 提供与 B-JointSP VNF 放置算法集成的评估代码
- 可选对比 TabPFN 与 AutoGluon（未安装则自动省略）

## 适用场景

- 研究 VNF 动态资源分配的预测方法并复现论文结果
- 获取真实 VNF 性能数据训练回归模型
- 评估 ML 模型在 VNF 放置算法中的效果与运行时开销

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Virtual network functions (VNFs), e.g., firewalls or video optimizers, can run on standard x86 servers and can be in
> L5: This repository contains real-world VNF performance data from the SNDZoo, code to train machine learning models on t

## 星数曲线

```mermaid
xychart-beta
    title "CN-UPB/ml-for-resource-allocation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-24 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8901241346a5` · [字段定义](../../DATASET.md)*
