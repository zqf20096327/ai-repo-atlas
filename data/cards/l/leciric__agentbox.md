# leciric/agentbox

⭐ 17 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/leciric/agentbox) · [官网](https://agentbox.linting.dev) · 个人维护

**在本地电脑运行 AI 编程 agent 团队并逐一隔离的开源应用**

用 Electron 打包的桌面应用，在本机 VM 内并行运行多个 AI 编程 agent：每个 agent 获得独立 Linux 容器（独立网络、Docker、端口与数据库）、独立 git 分支/worktree、带浏览器的桌面环境，可在界面实时观看或接管操作。通过一个 lead 聊天创建与指挥 agent，工作产物附录像、截图、diff 与 pull request 供审查合并，并保留项目记忆供后续 agent 使用。支持手机 QR 配对跟进。依赖 /dev/kvm，远程环境依赖非开源的 hub 程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每个 agent 独立 Linux 容器：独立网络、Docker、端口，互不冲突
- 每个 agent 配桌面与浏览器，可实时观看并一键接管
- 工作附录像/截图/diff/PR 作为审查依据，附带步骤时间线
- 六种 AI 编程 CLI（Claude Code/Codex/OpenCode/Cursor/Gemini CLI/Copilot CLI）共用一个聊天指挥

## 适用场景

- 同时让多个 agent 并行处理不同任务而互不干扰
- 通过录像与截图核验 agent 实际完成了工作再合并
- 在本地环境中运行 agent，代码不离开本机
- 用手机远程跟进 agent 进度并回答其提问

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3:  An open-source app that runs a team of AI coding agents on your own computer, each with a Linux machine of its own,
> L45: - **Six AI tools, your own accounts.** Claude Code, Codex, OpenCode, Cursor, Gemini CLI and GitHub Copilot CLI in t
> L63: Each of these runs coding agents in parallel; they differ in what an agent gets, and in who


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `394ebe8568ad` · [字段定义](../../DATASET.md)*
