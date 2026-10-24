# sbryngelson/ANEForge

⭐ 65 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/sbryngelson/ANEForge) · [官网](https://aneforge.com) · 个人维护

**在 Apple 神经引擎上直接训练与运行神经网络的 Python 运行时**

面向 Apple Silicon 开发者的 ANE 推理与训练运行时：绕过 CoreML，将张量图编译为单一 ANE 程序，通过 aned 私有栈调度，支持前向、反向与 Adam 更新全部在引擎上运行。可加载 Hugging Face Hub 模型或 GGUF 权重，运行 LLM 解码、Whisper 语音转文字、嵌入与重排序等；提供 28 个 ANE 目标的交叉编译与延迟估计。限制：研究项目，依赖可能变动的私有框架符号，需 macOS 14+ 与 Xcode 命令行工具，e5rt 分发垫片需本机源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 绕过 CoreML 直接编译到 ANE，训练（前向/反向/Adam）与推理均在引擎上运行
- 从 Hugging Face Hub 或 GGUF 加载 LLM，驻留 KV-cache 解码与投机解码
- 58 个融合算子 + 19 个原生桥接算子，int8/int4/fp16 权重压缩
- 28 个 ANE 目标（M1-M5）交叉编译与免运行的延迟估计

## 适用场景

- 在 Mac 神经引擎上直接运行 LLM、Whisper、嵌入等模型而不经 CoreML
- 在 ANE 上从头训练或微调小型神经网络
- 为不持有的 Apple 芯片交叉编译 ANE 程序并估计延迟

## 场景标签

`语音识别` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L16: **Train and run neural networks directly on the Apple Neural Engine, from
> L27: CPU or GPU, and it gives you no way to train there. ANEForge skips it: it compiles
> L28: a tensor graph into one ANE program and dispatches that program through the same

## 星数曲线

```mermaid
xychart-beta
    title "sbryngelson/ANEForge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-24 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `898b41d5009b` · [字段定义](../../DATASET.md)*
