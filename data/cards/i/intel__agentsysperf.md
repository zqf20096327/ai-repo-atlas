# intel/agentsysperf

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-05 · [GitHub](https://github.com/intel/agentsysperf) · 组织维护

**面向端到端 Agentic AI 系统栈的可插拔基准测试套件**

以栈为单位而非单端点，对 Agentic AI 系统做端到端性能基准测试。核心机制是通过 Python entry points 组合四类插件（基准、测量、优化档案、硬件遥测），外部开发者可不改动套件本体发布适配器。内置 6 个基准适配器、4 个测量层、7 个分析器，结果存入 SQLite 规范存储，支持 Markdown/PowerPoint 报告、Prometheus/Grafana 导出与 Streamlit 仪表盘。限制：要求 Python 3.12/3.13 与 Linux x86_64；优化档案尚未接入实际运行，仅提供声明式规格与验证机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 7 个 entry-point 组实现插件化扩展，含 6 个基准适配器与 4 个测量层
- LLM 轨迹录制/回放缓存，回放免 API 调用且结果确定
- 每次运行自报告测量覆盖率，避免部分数据被误读为完整结果
- SQLite 规范存储 + Streamlit 仪表盘 + Prometheus/Grafana 导出

## 适用场景

- 对终端型 agent（Terminal-Bench/SWE-bench 等）做系统级性能剖析
- 测量 CPU/缓存/内存带宽等硬件层瓶颈与并发拐点
- 录制一次 LLM 轨迹后离线回放测量硬件表现
- 以插件形式接入自研基准或遥测探针

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A pluggable benchmark suite for end-to-end agentic AI stacks. Stack-level, not single-endpoint. Plugins for benchmar
> L15: - **6 BenchmarkAdapters** — synthetic_cpu (9 workloads), terminal_bench (Harbor/Terminus-2), openclaw, swe_bench, t


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `5079a6d905ee` · [字段定义](../../DATASET.md)*
