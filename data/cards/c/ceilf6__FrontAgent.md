# ceilf6/FrontAgent

⭐ 120 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ceilf6/FrontAgent) · [官网](https://marketplace.visualstudio.com/items?itemName=ceilf6.frontagent) · 个人维护 · 中文 README

**面向前端工程的 AI 编码 Agent 平台，SDD 约束下生成并验证 Web 代码**

开源前端 AI 编码 Agent，以 CLI、VS Code 插件、Electron 桌面端和 stdio MCP 服务器四种形态运行。采用规划/执行两阶段架构：先按 SDD 规格生成结构化执行计划，再分阶段执行代码生成、浏览器感知验证、shell 与 git/gh 仓库流程，带自愈错误恢复与最小补丁修改。内置 BM25+嵌入的混合 RAG、模块依赖追踪与事实记忆以减少路径幻觉；规划器蒸馏为 Qwen Coder LoRA 适配器（Hugging Face 发布），可不调用大型 LLM API 生成执行计划。MCP 模式仅暴露 6 个上层工具，内部文件/shell/浏览器工具不直接外露，支持宿主 Sampling 或直接 LLM 回退。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规划/执行两阶段架构，SDD 硬约束与阶段内错误恢复
- BM25+嵌入混合 RAG、模块依赖追踪与事实记忆减少路径幻觉
- 蒸馏 Qwen Coder 规划模型（Hugging Face），本地生成执行计划
- CLI / VS Code 插件 / Electron 桌面端 / MCP 服务器四种运行形态

## 适用场景

- 在终端或 VS Code 中让 Agent 按规格生成、修改并验证 React/TS 前端代码
- 作为本地 MCP 服务器接入 Claude Desktop、Cursor、Codex 等宿主复用前端 Agent 能力
- 用蒸馏规划模型在本地低成本生成前端执行计划

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: FrontAgent is an open-source AI coding agent for frontend engineering. It helps teams build, modify, validate, and 
> L20: - Generate and refactor React, TypeScript, Vite, Tailwind CSS, and modern web UI code from structured execution pla
> L25: - Use distilled Qwen Coder planner models from Hugging Face for local or lower-cost frontend execution planning.

## 星数曲线

```mermaid
xychart-beta
    title "ceilf6/FrontAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 119 --> 121
    line [120, 120]
```

2026-10-18 120 → 2026-10-29 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `77b1b4c0b48a` · [字段定义](../../DATASET.md)*
