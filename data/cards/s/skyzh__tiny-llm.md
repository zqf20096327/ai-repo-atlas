# skyzh/tiny-llm

⭐ 5,803 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/skyzh/tiny-llm) · [官网](https://tiny-llm.dev) · 个人维护

**面向系统工程师的 LLM 推理系统实践课程（Apple Silicon）**

tiny-llm 是一门面向系统工程师的实践课程，目标是端到端理解 LLM 推理。课程基于 MLX 数组与 MLX 扩展运行时，不使用高层神经网络层：学员在 Python、C++ 或 Metal 中实现算子，MLX 作为正确性参照与性能基线。路径为四周：从矩阵运算搭建 Qwen3 模型、KV-cache 与量化/SIMD 优化、实现 continuous batching 与 paged KV 的 mini vLLM，到构建带校验边界的 coding agent。课程环境需 Apple Silicon（共享内存与 Metal 内核）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四部分路径：Qwen3 模型搭建 → 单请求优化 → mini vLLM → coding agent
- 在 Python/C++/Metal 中手动实现算子，MLX 作正确性参照与性能基线
- 将公式与内存流量、kernel 占用、KV-cache、批处理、调度关联
- 配套参考实现 tiny_llm_ref 与测试/基准附录

## 适用场景

- 系统工程师想端到端理解 LLM 推理链路
- 在本地 Apple Silicon 上学习 kernel 与服务机制
- 动手实现 continuous batching 与 paged KV-cache

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: tiny-llm is a hands-on course for systems engineers who want to understand LLM
> L17: The course is built on MLX arrays and the MLX extension runtime, without using
> L25: The course follows a four-week learning path:

## 星数曲线

```mermaid
xychart-beta
    title "skyzh/tiny-llm 星数(近 26 点)"
    x-axis ["2026-10-20", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 4675 --> 5905
    line [4777, 4786, 4787, 4788, 4789, 4790, 4791, 4792, 5298, 5485, 5507, 4788, 5692, 5711, 5719, 5726, 5734, 5739, 5742, 5747, 5752, 5765, 5788, 5797, 5802, 5803]
```

2026-10-20 4,777 → 2026-11-23 5,803（+1,026）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `bc19b8c1c025` · [字段定义](../../DATASET.md)*
