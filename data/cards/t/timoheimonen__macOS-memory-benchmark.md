# timoheimonen/macOS-memory-benchmark

⭐ 21 · C++ · GPL-3.0 · 推送 2026-09-25 · [GitHub](https://github.com/timoheimonen/macOS-memory-benchmark) · 个人维护

**Apple Silicon 内存性能测量 CLI：CPU/GPU 带宽与合成 LLM 访存剖析**

面向 Apple Silicon Mac 的低层命令行基准工具，用 C++17 与 ARM64 汇编测量 CPU 主存/缓存带宽与延迟、访问模式、TLB 行为、双核缓存行交接延迟；另以运行时编译的 Metal 计算核测量 GPU 带宽，并提供合成 LLM decode/prefill 访存剖析（连续或确定性分页 KV，能力门控的 Metal 后端）。输出带校准/工作量/重复性元数据的 JSON 以供审计比较，支持笛卡尔参数扫描与可恢复检查点。需 macOS 26+，可用 Homebrew 或源码 make 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU 带宽/延迟、访问模式、TLB、核间交接的原生 ARM64 测量路径
- Metal GPU 读/写/拷贝带宽测量（运行时编译 MSL 2.3 内核）
- 合成 LLM decode/prefill 访存剖析，支持连续与分页 KV，CPU/Metal 双后端
- 显式种子、笛卡尔扫描、可恢复 JSON 检查点与机读 stdout 输出

## 适用场景

- 我在 Apple Silicon 上做微架构层面的内存带宽与延迟调查
- 我需要剖析不同 KV 布局下 LLM decode/prefill 的内存流量
- 我要生成可审计、可复现的基准 JSON 用于硬件/配置对比

## 场景标签

 · 领域:系统性能测量/硬件基准

## 证据(README 行号)

> L5: `memory_benchmark` is a low-level command-line tool for measuring CPU and Metal GPU memory bandwidth, synthetic LLM
> L25: - **Synthetic LLM memory profile:** CPU and capability-gated Metal measurements of fixed-context decode and full-pr
> L181: |`--llm-memory`|Standalone synthetic LLM memory profile: CPU or Metal decode/prefill with contiguous or paged KV.|

## 星数曲线

```mermaid
xychart-beta
    title "timoheimonen/macOS-memory-benchmark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `900ed30503f1` · [字段定义](../../DATASET.md)*
