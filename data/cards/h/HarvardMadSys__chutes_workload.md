# HarvardMadSys/chutes_workload

⭐ 38 · Python · 推送 2026-10-17 · [GitHub](https://github.com/HarvardMadSys/chutes_workload) · 组织维护

**LLM 服务生产流量一年期追踪数据集（61.2 亿请求）**

论文《A Year in LLM Serving》的数据集与复现工件仓库：包含来自 Chutes 平台一年生产流量、覆盖 6.12B 请求与 9,174 个模型的请求级追踪（时间戳、模型/匿名用户标识、token 数、TTFT、前缀缓存复用等字段），数据以 91 GB parquet 文件发布并提供 DuckDB 暴露方式。仓库另含会话重构脚本（按前缀包含关系链接请求）、缓存驱逐与路由/负载均衡仿真，以及论文全部图表的复现流程。面向系统研究人员使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6.12B 请求、9,174 模型的一年生产级追踪数据
- 请求级字段含 TTFT、缓存 token、前缀复用与匿名用户标识（每三个月轮换重匿名）
- 会话重构脚本按前缀包含关系链接请求
- 前缀缓存驱逐与路由/负载均衡仿真及论文 48 张图复现

## 适用场景

- LLM 服务系统的缓存与路由策略研究
- 用真实生产负载做调度/负载均衡实验
- 复现论文的追踪分析与仿真结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: This repository contains the dataset and reproducibility artifacts for
> L18: We analyze one year of production traffic from

## 星数曲线

```mermaid
xychart-beta
    title "HarvardMadSys/chutes_workload 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-26 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d22a68c627b4` · [字段定义](../../DATASET.md)*
