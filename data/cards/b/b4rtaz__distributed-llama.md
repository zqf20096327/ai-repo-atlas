# b4rtaz/distributed-llama

⭐ 3,111 · C++ · MIT · 推送 2026-10-14 · [GitHub](https://github.com/b4rtaz/distributed-llama) · 个人维护

**分布式 LLM 推理引擎：多台家用设备组集群加速推理**

C++ 实现的分布式 LLM 推理引擎：将神经网络切片分布到多台设备（根节点 + 工作节点），通过以太网做张量并行与高速同步，内存用量也分摊到各节点。支持 Linux/macOS/Windows，针对 ARM 与 x86_64 AVX2 CPU 优化，另有实验性 Vulkan GPU 支持。提供单命令启动脚本（自动下载模型）、CLI 聊天、推理基准与 API 服务器。限制：节点数须为 2^n 且受模型 KV 头数上限约束，仅支持 q40/f32 量化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 根节点 + 工作节点的张量并行架构，RAM 分摊到各节点
- 支持 Llama 3.x、DeepSeek R1 Distill、Qwen 3（含 MoE）等模型
- 单命令 launch.py 下载模型并启动，支持 CLI chat 与 API 服务器
- 支持 ARM 与 x86_64 AVX2 CPU，实验性 Vulkan GPU 支持

## 适用场景

- 把家里多台电脑或树莓派组成集群跑大模型
- 在内存受限设备上分摊运行 70B/405B 级模型
- 搭建局域网 LLM 推理 API 服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Connect home devices into a powerful cluster to accelerate LLM inference. More devices mean faster performance, leve
> L64: * **🔸 Root node** - it's responsible for loading the model and weights and forward them to workers. Also, it synchr
> L71: * `dllama inference` - run the inference with a simple benchmark,

## 星数曲线

```mermaid
xychart-beta
    title "b4rtaz/distributed-llama 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 3111 --> 3114
    line [3113, 3112, 3112]
```

2026-10-18 3,113 → 2026-10-21 3,112（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `592af34307f0` · [字段定义](../../DATASET.md)*
