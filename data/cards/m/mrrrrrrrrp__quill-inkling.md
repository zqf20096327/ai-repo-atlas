# mrrrrrrrrp/quill-inkling

⭐ 4 · C++ · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/mrrrrrrrrp/quill-inkling) · 个人维护

**面向 Windows+NVIDIA 的 Inkling 2 Mini 本地推理引擎与安装器**

quill 是一个用 C++/CUDA 编写的推理引擎，专门服务于单一模型 Inkling 2 Mini（提供 abliterated 与原版两种安装），运行时不依赖 Python。采用 DFlash2 投机解码与混合 MoE 布局，将部分专家放在 GPU、其余用 CPU AVX2 内核计算；提供 OpenAI 兼容 API 与浏览器聊天页。Rust 编写的 Windows 安装器检测硬件、自动选择设置、下载校验模型与引擎文件，并支持按 12/16 GB 显存档位与显存不足场景缩放参数。源码构建需 Visual Studio 2022 与 CUDA 13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DFlash2 投机解码与 CPU/GPU 混合 MoE 专家布局
- OpenAI 兼容 API（Base URL /v1，支持 tool calls 与 reasoning_effort）
- Rust 安装器检测硬件并自动选择设置，文件校验、断点续装
- 12 GB RTX 40 上 600k 上下文，16 GB 卡提供 1M 上下文与 GPU 视觉编码

## 适用场景

- 在 Windows + RTX 40 机器上本地运行 Inkling 2 Mini
- 通过 OpenAI 兼容 API 接入 OpenCode、pi 等客户端
- 为编码代理提供本地长上下文模型服务
- 需要图像输入的本地多模态推理

## 场景标签

`推理引擎` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: **quill** is an inference engine (C++/CUDA, no Python at run time) written for one model: **Inkling 2 Mini**
> L5: on the CPU. It serves an **OpenAI-compatible API** and a **chat page** in your browser.
> L16: A Windows installer, written in Rust, checks your hardware, picks the settings, downloads and verifies everything,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f401d6f33789` · [字段定义](../../DATASET.md)*
