# szilard/GBM-perf

⭐ 225 · HTML · MIT · 推送 2026-02-17 · [GitHub](https://github.com/szilard/GBM-perf) · 个人维护

**开源 GBM/GBDT 实现（xgboost/lightgbm/catboost/h2o）性能基准**

对比 h2o、xgboost、lightgbm、catboost 四种开源梯度提升实现在 airline 数据集（100K/1M/10M/100M 条记录，100 棵树、深度 10）上的训练时间、AUC 与内存占用，覆盖 CPU 与 GPU（V100）环境。附加内容含多核扩展性、多路 CPU（NUMA）影响、GPU 利用率模式、RAM 用量及 Spark MLlib GBT 对比。全程通过 Docker 自动化复现，git clone 后 build/run 即可重跑基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 GBM 实现在多个数据规模上的训练时间/AUC/内存基准结果
- Docker 全自动复现流程（CPU 与 GPU 两套镜像）
- 多核扩展与多路 NUMA 场景的专项测量（含 2020 优化前后对比）
- Spark MLlib GBT 的速度与内存对比数据

## 适用场景

- 为梯度提升库选型时查阅训练速度与内存占用数据
- 评估多核/多路 CPU 或 GPU 环境下的训练加速比
- 用 Docker 一键复现基准验证结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Performance of the top/most widely used open source gradient boosting machines (GBM)/ boosted trees (GBDT)
> L17: Installing to latest software versions and running/timing is easy and fully automated with docker:

## 星数曲线

```mermaid
xychart-beta
    title "szilard/GBM-perf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 224 --> 226
    line [225, 225]
```

2026-10-18 225 → 2026-10-31 225（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5ab784b2c032` · [字段定义](../../DATASET.md)*
