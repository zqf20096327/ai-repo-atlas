# buyukakyuz/rig

⭐ 37 · Rust · 推送 2026-01-25 · [GitHub](https://github.com/buyukakyuz/rig) · 个人维护

**跨机器分布式 LLM 推理框架：WiFi/LAN 组集群跑大模型**

Rig 是用 Rust 编写的分布式推理框架，通过流水线并行将大语言模型切分到多台机器（如 MacBook、旧台式机、工作笔记本），在普通 WiFi/LAN/VPN 上组成单一推理端点，协同运行单机跑不动的 70B+ 模型。提供单机 demo 与多机集群脚本两种使用方式，模型经 Hugging Face CLI 下载。要求 Rust 1.85+ 编译构建；项目处于活跃开发阶段，仅在 Apple Silicon 上测试过，CUDA 未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 流水线并行将模型切分到多台机器
- 通过 WiFi/LAN/VPN 组成单一推理端点
- 提供单机双 worker demo 与多机集群脚本
- Rust 实现，支持 Metal 编译特性

## 适用场景

- 把家里多台普通电脑凑起来跑 70B 级模型
- 无高速互联环境下搭分布式推理集群
- 在 Apple Silicon 机器上实验分布式 LLM 推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Rig is a distributed inference framework that splits large language models across multiple machines using pipeline p
> L7: Got a MacBook, an old desktop with a GPU, and a work laptop? None of them can run Llama 70B alone, but together they

## 星数曲线

```mermaid
xychart-beta
    title "buyukakyuz/rig 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9cf4f7a49dcc` · [字段定义](../../DATASET.md)*
