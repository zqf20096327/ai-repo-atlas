# John99101/claude-code-project-template

⭐ 4 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/John99101/claude-code-project-template) · 个人维护

**给 Claude Code 用户一键生成项目配置与安全钩子的工具包**

面向 Claude Code 开发者的项目配置生成器：一条命令检测技术栈后写入 CLAUDE.md、规则、权限、hooks、skills、agents 与 MCP 配置，并附带安全防护钩子、完成前运行测试的 done gate、依赖名核查，以及 /pr、/start-issue、/handoff 等工作流命令。支持以插件方式安装，或用 Python 安装脚本装入单个项目、全设备或新仓库，支持 Linux、macOS 与 Windows，要求 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令检测技术栈并生成 CLAUDE.md、规则、hooks、skills、agents 与 MCP 配置
- guard 钩子拦截破坏性命令与密钥文件写入，done gate 在结束前运行相关测试
- dependency check 核查 npm、PyPI、crates.io 上是否存在该包名
- 提供 /pr、/start-issue、/handoff、/spec 等工作流命令与四个专项 agent

## 适用场景

- 新项目快速生成 Claude Code 项目级配置，免去手工编写
- 限制 AI 编码助手的危险命令、伪造测试通过与编造包名行为
- 让团队通过 git 共享统一的 Claude 配置与提交/PR 规范

## 场景标签

 · 领域:开发者工具/AI 编码辅助

## 证据(README 行号)

> L5: One command, and Claude reads your repo, asks a few multiple-choice questions, and writes the whole setup for you:
> L6: `CLAUDE.md`, rules, permissions, hooks, skills, agents and MCP servers, all matched to your real stack.
> L90: > **Requirements:** Claude Code and Python 3.8+ (the hooks use only the standard library). Tested on every push on 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `fe5d6e3591ff` · [字段定义](../../DATASET.md)*
