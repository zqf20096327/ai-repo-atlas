# NVIDIA/runx

⭐ 641 · Python · BSD-3-Clause · 推送 2025-12-11 · [GitHub](https://github.com/NVIDIA/runx) · 组织维护

**深度学习实验管理工具：超参扫描、日志与结果汇总**

NVIDIA 维护的深度学习实验管理工具，由三个模块组成：runx 通过 yaml 定义超参列表并计算笛卡尔积生成命令行，支持交互运行或提交到 farm 集群；logx 负责指标、日志、tensorboard 与 checkpoint 记录；sumx 汇总各训练运行的超参与结果并排序。每个 run 自动生成唯一输出目录并复制代码副本。注意：README 首部声明项目已停止维护且含安全漏洞。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- yaml 定义超参并自动计算笛卡尔积生成训练命令
- 支持提交批处理任务到 farm 集群（可配置 SUBMIT_CMD/RESOURCES）
- 每次 run 生成唯一目录并复制代码快照
- logx 仅保留最新与最优 checkpoint；sumx 按指标汇总排序结果

## 适用场景

- 我不想为每次超参扫描写一次性脚本
- 在集群上批量提交训练任务并管理输出目录
- 训练后快速对比各超参组合的结果找最佳 run

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: # runx - An experiment management tool
> L7: `runx` helps to automate common tasks while doing research:
> L136: ## runx Architecture

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/runx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 640 --> 642
    line [641, 641]
```

2026-10-18 641 → 2026-10-26 641（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `788caa500310` · [字段定义](../../DATASET.md)*
