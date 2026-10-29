# InfraWhisperer/llmtop

⭐ 22 · Go · NOASSERTION · 推送 2026-05-11 · [GitHub](https://github.com/InfraWhisperer/llmtop) · 组织维护

**面向 LLM 推理集群的终端实时监控仪表盘**

用 Go 编写的 TUI 实时监控工具，供运行 vLLM、SGLang、LMCache、NVIDIA NIM、NVIDIA Dynamo、TGI、TensorRT-LLM、Triton、llama.cpp、LiteLLM、Ollama 等推理后端的集群运维者使用：读取各后端 Prometheus/JSON 指标，展示 KV cache、队列深度、TTFT/ITL 延迟、token 吞吐，并提供基于 DCGM exporter 的 GPU 视图（利用率/显存/温度/功耗）与按模型分组视图。原生支持 Kubernetes，经 API server 代理自动发现推理 Pod，无需端口转发。安装提供 brew、go install 与 GitHub Releases 二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 11 种推理后端（vLLM/SGLang/TGI/TensorRT-LLM/llama.cpp/Ollama 等）并自动探测
- 实时展示 KV cache、TTFT/ITL 延迟、token 吞吐等指标
- GPU 视图读取 DCGM exporter 的利用率/显存/温度/功耗
- Kubernetes 自动发现 Pod，经 API server 代理抓取，无需端口转发

## 适用场景

- 在终端实时查看推理集群各 worker 的负载与延迟指标
- 按模型分组对比吞吐并下钻查看明细
- 排查 GPU 利用率与显存占用情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L17: Real-time terminal dashboard for **vLLM**, **SGLang**, **LMCache**, **NVIDIA NIM**, and **NVIDIA Dynamo** inference
> L44: - Real-time KV cache, queue depth, TTFT/ITL latency, token throughput across all workers
> L47: - Kubernetes-native — auto-discovers pods, scrapes through API server proxy, no port-forwards needed

## 星数曲线

```mermaid
xychart-beta
    title "InfraWhisperer/llmtop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fe44a8c0e7ca` · [字段定义](../../DATASET.md)*
