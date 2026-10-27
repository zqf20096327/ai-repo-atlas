# ybubnov/metalchat

⭐ 23 · C++ · GPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/ybubnov/metalchat) · [官网](https://metalchat.readthedocs.io) · 个人维护

**Apple Silicon 上 Metal 加速的 C++ LLM 推理框架与命令行解释器**

用 C++23 编写、基于 Metal 的 LLM 推理框架，同时提供命令行解释器，支持在 Apple Silicon 芯片上运行 Meta Llama、Google Gemma 与 Liquid 模型。既可作为库通过 CMake 导出目标链接使用，也可作为 CLI 与模型交互。安装途径包括 Homebrew tap 与本地 Conan 包构建。README 声明库 API 与 CLI 处于活跃开发中，可能不经弃用通知即变更，已知问题见 issues 页。以 GPLv3 许可分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Metal 加速的 C++23 LLM 推理框架与 CLI
- 支持 Meta Llama、Google Gemma、Liquid 模型
- 可通过 CMake 导出目标（MetalChat::MetalChat）作为库链接
- 支持 Homebrew 与 Conan 两种安装/构建途径

## 适用场景

- 在 Mac 上本地运行 Llama/Gemma/Liquid 模型推理
- 将 LLM 推理能力以 C++ 库形式集成到自己的 Apple Silicon 应用
- 通过命令行与本地模型交互

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: MetalChat is a Metal-accelerated C++ framework and command
> L4: line interpreter for inference of Meta Llama,
> L5: Google Gemma, and Liquid

## 星数曲线

```mermaid
xychart-beta
    title "ybubnov/metalchat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `458e77bf2d26` · [字段定义](../../DATASET.md)*
