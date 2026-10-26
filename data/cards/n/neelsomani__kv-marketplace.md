# neelsomani/kv-marketplace

⭐ 27 · Python · MIT · 推送 2025-11-12 · [GitHub](https://github.com/neelsomani/kv-marketplace) · 个人维护

**跨 GPU 复用 KV Cache 的分布式推理组件，面向 vLLM**

推理运行时扩展：将 transformer 注意力 KV 张量作为可共享对象，进程在 prefill 后导出前缀缓存到注册表，其他匹配前缀的进程通过 CUDA peer-to-peer/IPC 直接跨 GPU 导入，避免重复计算。MVP 限定节点内复用，需配合 vLLM fork（vllm-kvm-dev 分支），提供精确前缀匹配、配置一致性校验与无匹配时自动回退；跨主机传输、前缀淘汰、分片 KV 导入等列为范围外。安装含 CUDA 扩展编译，需 CUDA 12.8 与支持 P2P 的 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- vLLM fork 提供 before_prefill/after_prefill 两个集成钩子
- CUDA peer-to-peer/IPC 跨 GPU 直接传输 KV 张量，绕过主机内存
- 前缀注册表支持精确匹配（LCP 计划中）与配置一致性强制校验
- 无匹配前缀时自动回退标准执行，测试验证复用保持输出一致

## 适用场景

- 多租户/共享系统提示的推理服务中消除重复前缀计算
- RAG、聊天服务等相同前缀负载下提升吞吐降低延迟
- 研究分布式推理中的前缀去重与缓存感知负载均衡

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: We propose a distributed inference runtime that enables cross-GPU reuse of transformer attention states. In autoregr
> L7: The Cross-GPU KV Cache Marketplace treats these attention states as first-class, shareable artifacts. Each process e
> L15: This initial release will focus on node-local reuse of transformer KV tensors within vLLM.

## 星数曲线

```mermaid
xychart-beta
    title "neelsomani/kv-marketplace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ff9ab00bb278` · [字段定义](../../DATASET.md)*
