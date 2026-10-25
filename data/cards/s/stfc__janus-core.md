# stfc/janus-core

⭐ 51 · Python · BSD-3-Clause · 推送 2026-10-07 · [GitHub](https://github.com/stfc/janus-core) · [官网](https://stfc.github.io/janus-core/) · 组织维护

**机器学习原子间势（MLIP）的计算工具库，服务材料/分子模拟**

由 STFC（英国科研机构）开发的 Python 库与 CLI 工具，基于 ASE 统一调用 10 种机器学习原子间势（MACE、CHGNet、SevenNet、NequIP、GRACE、UMA 等），提供单点能计算、几何优化、分子动力学（NVE/NVT/NPT）、过渡态（NEB）、声子、状态方程、弹性常数、MLIP 训练与微调、数据预处理及 PLUMED 稀有事件模拟等功能。计算结果自动记录模型架构与来源信息，可经 aiida-mlip 插件做溯源。MLIP 默认不随装，按 extras 单独安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接口接入 10 种 MLIP（MACE/CHGNet/SevenNet/NequIP/DPA/Orb/GRACE/UMA 等）
- 覆盖单点能、几何优化、MD、NEB、声子、状态方程、弹性常数等计算
- 支持 MACE/NequIP/SevenNet 的训练与微调
- 提供 Python API、janus CLI、YAML 配置文件与 Jupyter/marimo Docker 镜像

## 适用场景

- 材料模拟研究中用多种 MLIP 对比计算能量、力与应力
- 运行 MLIP 分子动力学（NVE/NVT/NPT）与声子/弹性计算
- 在已有数据上训练或微调 MACE、NequIP、SevenNet 势函数
- 在 Jupyter/marimo 容器环境中开展教学或复现实验

## 场景标签

`科研工具` `微调` · 领域:学习与行业

## 证据(README 行号)

> L66: - [x] Support for multiple MLIPs
> L177: All supported MLIP calculations are accessible through subcommands of the `janus` command line tool, which is inst

## 星数曲线

```mermaid
xychart-beta
    title "stfc/janus-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-25 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3036804740fd` · [字段定义](../../DATASET.md)*
