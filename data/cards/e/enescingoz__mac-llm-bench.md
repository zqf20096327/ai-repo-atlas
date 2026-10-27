# enescingoz/mac-llm-bench

⭐ 45 · Shell · MIT · 推送 2026-04-22 · [GitHub](https://github.com/enescingoz/mac-llm-bench) · 个人维护

**Apple Silicon 上本地运行 LLM 的社区性能基准数据库**

面向 Apple Silicon Mac（M1–M5）的社区驱动基准数据库，收录本地 LLM 的推理速度与代码质量结果：用 llama-bench（GGUF/llama.cpp）与 mlx_lm.benchmark（MLX）在固定 token 数下测速，用 EvalPlus HumanEval+ 测 pass@1；结果按芯片代际→型号→硬件配置组织，GGUF 与 MLX 并排对比。提供 bench 脚本复现测试并贡献结果，支持参数扫描寻找最优设置。已知限制：单一量化档位（Q4_K_M/4-bit）、质量测试仅单机配置、推理模型关闭思维链测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双运行时测速：llama.cpp(GGUF) 与 Apple MLX，指标固定可对比
- EvalPlus HumanEval+ pass@1 代码质量评测
- 覆盖 10 个模型家族共 100 个基准，跨 M1–M5 各硬件配置组织结果
- 提供 --sweep 参数扫描寻找各模型最优设置

## 适用场景

- 查我的 Mac 跑某个模型每秒多少 token，选最优设置
- 对比同一模型在 GGUF 与 MLX 运行时下的表现
- 为本机贡献基准测试结果充实数据库

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Community-driven benchmark database for running LLMs locally on Apple Silicon Macs. Speed + code quality benchmarks 
> L40: |**GGUF**|`llama-bench`|`./bench_gguf.sh`|GGUF (llama.cpp)|Q4_K_M|
> L42: |**Quality**|EvalPlus (HumanEval+)|`./bench_quality.sh`|GGUF or MLX|same as above|
> L66: - Tool: EvalPlus v0.3.1

## 星数曲线

```mermaid
xychart-beta
    title "enescingoz/mac-llm-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6bd74797a491` · [字段定义](../../DATASET.md)*
