# Makdok/llama.cpp-inkling2-amd

⭐ 7 · C++ · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Makdok/llama.cpp-inkling2-amd) · 个人维护

**在 AMD RDNA3 GPU 上加速 Inkling 2 Mini 推理的 llama.cpp 分支**

基于 Unsloth llama.cpp 发布版 b12568 的分支，通过为 Inkling 2 Mini（26.4B MoE）修改注意力偏置处理、融合内核、调度上传与 DSpark drafter，使其在 ROCm/HIP 下的 RDNA3.0 GPU（gfx1100-gfx1103）上获得更高的提示读取与生成速度。作者声明未与 ggml-org、Unsloth 或 Thinking Machines 关联；代码路径仅在 RDNA3.0 GPU 上激活，其他 GPU 运行原版内核，且仅在一块 RX 7900 XTX 上构建和测得数据。配套提供专用 GGUF 模型文件与构建/检查脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- RX 7900 XTX 上实测提示读取约 3000 tok/s、生成约 110 tok/s，上下文最高 262144
- 融合内核将每 token 内核启动数从约 8100 降至约 1215
- 附带 DSpark drafter 与多会话 slot 并行处理改动
- 提供配套 GGUF 模型文件与 scripts/inkling2-amd 构建检查脚本

## 适用场景

- 在 RX 7900 XTX 上本地运行 Inkling 2 Mini 的长上下文推理
- 对比 Unsloth 发布版评估 AMD RDNA3 上的提示处理速度
- 为该模型搭配 DSpark drafter 做投机解码

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: > **This is not upstream llama.cpp.** This branch is the Unsloth llama.cpp release
> L17: > Inkling 2 Mini fast on AMD GPUs under ROCm/HIP. It is
> L29: Inkling 2 Mini (Thinking Machines, 26.4B parameters, mixture of experts with 128 experts and 8 per token, 24 stored

## 星数曲线

```mermaid
xychart-beta
    title "Makdok/llama.cpp-inkling2-amd 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 4 --> 8
    line [5, 7]
```

2026-11-26 5 → 2026-11-27 7（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `0b35ede06e84` · [字段定义](../../DATASET.md)*
