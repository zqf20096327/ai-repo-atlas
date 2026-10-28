# arizqi/cpubrrr

⭐ 56 · Rust · Apache-2.0 · 推送 2026-08-11 · [GitHub](https://github.com/arizqi/cpubrrr) · 个人维护

**Apple 芯片 CPU 上的 MoE 模型推理研究运行时（Rust）**

从零用 Rust 编写的纯 CPU LLM 推理引擎：在手写 NEON/SME 整数内核、四路交错权重布局、Q8_K 整数累加内核与 12 工作线程调度下，于 Apple M4 Max CPU 上运行 gpt-oss:20b（MXFP4）等 4 个 MoE 模型，gpt-oss:20b 解码约 90.1 tok/s，相对调优后的 llama.cpp 约 1.17×。附带 OpenAI 兼容 API 服务脚本与并排演示页；README 详尽记录基准修正史（早期 7.5×/110 tok/s 结论已撤回）。定位为研究引擎而非生产服务器：单请求串行服务、无跨用户批处理，要求 Apple silicon 与 Rust/Python3/Ollama 环境，从源码编译运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- gpt-oss:20b MXFP4 在 M4 Max CPU 上解码 90.1 tok/s（同会话对比调优后 llama.cpp b9860 约 1.17×）
- 手写 NEON 整数内核（sdot/tbl）+ 四路交错权重布局 + Q8_K 整数累加内核
- 支持 4 个 MoE 模型（gpt-oss:20b/120b、Qwen3-Coder-30B、Qwen3-30B），配置驱动、同族零代码改动
- GSM8K 正确性对标：与 Ollama/llama.cpp 同权重结果持平（98 vs 94、89 vs 87，n=100 噪声范围内）

## 适用场景

- 在 Apple 芯片笔记本上无 GPU 运行 gpt-oss/Qwen3 MoE 模型
- 通过 OpenAI 兼容端点把本地 CPU 引擎接入聊天 UI、IDE 插件或 agent 框架
- 研究 CPU 推理内核优化（NEON/SME、量化内核、MoE 调度）并复现基准方法论

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: `cpubrrr` is a research runtime that runs frontier-class **mixture-of-experts** models
> L129: python3 scripts/openai_server.py          # serves http://localhost:8643/v1
> L230: This is a **research engine**, not a production server (no cross-user batching, no

## 星数曲线

```mermaid
xychart-beta
    title "arizqi/cpubrrr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-28 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cd2f2151bcb8` · [字段定义](../../DATASET.md)*
