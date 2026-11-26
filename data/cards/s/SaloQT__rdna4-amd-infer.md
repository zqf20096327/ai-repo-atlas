# SaloQT/rdna4-amd-infer

⭐ 4 · C · 推送 2026-11-24 · [GitHub](https://github.com/SaloQT/rdna4-amd-infer) · [官网](https://saloqt.github.io/rdna4-amd-infer/) · 个人维护

**面向 RX 9070 XT 的本地 LLM 推理引擎，免装 Windows ROCm**

基于 Han Wang 的 C11 引擎 hanw/amd.c 的移植分支：面向 AMD Radeon RX 9070 XT（RDNA4/gfx1201），新增 Windows 11 WDDM 支持（无需安装系统级 ROCm）并添加 310 个自定义 gfx1201 GPU 内核。读取 GGUF v3 模型量化文件，经 ie-serve 提供 OpenAI 兼容 API，支持 DSpark 短清单、最长 256K 上下文、零 VRAM WMMA ViT 图像输入，README 附 52 轮优化基准表、实时演示视频与 PowerShell 启动脚本。上游代码因无 LICENSE 文件而未另行授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Windows 11 WDDM 直接运行，无需安装系统级 ROCm
- 310 个自定义 gfx1201 内核（含 6 个 RDNA4 WMMA 视觉内核）
- OpenAI 兼容的 ie-serve API 与 GGUF v3 模型支持
- 16 GB 单卡支持填满 256K 上下文并内置 DSpark

## 适用场景

- 在单张 RX 9070 XT 16GB 上本地运行 Inkling-2-Mini 等模型
- Windows 环境下不想安装 ROCm 的本地推理部署
- 通过 OpenAI 兼容 API 接入 Open WebUI 等前端聊天

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # rdna4-amd-infer: RX 9070 XT LLM Engine
> L3: **Fast local LLM inference engine for AMD Radeon RX 9070 XT (RDNA4 / `gfx1201`) built on top of Han Wang's `hanw/amd
> L5: Base C11 engine & verified core by `hanw/amd.c` · Windows WDDM port + 310 custom `gfx1201` kernels + DSpark/shortlis


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `72070e8ddc2d` · [字段定义](../../DATASET.md)*
