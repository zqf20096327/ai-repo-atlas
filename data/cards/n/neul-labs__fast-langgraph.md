# neul-labs/fast-langgraph

⭐ 27 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/neul-labs/fast-langgraph) · [官网](https://fast-langgraph.neullabs.com) · 组织维护

**LangGraph 的 Rust 加速组件：提速检查点与状态管理**

面向 LangGraph 应用的高性能 Rust 加速库，提供两类用法：通过环境变量或 patch_langgraph() 实现零代码改动的自动加速（约 2.8x），以及手动使用 RustSQLiteCheckpointer（检查点 5-6x）、@cached 装饰器（LLM 响应缓存 10x+）、langgraph_state_update（状态更新 13-46x）等组件，并附带 GraphProfiler 性能分析器。以 pip/uv 安装的 Python 包发布，同时提供 crates.io 上的 Rust crate。要求 Python 3.9+，宣称兼容任意 LangGraph 版本。由 Neul Labs 维护，属其加速器工具链家族（fast-litellm/fast-crewai 等）的一员。

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

- 零代码改动的 shim 自动加速（FAST_LANGGRAPH_AUTO_PATCH 或 patch_langgraph()）
- RustSQLiteCheckpointer 检查点替代组件（宣称 5-6x 提速）
- @cached 装饰器缓存 LLM 响应，减少重复 API 调用
- GraphProfiler 性能分析器定位瓶颈

## 适用场景

- LangGraph 生产应用遇到检查点序列化或状态更新瓶颈时替换组件
- 缓存重复 LLM 调用以降低 API 开销
- 对现有 LangGraph 应用做透明加速而不改动业务代码

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Rust accelerators for LangGraph — up to 700x faster checkpoints.** Drop-in components that provide **up to 700x sp
> L18: Fast-LangGraph solves these by reimplementing critical paths in Rust while maintaining full API compatibility.
> L108: Drop-in replacement for LangGraph's SQLite checkpointer:

## 星数曲线

```mermaid
xychart-beta
    title "neul-labs/fast-langgraph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `074eda43f85f` · [字段定义](../../DATASET.md)*
