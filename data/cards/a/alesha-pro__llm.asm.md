# alesha-pro/llm.asm

⭐ 159 · Assembly · MIT · 推送 2026-11-25 · [GitHub](https://github.com/alesha-pro/llm.asm) · 个人维护

**纯 x86-64 汇编实现的三个 LLM 项目：推理、裸机 OS、训练器**

三个完整子项目均以 100% NASM 汇编编写，零 C、零 libc、零运行时依赖：①14 KB 的 Qwen3-0.6B 静态 Linux ELF 推理程序，内置 BPE 分词器、AVX2+FMA GEMM 引擎与多轮 KV-cache 聊天 REPL；②24 KB 可启动裸机 SMP 内核，不经 Linux/Windows 直接运行多轮对话；③32 KB 从零实现的 Mini-GPT 训练器，含解析式反向传播、AdamW 与实时盲文 TUI。构建用 nasm+make，需 AVX2/FMA/F16C CPU，权重导出需一次性 python3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个子项目全部纯汇编，17,252 行，零运行时依赖
- Qwen3-0.6B Q8_0 推理程序仅 14,712 字节，支持 --chat 多轮 KV-cache
- 可启动裸机 OS（Multiboot→Long Mode→SMP→VGA/PS2/COM1），74–94 ms 启动
- 从零 Mini-GPT 训练器带解析反向传播、AdamW 与实时 80x24 盲文 TUI

## 适用场景

- 在无任何运行时依赖的 Linux 环境运行 Qwen3-0.6B 本地推理
- 用 QEMU 或实体机从裸机启动直接跑 LLM 多轮对话
- 从零训练小型 GPT 并在终端实时观察训练过程

## 场景标签

`推理引擎` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: **Three complete LLM projects written in 100% pure x86-64 NASM assembly.**
> L12: |**01-qwen3-inference/**|`build/asm-llm`|**14,712 B** *(14,008 B `FAST_Q8=0`)*|**0**|Static Linux ELF running `Qwen
> L106: - **CPU:** x86-64 with **AVX2 + FMA + F16C** (Intel Haswell / AMD Excavator or newer).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `928fa7562af5` · [字段定义](../../DATASET.md)*
