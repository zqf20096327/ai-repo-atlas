# mnemosyne-systems/orangu

⭐ 50 · Rust · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/mnemosyne-systems/orangu) · [官网](https://mnemosyne-systems.github.io/orangu/) · 组织维护

**全离线的终端 AI 编程环境，含自研 Rust GGUF 推理引擎**

纯 Rust 端到端实现的三层本地 AI 编码栈：orangu 终端编码/代码评审环境（交互式双栏 /review、LLM 驱动的带置信度 /auto_review、/create_patch 生成补丁）、orangu-coordinator 按需模型管理与代理、orangu-server 原生 GGUF 推理引擎（不依赖 llama.cpp/Python），支持 CPU/Vulkan/Metal/CUDA/ROCm，服务 17 个模型家族并提供 OpenAI 兼容 API 与文生图。另含 Tree-sitter 知识图谱、语义搜索、Git/构建自动化、MCP 客户端与 Agent 技能机制。面向重视隐私与离线环境的开发者，GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Rust 三层栈：终端环境 + 模型协调器 + 原生 GGUF 推理引擎
- 交互式 /review 与带置信度评分的 LLM 自动评审（/auto_review）
- CPU/Vulkan/Metal/CUDA/ROCm 硬件加速，多重量化格式支持
- Tree-sitter 知识图谱、语义搜索、MCP 客户端与 SKILL.md 技能发现

## 适用场景

- 在无网络或涉密环境中进行本地 AI 辅助编码与代码评审
- 把评审发现经 /create_patch 直接生成并应用补丁
- 用本地 GGUF 模型搭建私有 chat/embedding/文生图推理服务

## 场景标签

`代码审查` `推理引擎` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **orangu** is a local, workspace-aware, tool-driven coding environment for your terminal.
> L10: 3. **`orangu-server`** - Native, pure-Rust GGUF inference engine (**no llama.cpp, no ggml, no Python**).
> L108: - **`/review` (Interactive Review)**: Full-screen two-pane reviewer (diff vs. checklist). Mark files approved/reje
> L121: - **Single-File Bundles**: Package the server and a model into a standalone binary with `orangu-server bundle <mod

## 星数曲线

```mermaid
xychart-beta
    title "mnemosyne-systems/orangu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8cb564d80c98` · [字段定义](../../DATASET.md)*
