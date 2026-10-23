# geerlingguy/beowulf-ai-cluster

⭐ 380 · Jinja · GPL-3.0 · 推送 2026-08-04 · [GitHub](https://github.com/geerlingguy/beowulf-ai-cluster) · 个人维护

**用 Ansible 在异构机器上部署并基准测试分布式 AI 集群**

由 Jeff Geerling 维护的 Ansible playbook 集合：在通过 SSH 连接的一组异构主机上自动化部署 AI 推理环境（下载并编译 llama.cpp、配置 distributed-llama 与 Exo），随后运行三类基准——单节点 llama-bench、llama.cpp RPC 全集群模式、distributed-llama 全集群模式，结果输出到控制台（另存于作者的 ai-benchmarks 项目）。面向自建 Beowulf 集群做 AI 性能测试的用户；Exo 因上游开发停滞仅支持手动基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ansible 一键完成集群环境部署（下载并编译 llama.cpp 等）
- 三种基准：单节点 llama-bench、llama.cpp RPC 全集群、distributed-llama 全集群
- 提供手动基准流程用于调试（llama-rpc / dllama-worker 服务管理）
- 节点需 SSH 可达且 hostname 与 hosts.ini 记录一致

## 适用场景

- 我在一堆旧电脑上搭集群，测试分布式推理性能
- 对比集群各节点的 llama.cpp 推理性能并验证 GPU/NPU 识别
- 调试大模型在多节点 RPC 模式下的运行问题

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L36:  1. Setup: downloads and compiles all the code required to run an AI model.
> L53:  - **llama.cpp benchmark - individual nodes**: Runs `llama-bench` on each node indepdently, and can be used to comp
> L54:  - **llama.cpp benchmark - full cluster (rpc-server)**: Configures llama.cpp in RPC mode, and runs a benchmark agai

## 星数曲线

```mermaid
xychart-beta
    title "geerlingguy/beowulf-ai-cluster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 379 --> 381
    line [380, 380]
```

2026-10-18 380 → 2026-10-23 380（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `dd03c455ad17` · [字段定义](../../DATASET.md)*
