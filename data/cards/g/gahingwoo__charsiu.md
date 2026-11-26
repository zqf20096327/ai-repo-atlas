# gahingwoo/charsiu

⭐ 10 · C · GPL-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/gahingwoo/charsiu) · 个人维护 · 中文 README

**RK3576 NPU 上的主线上游 LLM 运行时，绕过厂商库**

在主线上游 Linux 内核下通过 rocket DRM-accel 驱动直接操作 RK3576 NPU 的开源 LLM 推理运行时，执行路径不含厂商库，默认开启投机解码。加载 llama/qwen/gemma/phi 等系列 gguf 模型文件，视觉依赖 llama.cpp mmproj 文件，语音依赖 whisper.cpp 文件。安装提供脚本、apt 与 .deb 三种途径，支持 Windows on Arm；RK3588 支持在开发分支上尚未在硬件上运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过主线上游 rocket 驱动运行 NPU，执行路径不含厂商库
- 默认开启投机解码，输出与关闭时一致
- 加载 llama/qwen2/qwen3/gemma3/phi3 等多种 gguf 模型文件
- CHARSIU_NPU=0 可回退到仅 CPU 运行

## 适用场景

- 在 RK3576 开发板上做本地大模型推理
- 对比主线上游驱动与厂商 rkllm 栈的性能表现
- 在 Windows on Arm 设备上通过 NPU 驱动运行 LLM

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: An open LLM runtime for the RK3576 NPU on a mainline Linux kernel. It drives the
> L72: It loads llama, qwen2, qwen3, gemma3, gemma4, phi3 and smollm3 gguf files.
> L81: An RK3576 board (tested on the ArmSoM CM5-IO and the Radxa ROCK 4D) and a


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7010e590abd0` · [字段定义](../../DATASET.md)*
