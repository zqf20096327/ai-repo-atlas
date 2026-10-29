# eliranwong/AMD_iGPU_AI_Setup

⭐ 28 · 推送 2026-06-17 · [GitHub](https://github.com/eliranwong/AMD_iGPU_AI_Setup) · 个人维护

**AMD 核显设备 AI 开发环境搭建指南与速度测试记录**

面向 AMD iGPU 设备（以 GPD Pocket 4 / Ryzen AI 9 HX 370 为测试机型）的 Linux AI 开发环境搭建教程仓库：记录 BIOS 显存分配设置、Ubuntu 24.04 安装、ROCm 7.2.1 与 Vulkan 驱动安装、gfx1150 环境变量配置，以及 Docker、Perplexica、SearXNG、Ollama、llama.cpp（ROCm/Vulkan 双后端编译）、Open Notebook、Fabric、AgentMake AI 等组件的安装步骤，并附速度测试结果。本仓库本体为文档与命令记录，不含可安装的软件产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 BIOS 显存设置到 ROCm/Vulkan 驱动的完整 iGPU 配置流程
- 提供 llama.cpp 的 ROCm 与 Vulkan 两种后端编译命令（gfx1150）
- 记录 Ollama、Perplexica、SearXNG、Open Notebook、Fabric、AgentMake AI 等组件安装步骤
- 测试机型上 Vulkan 后端可运行 70b 模型（-ngl 99）并附速度测试结果

## 适用场景

- 我想在 AMD 核显笔记本上搭建本地 LLM 运行环境
- 我需要 ROCm 在 gfx1150 等 APU 上的配置与排错参考
- 我想对比 iGPU 上 ROCm 与 Vulkan 后端的运行方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: AMD-iGPU-device setup for AI development. We also record some speed test results.
> L9: Device: GPD Pocket 4
> L63: # Install ROCM

## 星数曲线

```mermaid
xychart-beta
    title "eliranwong/AMD_iGPU_AI_Setup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `52cf559d282b` · [字段定义](../../DATASET.md)*
