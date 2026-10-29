# raullenchai/twinspark

⭐ 176 · Shell · MIT · 推送 2026-08-14 · [GitHub](https://github.com/raullenchai/twinspark) · 个人维护

**在 2 台 DGX Spark 上部署 DeepSeek-V4-Flash 集群的完整配方**

面向本地大模型部署的操作手册型仓库：给出在 2× NVIDIA DGX Spark（GB10）上以 vLLM 0.25.2 + Ray 组建 TP=2 双节点集群、运行 DeepSeek-V4-Flash-0731（284B MoE，167 GB）的完整步骤，含 QSFP/RDMA 网络配置、netplan 文件、14 条故障排查记录、自愈容器架构（重启后约 8 分钟自动恢复服务）与基准数据（单流解码约 75 tok/s），并演示 OpenAI Codex CLI 接入本地端点做 agentic coding。版本全部锁定，作者注明为 2026-08-11 时点快照、预期随时间漂移。

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

- vLLM + Ray 双节点 TP=2 部署，2 台 DGX Spark 联合计算每个 token
- 自愈容器架构：任一或双机重启后零手动操作自动恢复服务
- 14 条实测故障排查表（RDMA memlock、Ray OOM、投机解码脏 KV 等）
- DSpark 投机解码调优，单流解码约 75 tok/s、预填约 1.7k tok/s

## 适用场景

- 在两台 DGX Spark 上跑起放不进单机的 284B MoE 模型
- 让 Codex CLI 指向本地 OpenAI 兼容端点做 agentic coding
- 排查双节点 vLLM 集群的 RDMA/Ray/长上下文问题

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: *Production-grade recipe: self-healing 2-node vLLM cluster, reboot-verified, tuned DSpark speculative decoding (~75 
> L9: - **Engine**: vLLM 0.25.2 (community image `ghcr.io/anemll/dspark-vllm-gx10:0.1.1` with GB10/sm_121 kernels: FlashIn
> L120: ## 4. Architecture: self-healing containers

## 星数曲线

```mermaid
xychart-beta
    title "raullenchai/twinspark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 175 --> 177
    line [176, 176]
```

2026-10-18 176 → 2026-10-29 176（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4d18ea5d8a04` · [字段定义](../../DATASET.md)*
