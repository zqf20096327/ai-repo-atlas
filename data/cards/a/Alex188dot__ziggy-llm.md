# Alex188dot/ziggy-llm

⭐ 24 · Zig · Apache-2.0 · 推送 2026-04-27 · [GitHub](https://github.com/Alex188dot/ziggy-llm) · [官网](https://alex188dot.github.io/ziggy-llm/) · 个人维护

**Zig 编写的 Apple Silicon GGUF 本地推理引擎**

用 Zig 从零实现的 GGUF 推理引擎，量化内核、Metal GPU shader、GGUF 解析器与推理运行时均为自研，无外部依赖，非 llama.cpp 封装。仅面向 Apple Silicon/Metal 与 GGUF 格式，产出单二进制 CLI，提供 chat/run/bench/inspect 命令；支持 Qwen、LLaMA、Mistral、Gemma 等架构及 Q4_K_M/Q6_K/Q8_0 等量化。Qwen 3.5 MoE 目前仅 CPU 路径，OpenAI 兼容 server 仍是待实现的脚手架。需 Zig 0.15.2+ 从源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 量化内核、Metal shader、GGUF 解析与运行时全部用 Zig 自研，零外部依赖
- 单二进制 CLI：chat / run / bench / inspect 命令
- 支持 Qwen / LLaMA / Mistral / Gemma 架构与 Q4_K_M、Q6_K、Q8_0、F16/F32 量化
- README 提供 ziggy-llm 与 llama.cpp、ZINC 的解码吞吐对比基准表

## 适用场景

- 在 Mac 上本地运行 GGUF 模型做文本生成
- 本地模型解码吞吐基准测试
- 作为可读性优先的 Zig 推理引擎实现来阅读与研究

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Built from the ground up with **zero external dependencies**, every line of quantization kernels, Metal GPU shaders,
> L9: We don't try to do everything for everyone; instead, we do one thing exceptionally well. By focusing exclusively on 

## 星数曲线

```mermaid
xychart-beta
    title "Alex188dot/ziggy-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8e2d01ae848c` · [字段定义](../../DATASET.md)*
