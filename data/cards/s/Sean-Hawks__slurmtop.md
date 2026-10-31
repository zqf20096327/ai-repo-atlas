# Sean-Hawks/slurmtop

⭐ 13 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/Sean-Hawks/slurmtop) · 组织维护 · 中文 README

**单文件 Python 脚本：跨节点查看 GPU 占用者与利用率**

slurmtop 是一个仅依赖 Python 标准库（3.8+）的单文件脚本，通过 SSH 读取局域/集群中各节点的 CPU、内存、磁盘、网络与逐 GPU 利用率，显示持有每块 GPU 的用户与 Slurm 作业、队列，并标记被占用但闲置的 GPU。节点端零安装（仅需 SSH 与 POSIX sh），提供终端视图、浏览器仪表盘（可被 Prometheus 抓取 /metrics 喂 Grafana）、JSON 输出与可包裹任意命令的 HTML 报告（均值/p95/峰值）。支持 NVIDIA/AMD/Apple Silicon，Slurm 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件、节点端零安装，纯 SSH 读取，无 agent/数据库/守护进程
- 显示每块 GPU 的持有者与作业，标记被占用但闲置的 GPU
- 终端 / 浏览器 / Prometheus / JSON / HTML 报告五种输出共用一次刷新
- --report 包裹任意命令，输出平均/p95/峰值利用率、能耗等 HTML 报告

## 适用场景

- 一眼看清实验室里谁占着 GPU、哪些在空转
- 无监控设施时今天就能在若干节点上跑起来的集群监控
- 包裹训练命令生成本次运行的利用率与能耗报告

## 场景标签

 · 领域:HPC/基础设施监控

## 证据(README 行号)

> L8: `slurmtop` is a single Python script (standard library only, Python 3.8+) that
> L10: holds each GPU, and the Slurm queue. It reads other machines over plain SSH, so
> L57: |graphs in Grafana, alerts in Prometheus|`slurmtop --web`, scrape `/metrics`|node and per-GPU metrics, owner info, 

## 星数曲线

```mermaid
xychart-beta
    title "Sean-Hawks/slurmtop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `354f82bd1357` · [字段定义](../../DATASET.md)*
