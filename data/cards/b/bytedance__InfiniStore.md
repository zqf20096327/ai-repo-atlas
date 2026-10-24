# bytedance/InfiniStore

⭐ 449 · C++ · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/bytedance/InfiniStore) · [官网](https://bytedance.github.io/InfiniStore/) · 组织维护

**面向 LLM 推理集群的分布式 KV cache 存储与传输服务**

开源高性能 KV store，服务于 LLM 推理集群：在 prefill-decoding 分离集群中提供 prefill 与 decoding 节点间的 KV cache 传输与复用；在非分离集群中作为 GPU/CPU cache 之外的扩展 KV cache 池并支持跨节点复用。也可作为独立 KV store 接入任意 LLM 训练/推理服务。已通过 LMCache 集成 vLLM，SGLang 等引擎集成进行中。支持 TCP/IP 与 RDMA（RoCE/Infiniband）网络，服务器可运行于 GPU 或 CPU 机器；提供 pip 安装与源码开发安装两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 prefill-decoding 分离与非分离两类集群的 KV cache 传输/复用
- 通过 LMCache 与 vLLM 集成，可作为独立 KV store 接入其他服务
- 支持 TCP/IP 与 RDMA（RoCE/Infiniband）网络
- 提供 pip 安装、selftest 自检命令与客户端示例

## 适用场景

- 为 prefill-decoding 分离推理集群提供 KV cache 传输
- 扩展推理集群 KV cache 容量并做跨节点复用
- 作为独立 KV store 接入自建 LLM 训练/推理服务

## 场景标签

 · 领域:LLM 基础设施/分布式存储

## 证据(README 行号)

> L7: InfiniStore is an open-source high-performance KV store. It's designed to support LLM Inference clusters, whether th
> L15: * Prefill-Decoding disaggregation clusters: in such mode inference workloads are separated into two node pools: pre
> L20: Currently InfiniStore has been integrated with vLLM. The integration is done via LMCache for the flexibility purpos

## 星数曲线

```mermaid
xychart-beta
    title "bytedance/InfiniStore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 448 --> 450
    line [449, 449]
```

2026-10-18 449 → 2026-10-24 449（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `665744b073cc` · [字段定义](../../DATASET.md)*
