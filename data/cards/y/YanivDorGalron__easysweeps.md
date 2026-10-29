# YanivDorGalron/easysweeps

⭐ 21 · Python · MIT · 推送 2026-01-02 · [GitHub](https://github.com/YanivDorGalron/easysweeps) · [官网](https://yanivdorgalron.github.io/easysweeps/) · 个人维护

**自动化 W&B 超参扫描创建、启动与 GPU 进程管理的 CLI 工具**

面向使用 Weights & Biases 做实验管理的深度学习研究者的命令行工具：通过模板加变体文件从单一配置为多个数据集/环境批量创建隔离的 sweep，在指定 GPU 上以 systemd scope 单元启动、列出和终止 sweep agent，并按 GPU 或 sweep 灵活停止进程。以 pip 包提供，要求 Python 3.7+、W&B 账号，CUDA GPU 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模板+变体机制为多数据集批量生成隔离 sweep
- 按 GPU 列表启动 agent，支持每 GPU 多 agent
- ez kill 按 GPU/sweep 灵活终止 agent
- agent 以 systemd scope 单元运行

## 适用场景

- 在多张 GPU 上批量启动和管理 W&B 超参扫描
- 为多个数据集复用同一超参模板创建独立 sweep
- 按 GPU 或 sweep 停止失控的实验进程

## 场景标签

 · 领域:机器学习实验管理

## 证据(README 行号)

> L9: # EasySweeps - A CLI tool for automating Weights & Biases sweeps across multiple GPUs.
> L23: EasySweeps solves these by providing simple commands to **create, launch, monitor, and manage** sweep agents.

## 星数曲线

```mermaid
xychart-beta
    title "YanivDorGalron/easysweeps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fd04ca7c88ea` · [字段定义](../../DATASET.md)*
