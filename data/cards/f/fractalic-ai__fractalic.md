# fractalic-ai/fractalic

⭐ 52 · Python · MIT · 推送 2025-11-11 · [GitHub](https://github.com/fractalic-ai/fractalic) · [官网](https://fractalic.ai/docs) · 组织维护

**用 Markdown+YAML 构建、运行并版本化多模型 AI 工作流的开发框架**

Fractalic 是一个面向开发者的 LLM 编排框架：工作流以单个可执行 Markdown 文件定义，用 3-6 行 YAML 操作（@llm/@shell/@run/@import/@return）替代胶水代码，文档本身即运行时。通过 LiteLLM 支持 100+ 模型与供应商（含本地模型），支持 MCP 服务器、Python 模块与 shell 命令作为工具，提供上下文按区块精确控制与逐步执行审计日志。附带 Fractalic Studio IDE、Publisher Docker 部署系统与 MCP/工具市场。提供 Docker 镜像、源码构建与 pip 包三种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单个可执行 Markdown 文件即工作流运行时，无胶水代码
- @llm/@shell/@run/@import/@return 五类确定性操作，支持模块化参数传递
- LiteLLM 集成支持 100+ 模型与供应商，含本地模型
- 完整 MCP 支持（schema 缓存、OAuth 2.0）与 Python 模块作工具
- Fractalic Studio IDE：会话视图、diff 检查器、调试与部署工具

## 适用场景

- 用自然语言加 YAML 在一份 Markdown 里编写多步骤 AI 工作流
- 串联 MCP 服务、Python 函数与 shell 命令做自动化任务（如搜索→写入 Notion）
- 对 AI 工作流做 git 版本化跟踪与逐步执行审计
- 通过 Docker 一键部署带 UI/API/AI 服务器的工作流服务

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: Design, run and evolve multi‑model AI workflows in one executable Markdown file—no glue code—with precise context co
> L113: - **Multi-model workflows**: Switch between LLM models and providers in the same document.
> L124: - `@llm` – Sends specified blocks of content to any supported language model, including local models.

## 星数曲线

```mermaid
xychart-beta
    title "fractalic-ai/fractalic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4b32c3c5fa10` · [字段定义](../../DATASET.md)*
