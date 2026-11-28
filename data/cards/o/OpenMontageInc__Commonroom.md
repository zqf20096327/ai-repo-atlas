# OpenMontageInc/Commonroom

⭐ 6 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/OpenMontageInc/Commonroom) · 组织维护

**让用户与多个 AI 编码代理共享同一工作区的桌面工具**

Commonroom 是一个 Electron 桌面应用，为每个项目文件夹提供一间“房间”：用户与 Claude Code、Codex、Antigravity 等 AI 编码代理共用一个会话，每个代理可见所有消息并自行决定是否回复，可 @mention 定向对话。它驱动本机已安装并登录的官方 CLI 工具，使用用户现有订阅而非 API key；提供工具自动发现、lead agent 选择、聊天内审批，并提示代理以完全自主模式运行的风险。Windows 提供安装包，macOS/Windows 可从源码运行（Python 3.10+，桌面壳需 Node.js 20+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多个 AI 编码代理共享同一会话，可互相与用户对话
- 使用现有订阅通过官方 CLI 运行，无需 API key
- 自动发现本机已安装的 AI 工具并选择 lead agent
- 工具审批请求直接出现在聊天中

## 适用场景

- 让 Claude Code 与 Codex 在同一项目里协作写代码
- 为每个项目维护独立的代理会话与历史
- 不想为每个代理单独配置 API key

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L11: folders. You and any mix of AI coding agents — Claude Code, Codex, Antigravity,
> L24: - **One chat per project.** Pick a folder; Commonroom keeps that room's history, members and sessions.
> L44: 2. Download and run the latest **Commonroom Setup** from Releases.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `836c49dba951` · [字段定义](../../DATASET.md)*
