# windagency/valora.ai

⭐ 24 · TypeScript · 推送 2026-10-13 · [GitHub](https://github.com/windagency/valora.ai) · 组织维护

**AI 辅助软件开发的多 Agent 编排与生命周期控制层**

开源的 AI 开发编排器，以 CLI 驱动结构化软件生命周期：规划、实现、验证、测试、安全审查、评审到创建 PR。它协调产品、架构、工程、质量、安全等专业化角色，每个角色可配置独立的指令、工具、上下文与模型。模型层可替换，支持 Anthropic、OpenAI、Google、xAI、本地模型及 OpenAI 兼容端点；支持 MCP 外部工具集成、插件扩展、Git worktree 并行开发、项目记忆与上下文工程（AST 解析、过滤、压缩）。强调人保留控制权与多层安全治理（凭据保护、危险命令检测、提示注入防护等）。npm 全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 编排覆盖规划到 PR 的结构化生命周期
- 模型层可替换：Anthropic/OpenAI/Google/xAI/本地模型/OpenAI 兼容端点
- MCP 集成外部工具（GitHub/Playwright/Figma/Terraform 等）
- 安全治理：凭据脱敏、危险命令检测、提示注入防护、供应链控制

## 适用场景

- 把一个功能需求从规划到 PR 走完整工程流程
- 用本地模型（如 qwen3:8b）执行 AI 开发工作流
- 通过专业角色 Agent 做代码评审与安全审查
- 用 Git worktree 隔离多方案并行探索

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L22: **VALORA is an open-source AI development orchestrator.**
> L177: VALORA sits between the developer, the development workflow, AI agents, models, tools, and the codebase.
> L318: VALORA does not depend on a single AI provider.

## 星数曲线

```mermaid
xychart-beta
    title "windagency/valora.ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8ccca7a77c27` · [字段定义](../../DATASET.md)*
