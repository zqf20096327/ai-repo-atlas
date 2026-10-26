# google/paxml

⭐ 560 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/google/paxml) · 组织维护

**给大模型训练研究者的 Jax 大规模训练框架**

Google 维护的基于 Jax 的机器学习实验框架，用于配置与运行大规模模型训练，支持 Cloud TPU 单机与多 slice（multislice）并行、SPMD/pjit 训练示例配置（1B/16B/22B/GPT3-XL 于 c4 数据集）以及 MFU 训练效率基准。安装途径为 PyPI 稳定版或 GitHub 源码，依赖 praxis 库；提供文档目录与 Jupyter Notebook 教程，GPU 支持指向 NVIDIA Rosetta 仓库的更新版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Jax 的大规模训练实验配置与运行框架
- 支持 Cloud TPU 单机与 multislice 多 slice 并行训练
- 提供 1B/16B/22B/GPT3-XL 在 c4 数据集的示例收敛运行配置
- 含 Model FLOPs Utilization (MFU) 训练效率基准说明

## 适用场景

- 在 Cloud TPU 上训练大规模语言模型
- 复现或修改 c4 数据集上的 GPT 类模型训练配置
- 进行多 slice TPU Pod 的分布式训练实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Pax is a framework to configure and run machine learning experiments on top of Jax.
> L150: To evaluate the MFU of a key class of workloads on TPU v4 Pods with Pax, we carried out an in-depth benchmark camp

## 星数曲线

```mermaid
xychart-beta
    title "google/paxml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 559 --> 561
    line [560, 560]
```

2026-10-18 560 → 2026-10-26 560（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c068f3006a5a` · [字段定义](../../DATASET.md)*
