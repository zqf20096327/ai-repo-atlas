# ariannamethod/notorch

⭐ 29 · C · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/ariannamethod/notorch) · [官网](https://x.com/@olegataefff) · 个人维护

**纯 C 实现的神经网络框架：训练并运行 LLM 等模型**

以 notorch.h/notorch.c 两个文件为核心的纯 C 神经网络框架，无 Python 依赖，提供张量、显式自动微分 tape、SGD/Adam/AdamW 及 Chuck 优化器，内置构建 transformer 所需算子（GQA 注意力、RoPE、SwiGLU、BitNet 等）并通过数值梯度校验。附带 GGUF 推理 harness，可路由 llama/qwen2/qwen3/gemma3/mamba 等模型家族，支持 CPU/Metal/CUDA 路径；另含字符级 LLaMA 训练器与 LoRA SFT 示例。面向希望阅读源码理解机制、在非云环境训练或向 C/C++ 应用嵌入推理的开发者。核心张量上限 268M 元素。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心仅 notorch.h/notorch.c 两文件，数秒内完成编译
- 显式 tape 式反向自动微分与多种优化器（含自适应的 Chuck）
- GGUF harness 路由 llama/qwen/gemma3/mamba 等模型家族，支持 CPU/Metal/CUDA
- 内置算子均通过数值梯度校验

## 适用场景

- 在无 Python 环境的机器上训练小型模型
- 把 GGUF 量化模型作为单一 C 二进制运行或终端对话
- 将神经网络推理以 C 库形式嵌入 C/C++ 应用
- 通过可读源码学习张量、autograd 与训练循环实现

## 场景标签

`微调` `模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: **NOTORCH** is a complete neural network framework written in pure C — it **runs** models and it **trains** them.
> L141: The core is notorch.h and notorch.c.

## 星数曲线

```mermaid
xychart-beta
    title "ariannamethod/notorch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-30 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `327aad74f04f` · [字段定义](../../DATASET.md)*
