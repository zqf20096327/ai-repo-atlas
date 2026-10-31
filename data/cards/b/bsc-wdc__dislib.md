# bsc-wdc/dislib

⭐ 55 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/bsc-wdc/dislib) · 组织维护

**面向 HPC 的分布式机器学习 Python 库（基于 PyCOMPSs）**

由巴塞罗那超算中心（BSC）工作流与分布式计算组开发的分布式算法库，当前聚焦机器学习算法，API 设计参考 scikit-learn 与 PyTorch。底层基于 PyCOMPSs 编程模型，代码可在本地经 docker 开发后不改一行直接运行于集群、超算、云与容器化平台。README 列出 20 余台已预装 PyCOMPSs 的欧洲超算及支持的架构（Intel SSF、IBM Power 9），并提供 eScience 2019 论文供引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供开箱即用的分布式机器学习算法库
- 基于 PyCOMPSs，代码可从本地无缝迁移到集群/超算/云
- API 设计参考 scikit-learn 与 PyTorch
- 列出 20 余台已预装 PyCOMPSs 的超算平台

## 适用场景

- 在超算或集群上运行大规模机器学习算法
- 本地用 docker 开发分布式 ML 代码后直接部署到生产平台
- 科研论文中使用并引用其 eScience 2019 论文

## 场景标签

 · 领域:高性能计算/分布式机器学习

## 证据(README 行号)

> L33: The Distributed Computing Library (dislib) provides distributed algorithms ready to use as a library. So far, disli
> L5:  Distributed computing library implemented over PyCOMPSs programming model for HPC.

## 星数曲线

```mermaid
xychart-beta
    title "bsc-wdc/dislib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-31 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bf1e3cfb0b05` · [字段定义](../../DATASET.md)*
