# benmaster82/Pith_OS

⭐ 3 · Assembly · MIT · 推送 2026-11-27 · [GitHub](https://github.com/benmaster82/Pith_OS) · 个人维护

**在 Linux 与裸机 x86-64 汇编上运行 LiquidAI LFM 模型的推理引擎**

以 NASM x86-64 汇编实现的 LiquidAI LFM3-1.7B（Q4_K_M GGUF）与 LFM2.5-350M（BF16）推理运行时，无 libc、无 Python（Python 仅用于构建与验证）。提供两种形态：Linux 可执行文件与可从 BIOS/UEFI 引导的独立操作系统 ISO，启动后进入 Unicode 聊天控制台。实现 BPE 分词器、AVX2/FMA 内核、最多 16 线程并行、block prefill 与采样；输出经与 Transformers FP32 参考实现逐块核对。MIT 许可，构建需 NASM、GNU ld、GNU make 与 Python tokenizers 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 libc、无 Python 运行时的 x86-64 NASM 推理引擎
- 可从 BIOS/UEFI 引导为独立操作系统，进入 Unicode 聊天控制台
- AVX2/FMA 内核，支持最多 16 CPU 并行与 32,768 位置上下文
- 分词器与模型输出经 FP32 参考实现逐块验证

## 适用场景

- 在裸机 PC 上不装系统直接从 U 盘引导进行本地 LLM 对话
- 在 Linux 终端运行 LiquidAI LFM 模型做文本生成实验
- 研究 LLM 推理内核的汇编级实现与数值验证方法

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3:  LiquidAI language models in x86-64 NASM, on Linux and as a standalone operating system.
> L8:  Runs on Linux and on bare metal with BIOS or UEFI
> L28: Pithos CORE runs LiquidAI LFM3-1.7B, the main model, from its Q4_K_M GGUF, and LFM2.5-350M, the compact model, from


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `471c7f8c855e` · [字段定义](../../DATASET.md)*
