# charlesjones-dev/ai-agent-plugins

⭐ 35 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/charlesjones-dev/ai-agent-plugins) · [官网](https://charlesjones.dev) · 个人维护

**面向 Claude Code/Codex/Cursor 的 13 个开发工作流插件集**

为 AI 编码代理提供命令插件的集合，覆盖 git 工作流（.gitignore 生成、preflight 检查、提交推送建 PR）、代码审计（无障碍/许可证/技术债/性能/安全）、发布检查（Swift/Xcode）、团队知识库（以 Claude Code rules 形式存于 git）与 Azure DevOps 集成。13 个插件均运行于 Claude Code，其中 8 个遵循 Agent Plugins 1.0 格式，另可在 Codex 与 Cursor 中加载。通过各平台 marketplace 命令或本地目录复制安装，可仅装所需插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个插件以命令形式提供（如 /git-init、/security-audit）
- git preflight 检查覆盖 typecheck、lint、format、安全与测试
- 审计插件支持带参数的无人值守定时运行
- 8 个插件遵循 Agent Plugins 1.0 标准格式，可被其他支持的代理加载

## 适用场景

- 在 Claude Code 中用命令完成 git 提交、推送与建 PR
- 开发过程中对代码做安全、无障碍、性能与技术债审计
- 把团队知识库存入 git 并让代理按需加载

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Plugins for git and project workflows, code audits and release checks. All 13 run in Claude Code, and 8 of them also
> L13: Each skill is a command you run by name, such as `/git-init` in Claude Code and Cursor. Interactive skills ask for 
> L80: The plugins that run in Codex and Cursor follow the Agent Plugins 1.0 format, with a `plugin.json` at the root of e

## 星数曲线

```mermaid
xychart-beta
    title "charlesjones-dev/ai-agent-plugins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04a1c61963fb` · [字段定义](../../DATASET.md)*
