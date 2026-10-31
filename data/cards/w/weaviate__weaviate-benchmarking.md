# weaviate/weaviate-benchmarking

⭐ 32 · Go · BSD-3-Clause · 推送 2026-10-30 · [GitHub](https://github.com/weaviate/weaviate-benchmarking) · 组织维护

**Weaviate 向量数据库的性能基准测试工具（Go 实现）**

由 Weaviate 团队维护的性能基准测试仓库，包含基于 Go 的 benchmarker 工具，对 Weaviate 向量数据库执行 ANN（近似最近邻）检索性能测试。测试通过 Docker Compose 在同一机器上同时运行 Weaviate 容器与 benchmarker 容器，从 ann-benchmarks 格式的 hdf5 数据集（dbpedia-openai、snowflake-msmarco、sift、sphere 等）读取数据，按指定距离度量（如 cosine）运行单一性能测试。README 给出推荐机器配置（16 vCPU / 128GB 内存 / Debian 12），结果可在 Weaviate 文档中查阅。

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

- Go 编写的 benchmarker 基准测试工具
- Docker Compose 同时运行 Weaviate 与 benchmarker 容器
- 支持 ann-benchmarks hdf5 数据集（dbpedia-openai/sift/sphere 等）
- 可指定数据集与距离度量运行单一性能测试

## 适用场景

- 复现或自定义 Weaviate 的 ANN 检索性能基准
- 对比不同向量数据集与距离度量下的性能表现
- 为选型评估收集 Weaviate 的吞吐与延迟数据

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: This repo contains a tool for benchmarking Weaviate performance.
> L15: 2. `benchmarker` a go based benchmarking tool
> L42: DATASET=./datasets/dbpedia-openai-1000k-angular.hdf5 DISTANCE=cosine docker compose up --abort-on-container-exit

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/weaviate-benchmarking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ba6c369597e2` · [字段定义](../../DATASET.md)*
