# KaruroChori/comfyui-bun-client

⭐ 16 · TypeScript · BSD-3-Clause · 推送 2025-11-24 · [GitHub](https://github.com/KaruroChori/comfyui-bun-client) · [官网](https://karurochori.github.io/comfyui-bun-client/) · 个人维护

**面向 Bun 运行时的 ComfyUI TypeScript 客户端库**

专为 TypeScript 与 Bun 运行时设计的 ComfyUI 客户端库，用于无头（headless）操作与自动化。提供对 ComfyUI 全部 REST 端点接近 1:1 的封装、带生命周期回调的 job 抽象、部署与产物收集工具、支持静态类型检查的 TS 工作流编写器，以及把现有 ComfyUI 工作流转换为 TS 代码的代码生成器。另附带小型 CLI，可从 ComfyUI 实例生成类型、从图像元数据生成工作流代码。不提供 JS 发行版，也无 npm 分发计划，仅通过 git 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ComfyUI REST 端点接近 1:1 的 TypeScript 封装
- 带生命周期回调的 job 抽象
- TS 工作流编写器与静态类型检查支持
- 工作流→TS 代码的代码生成器与配套 CLI

## 适用场景

- 用脚本自动化调用 ComfyUI 生图任务
- 以 TS 代码编写并静态检查 ComfyUI 工作流
- 把现有 ComfyUI 工作流转换为可维护的 TS 代码

## 场景标签

`图像生成` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L4: > This library is specifically designed to work with typescript and the bun runtime.
> L11: - A mostly 1-to-1 wrapper for all the REST endpoints defined by ComfyUI.

## 星数曲线

```mermaid
xychart-beta
    title "KaruroChori/comfyui-bun-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5d63282bbe87` · [字段定义](../../DATASET.md)*
