# megeezy/Chameleon

⭐ 42 · Rust · MIT · 推送 2026-04-12 · [GitHub](https://github.com/megeezy/Chameleon) · 个人维护

**按请求动态加载/卸载模型的无状态 LLM 运行时**

Rust+Python 双语言的 LLM 推理运行时：不常驻任何模型，每条请求经意图分类与路由打分后选模型、加载、推理、卸载并释放全部 VRAM，空闲时占用为零。Rust 控制面（Axum 网关、路由、LRU 热缓存、VRAM 预算、监督进程），Python 推理面可插拔 llama-cpp-python/vLLM/Transformers/ExLlamaV2 后端，gRPC 连接多 Worker 分布式集群。支持热注册模型、SSE 流式 API、遥测入库。需从源码构建，Rust≥1.78、Python≥3.11、SQLite≥3.40，CUDA 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 请求级模型生命周期：加载→推理→卸载→空闲零 VRAM
- 规则/ML 双模式意图分类与可配置权重的路由打分
- LRU 热缓存以显存换延迟（warm_slots 0-4 档位）
- 可插拔推理后端（llama-cpp-python/vLLM/Transformers/ExLlamaV2）与 gRPC 多 Worker 集群

## 适用场景

- 显存有限的单卡环境按需轮换服务多个专用模型
- 为不同任务（代码/推理/摘要/对话）自动路由到最合适模型
- 搭建共享 GPU 集群上零空闲成本的推理服务

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L25: Chameleon is a **stateless AI execution runtime**. Unlike traditional model-serving systems that keep one or more L
> L51: - **Rust** — the control brain. Handles routing, lifecycle management, warm caching, concurrency, and the VRAM budg
> L145: Chameleon automatically selects the best model for the task, loads it, streams the response, and unloads when comp

## 星数曲线

```mermaid
xychart-beta
    title "megeezy/Chameleon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6617d4f8982e` · [字段定义](../../DATASET.md)*
