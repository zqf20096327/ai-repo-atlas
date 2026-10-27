# mercator-ocean/oceanbench

⭐ 49 · Jupyter Notebook · 推送 2026-10-26 · [GitHub](https://github.com/mercator-ocean/oceanbench) · 组织维护

**评估数据驱动全球海洋预报系统的基准工具**

Mercator Ocean International 维护的海洋预报基准评测工具：以 GLORYS 再分析（1993-2019）与观测数据为参照，通过执行 Python notebook 对预报系统（challenger 数据集）运行多种评测方法，产出评测报告并汇总至官方积分表。提供 pip 安装、CLI 与 Python API，支持全球域及自定义区域评测，结果可上传 S3，并可在 EDITO datalab 或离线 HPC 节点运行。1/12° 分辨率评测依赖 Copernicus Marine Toolbox 并需其认证。论文发表于 NeurIPS 2025。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 challenger 预报数据集执行多种评测方法并生成 notebook 报告
- 开放 1/12° 与 1° GLORYS 训练数据集（lazy xarray.Dataset，140TB）
- CLI 支持并行评测多系统、区域选择与结果上传 S3
- 官方提交需附系统输出数据（Zarr/NetCDF）或可复现代码/容器

## 适用场景

- 我将自己的海洋预报系统提交官方评测并进入积分表
- 我用 GLORYS 再分析数据训练海洋预报模型
- 我在本地或 HPC 上离线评测预报系统的区域表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: OceanBench is a benchmarking tool to evaluate ocean forecasting systems against reference ocean analysis datasets (

## 星数曲线

```mermaid
xychart-beta
    title "mercator-ocean/oceanbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b4e82e5193cd` · [字段定义](../../DATASET.md)*
