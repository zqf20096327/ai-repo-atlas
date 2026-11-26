# lightseekorg/tokenspeed

⭐ 2,964 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/lightseekorg/tokenspeed) · [官网](https://lightseek.org/blog/lightseek-tokenspeed.html) · 组织维护

**面向生产级 agentic 工作负载的 LLM 推理引擎**

TokenSpeed 是面向 agentic 工作负载的 LLM 推理引擎，由非营利组织 LightSeek Foundation 维护。架构上以 C++ 控制平面（有限状态机管理请求生命周期与 KV cache，编译期类型系统强制资源安全）与 Python 执行平面分离为核心机制；内核层通过可插拔公共 API 与集中注册表支持异构加速器，请求路径上无 Python。提供 SMG/Dynamo（Rust）入口与服务器启动文档。README 未给出具体安装命令，仅链接到 Getting Started 与服务器参数文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 控制平面与执行平面分离：C++ 状态机 + Python 执行层
- 可插拔内核子系统：公共 API、集中注册表与插件机制
- Rust 入口（SMG/Dynamo）经 msgpack 驱动引擎，请求路径无 Python
- 已加入 PyTorch Ecosystem Landscape

## 适用场景

- 生产环境部署服务 agentic 工作负载的 LLM
- 在 NVIDIA/AMD 加速器上运行推理服务器
- 为前沿模型做 Day 0 服务与内核优化

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: TokenSpeed is a speed-of-light LLM inference engine designed for **agentic workloads**, with TensorRT-LLM-level perf
> L9: - **Scheduler**: C++ control plane and Python execution plane. Request

## 星数曲线

```mermaid
xychart-beta
    title "lightseekorg/tokenspeed 星数(近 26 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 2755 --> 2983
    line [2774, 2779, 2782, 2802, 2814, 2819, 2824, 2829, 2832, 2841, 2779, 2888, 2914, 2919, 2920, 2924, 2925, 2931, 2930, 2931, 2936, 2941, 2944, 2950, 2958, 2964]
```

2026-10-24 2,774 → 2026-11-26 2,964（+190）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4ec86757068d` · [字段定义](../../DATASET.md)*
