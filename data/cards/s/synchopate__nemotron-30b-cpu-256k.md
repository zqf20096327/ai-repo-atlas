# synchopate/nemotron-30b-cpu-256k

⭐ 23 · Python · 推送 2026-10-30 · [GitHub](https://github.com/synchopate/nemotron-30b-cpu-256k) · 个人维护

**在纯 CPU 上以 30-50+ tok/s 运行 30B MoE 模型、256K 上下文的技术方案与 llama.cpp 补丁集**

面向 llama.cpp（ggml-cpu）的 CPU 推理优化工程文档与补丁仓库：以 NVIDIA Nemotron 3.5 Lightning 30B-A3B 混合 Mamba-2/MoE 架构为基础，在 AMD Ryzen 9 9955HX（Zen 5、64GB DDR5、无 GPU）上实现 256K 上下文、30-50+ tok/s 生成。手段包括 AVX-512 VNNI 权重重排、非时间性 L3 流、2MB HugePages、双 CCD 线程绑核、无草稿模型投机解码（RouteCrack）、KV 量化与 /dev/shm 前缀缓存等八项优化，附与 Qwen 系列基线的基准对比表。仓库以 README 工程论文加 patches 目录形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合 Mamba-2 SSM（46/52 层）+ MoE 架构将 KV 缓存降至 1.54-1.73 KB/token
- 八项微架构与引擎优化（AVX-512 VNNI 重排、NTA 流、HugePages、双 CCD 绑核等）
- RouteCrack 无草稿模型投机解码，有效生成速度 50.5-65.0 tok/s
- 25K 上下文多轮 TTFT 从 148 秒降至 <0.35 秒（HARP-Cache + KV 复用）

## 适用场景

- 在无 GPU 的工作站/移动 CPU 上运行 30B 级 MoE 长上下文推理
- 为 llama.cpp 打补丁获得 AVX-512/HugePages 等底层加速
- 研究混合 SSM 架构在 CPU 推理中的 KV 缓存权衡

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: *Date: October 2026 | Target Engine: `llama.cpp` (`ggml-cpu`) + RouteCrack Draftless Speculative Engine | Hardware: 
> L43: ├── patches/
> L113: Even with Nemotron 3.5's tiny KV footprint, scaling to 256K tokens at 30–50+ tok/s required solving eight deep sys


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6138222afce7` · [字段定义](../../DATASET.md)*
