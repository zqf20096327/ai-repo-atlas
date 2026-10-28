# facebookresearch/clusterscope

⭐ 25 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/facebookresearch/clusterscope) · [官网](https://facebookresearch.github.io/clusterscope/) · 组织维护

**提取 HPC 集群与作业信息的 CLI 和 Python 库**

Meta（facebookresearch）开源的 Python 库与命令行工具（CLI 命令为 cscope），用于读取 HPC 集群的配置信息与 Slurm 作业相关信息，以 Python API（如 clusterscope.cluster()）或命令行子命令形式调用。面向在 Slurm 集群上部署和管理训练/计算作业的开发者与科研用户。通过 pypi 安装，MIT 许可证，由 Lucca Bertoncini 与 Kalyan Saladi 维护。

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

- 以 Python 库与 cscope CLI 两种形式使用
- 读取 HPC 集群与 Slurm 作业信息
- pip install clusterscope 即可安装

## 适用场景

- 在脚本中程序化获取所在 Slurm 集群的配置信息
- 在 HPC 集群上排查或查询作业相关信息
- 为训练/计算任务编写集群自适应的启动逻辑

## 场景标签

 · 领域:HPC/集群工具

## 证据(README 行号)

> L3: Clusterscope is a CLI and python library to extract information from HPC Clusters and Jobs.
> L25: $ cscope

## 星数曲线

```mermaid
xychart-beta
    title "facebookresearch/clusterscope 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6d60307810a2` · [字段定义](../../DATASET.md)*
