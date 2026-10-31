# kbeaugrand/SemanticKernel.Assistants

⭐ 114 · C# · MIT · 推送 2025-11-21 · [GitHub](https://github.com/kbeaugrand/SemanticKernel.Assistants) · 个人维护

**Semantic Kernel 的 Assistants 框架：本地运行助手，不依赖 OpenAI Assistant API**

构建在 Microsoft Semantic Kernel 之上的 Assistants 框架，以 NuGet 包分发。提供基于 SK 插件的助手、多助手对话、AutoGen 双助手协作（NL 2 Code + CodeInterpreter，通过 Docker 容器执行 Python 代码）等场景。助手在本地运行 planner 与插件，不依赖 OpenAI Assistant API；通过 SK 连接器（如 Ollama connector）可接入自有模型并在本地托管。助手以 YAML 描述文件定义，代码中实例化并创建对话线程调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 不依赖 OpenAI Assistant API，本地运行 planner 与插件
- 支持 SK 插件助手、多助手对话、AutoGen 代码执行场景
- 通过 Ollama connector 接入自有模型
- YAML 定义助手，C# 实例化与线程调用

## 适用场景

- 在 .NET 应用中构建多助手对话能力
- 用自有模型（如 Ollama）替代 OpenAI 托管助手
- 搭建自然语言转代码并沙箱执行的 AutoGen 流程

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: This is assistant proposal for the Semantic Kernel.
> L22: **Semantic Kernel (SK)** is a lightweight SDK enabling integration of AI Large

## 星数曲线

```mermaid
xychart-beta
    title "kbeaugrand/SemanticKernel.Assistants 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-31 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `00a77787aa66` · [字段定义](../../DATASET.md)*
