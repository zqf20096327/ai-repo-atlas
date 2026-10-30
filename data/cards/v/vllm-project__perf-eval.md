# vllm-project/perf-eval

⭐ 17 · Python · 推送 2026-10-29 · [GitHub](https://github.com/vllm-project/perf-eval) · 组织维护

**vLLM 的性能基准与准确率评测工作负载仓库**

vLLM 项目维护的评测仓库：以 workloads/ 下的 YAML 配方定义 (模型, 硬件, 任务集) 组合，由 Buildkite 流水线自动发现并运行。配方支持四类评测块：lm_eval（基于 lm-evaluation-harness 的准确率）、vllm_bench（vllm bench serve 吞吐性能）、aiperf（客户端负载生成）、bfcl（函数调用评测）。面向需要跟踪特定 vLLM commit 性能的开发者，通过指定 VLLM_COMMIT 与 VLLM_IMAGE 触发构建，结果进入性能/评测看板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 配方定义 (模型, 硬件, 任务集)，Buildkite 自动发现运行
- 四类评测块：lm_eval / vllm_bench / aiperf / bfcl 可按需组合
- 并发扫描与 repetitions 中位数聚合，支持多 GPU（B200/H200/MI300X 等）
- 通过 VLLM_COMMIT / VLLM_IMAGE 跟踪特定 vLLM 版本的性能

## 适用场景

- 持续跟踪某 vLLM commit 的吞吐与准确率变化
- 为新模型在特定 GPU 上添加 nightly 性能回归配方
- 对模型做函数调用（BFCL）与准确率任务评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Run accuracy + perf workloads against vLLM, defined by small YAML recipes in `workloads/`.
> L5: Each recipe is one `(model, hardware, set of tasks)` combination. The Buildkite pipeline picks recipes up automatica
> L34: - **`vllm_bench:`** — *what perf to measure.* Lists `vllm bench serve` configs (input/output lengths, concurrency, 

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/perf-eval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `231744c98c5c` · [字段定义](../../DATASET.md)*
