# proflead/copilot-agent-library

⭐ 21 · Shell · MIT · 推送 2026-06-18 · [GitHub](https://github.com/proflead/copilot-agent-library) · 个人维护

**36 个 GitHub Copilot 自定义 agent 定义文件集合，即取即用**

提供 36 个生产就绪的 GitHub Copilot 自定义 agent（.agent.md 格式），按编排、全栈开发、语言专家、测试质量、设计 UI/UX、生产力、DevOps、调试、集成 9 大类组织，覆盖 Python/Rust 专家、代码审查、安全审计、Figma 转 HTML、多 agent 协调等场景。使用方式为下载 agent 文件复制到 ~/.github/agents/ 或工作区 .github/agents/，通过 CLI（copilot agent run）或 VS Code 聊天（@agent-name）调用，可按需修改定制。MIT 许可，接受 PR 贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 36 个 .agent.md 格式 agent，按 9 个类别组织
- 支持 CLI 与 VS IDE 两种调用方式
- 提供单 agent、多 agent 编排、设计转代码等工作流示例
- Orchestrator agent 可将任务委派给多个专业 agent

## 适用场景

- 为 GitHub Copilot 添加特定语言或领域的编码助手
- 通过 Orchestrator 协调多个 agent 完成完整功能开发
- 复用现成 agent 定义（代码审查、安全审计、测试生成）再按团队需求定制

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A comprehensive collection of **36 production-ready custom GitHub Copilot agents** for developers, teams, and organi
> L14: 2. **Download the agent file** (`.agent.md`) to your local machine
> L21:  copilot agent run agent-name "Your task here"

## 星数曲线

```mermaid
xychart-beta
    title "proflead/copilot-agent-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b62a137fa831` · [字段定义](../../DATASET.md)*
