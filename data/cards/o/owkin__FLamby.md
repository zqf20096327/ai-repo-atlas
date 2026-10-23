# owkin/FLamby

⭐ 246 · Python · MIT · 推送 2026-07-07 · [GitHub](https://github.com/owkin/FLamby) · [官网](https://owkin.github.io/FLamby/) · 组织维护

**医疗跨孤岛联邦学习基准套件：7 个真实数据集与策略评测**

Owkin 维护的 cross-silo 联邦学习（FL）基准：以 dataset suite 形式提供 7 个自然划分的医疗数据集（Fed-Camelyon16、Fed-Heart-Disease、Fed-ISIC2019、Fed-IXITiny、Fed-KITS2019、Fed-LIDC-IDRI、Fed-TCGA-BRCA）的加载、预处理与评测代码，并含多种标准 FL 策略基线实现，支持复现随附 NeurIPS 2022 论文结果。仓库不分发数据本体，需在原网站接受许可后单独下载。提供 conda/make 安装与 Docker 基础镜像，并给出与 Fed-BioMed、FedML、Substra 等 FL 框架的对接示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个自然划分的真实医疗数据集的统一加载与评测代码
- 内置多种标准联邦学习策略基线并可复现论文基准
- 提供 Docker 基础镜像与各数据集容器化执行示例
- 兼容主流 FL 框架（Fed-BioMed / FedML / Substra 对接示例）

## 适用场景

- 在真实医疗数据上验证新的联邦学习策略并对比排行榜
- 复现随附论文的基准结果与异质性图表
- 跨数据集模态测试 FL 框架的适配性

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: FLamby is a benchmark for cross-silo Federated Learning with natural partitioning,
> L36: FLamby is a dataset **suite** instead of a repository.
> L21: A companion paper

## 星数曲线

```mermaid
xychart-beta
    title "owkin/FLamby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 245 --> 247
    line [246, 246]
```

2026-10-18 246 → 2026-10-23 246（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ade0dcabcc87` · [字段定义](../../DATASET.md)*
