# graphsignal/graphsignal

⭐ 271 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/graphsignal/graphsignal) · [官网](https://graphsignal.com) · 组织维护

**GPU 剖析器：让 AI agent 自主测量并优化推理性能**

以 sidecar 进程观测推理引擎或任意 GPU 应用的剖析工具：通过 CUPTI/ROCm 注入采集内核耗时、CUDA graph 回放、memcpy/同步等数据，经 NVML/AMD SMI 采集 GPU 遥测（利用率、显存、功耗、温度、XID/ECC 错误），并从 Prometheus 端点导入 vLLM/SGLang/TensorRT-LLM 的引擎指标。所有测量结果通过本地 /signals JSON 端点暴露，供 AI agent 执行基准测试-剖析-修改-复测的闭环；亦提供 graphsignal-top 终端视图与可内嵌的 C++ GPU probe 头文件。默认完全本地运行，仅设置 API key 时才上传数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CUPTI/ROCm 注入采集每内核、每 CUDA graph、每类传输/同步的累计耗时
- 本地 /signals JSON 端点供 agent 轮询读数，支持 benchmark-profile-modify 复测闭环
- graphsignal-top 终端实时视图与可内嵌的 lock-free C++ GPU probe
- 无需 root 或 GPU 剖析特权，默认不上传任何剖析数据

## 适用场景

- 让 AI agent 自主调优 vLLM/SGLang 等推理服务的延迟与吞吐
- 人工排查 GPU 工作负载中占主导的内核、传输或同步
- 在生产环境持续采集 GPU 与引擎指标（低开销默认模式）

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Graphsignal is a GPU profiler for AI agents to autonomously optimize inference performance across models, engines, a
> L9: * Inference engine metrics imported from Prometheus endpoints (vLLM, SGLang, TensorRT-LLM).
> L90: The endpoint is what closes the loop: an AI agent launches the workload under `graphsignal-run`, polls `/signals` u

## 星数曲线

```mermaid
xychart-beta
    title "graphsignal/graphsignal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 266 --> 272
    line [267, 271, 271]
```

2026-10-18 267 → 2026-10-24 271（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d29549a9f7ad` · [字段定义](../../DATASET.md)*
