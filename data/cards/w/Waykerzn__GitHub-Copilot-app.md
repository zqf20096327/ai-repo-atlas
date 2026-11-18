# Waykerzn/GitHub-Copilot-app

⭐ 62 · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/Waykerzn/GitHub-Copilot-app) · 组织维护

**开发者用的 agent 驱动桌面端：跨仓库运行与托管 Copilot 代理**

GitHub 官方的桌面应用（本仓库为其公开主页，© GitHub, Inc. 保留所有权利），定位为 agent-native 的软件工作管理端：查找待做工作、启动并引导本地与云端 Copilot 代理会话、通过 Canvas 查看与编辑代理工作、用 My Work 汇总会话/issue/PR、以 Automations 调度重复任务、用 Agent Merge 推进 PR 合并。本地会话运行于隔离的 git worktree。前置要求为 Git 与任一 Copilot 订阅，也支持自带密钥（BYOK）接入自有模型提供方。仓库本身仅用于下载发布版、报 bug 与讨论，不包含源代码构建说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地会话各自运行在隔离的 git worktree，云端会话运行在 GitHub 托管的隔离环境
- Canvas 将代理的计划、终端、diff 与工作流状态呈现为可检查、可编辑的界面
- Automations 将重复提示与工作流转为定时/后台任务；Agent Merge 推进 PR 审查与合并
- 无 Copilot 订阅时支持 BYOK 接入自有模型提供方

## 适用场景

- 并行让多个 Copilot 代理分别调查 bug、实现 issue、处理审查意见
- 在同一控制中心跨仓库管理会话、issue 与 pull request
- 把重复性提示和工作流设为定时后台任务自动执行

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: The GitHub Copilot app is an agent-native desktop experience for finding, running, steering, and landing software wo
> L15: The app is built for parallel agent-driven development. Each local session runs in its own isolated git worktree, a
> L13: The GitHub Copilot app is an agent-native desktop experience for managing software work from idea to pull request. 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `ef82cf6db0cd` · [字段定义](../../DATASET.md)*
