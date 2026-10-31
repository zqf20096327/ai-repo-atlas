# isEmmanuelOlowe/llm-explorer

⭐ 22 · TypeScript · MIT · 推送 2026-08-24 · [GitHub](https://github.com/isEmmanuelOlowe/llm-explorer) · [官网](https://llm.labiium.com/) · 个人维护

**图表式 LLM 架构与部署估算浏览器：查架构、算显存、配硬件、比云价**

静态 Web 应用（Next.js Pages Router，可部署到 GitHub Pages）：从 Hugging Face 以固定 revision、config.json 与 safetensors 头部范围请求读取模型元数据，生成交互式架构图（注意力、MoE、多模态路径），并把模型转为部署估算——权重/KV 缓存/优化器状态的显存构成、基于 roofline 的吞吐上限估计、跨 NVIDIA/AMD/Intel/Apple 硬件的容量匹配、以及仅在有带日期的供应商报价对应到确切硬件时才显示的云价格。面向做部署规划的开发者。区分精确算术、有源证据与估计三类输出，不下载权重、不执行远端代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固定 revision 的 Hugging Face 模型检视（config.json + 有界 safetensors 头请求）
- 推理/训练显存模型与 Full/LoRA/QLoRA 训练规划（DDP/FSDP/ZeRO-3）
- 跨 NVIDIA/AMD/Intel/Apple 的拓扑感知硬件匹配与带验证日期的云价目录
- 静态无后端部署（GitHub Pages），不收集 HF token、不执行远端 Python

## 适用场景

- 部署前估算模型在特定 GPU 上的显存占用与是否放得下
- 对比不同云厂商 GPU 价格与硬件选型
- 查看 Transformer 模型内部结构（注意力/MoE/多模态路径）

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L13: LLM Explorer is a static, source-backed workspace for inspecting modern language-model architectures and turning th
> L19: 3. **Will it fit?** Compare required memory with per-device and aggregate topology constraints across NVIDIA, AMD, 
> L21: 5. **What will the selected GPU cost?** Show a cloud rate only when a dated provider offering maps to that exact ha

## 星数曲线

```mermaid
xychart-beta
    title "isEmmanuelOlowe/llm-explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b4174cb3d052` · [字段定义](../../DATASET.md)*
