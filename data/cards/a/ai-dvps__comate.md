# ai-dvps/comate

⭐ 69 · TypeScript · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/ai-dvps/comate) · [官网](https://ai-dvps.github.io/comate/) · 组织维护 · 中文 README

**把 Claude Code 等 Agent 装进桌面的通用任务工作台**

Electron 桌面应用，将 Agent 会话、本地项目文件、浏览器辅助任务与操作审批组织到文件夹支撑的 Workspace 中：用户给出目标，Agent 执行多步工作并在受限操作前暂停等待审批。Agent 后端支持 Claude Code 与 OpenCode，Codex 为实验性（需环境变量开启）；运行需自带模型凭证或已登录的 Agent 账号，应用本身不含免费推理。内置技能管理器可安装/更新 Claude Code、Codex、OpenCode 的 Skills，支持接入 WeCom、飞书等企业工具。提供 macOS/Windows/Linux 安装包，Gitee 有国内镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Claude Code 与 OpenCode 为支持的后端，Codex 实验性可用
- 文件夹支撑的 Workspace 管理多项目与任务上下文
- 内置 skill-manager 通过对话安装/更新 Skills，支持 MCP 与定时自动化
- 受限操作前的可见审批与企业工具（WeCom/飞书）集成

## 适用场景

- 让 Agent 在本地项目文件上完成研究、写作、开发等多步任务
- 通过审批机制控制 Agent 的敏感操作与外部动作
- 在一个桌面应用里管理多个项目的 Agent 会话与技能

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: It brings your Agents, project context, files, browser work, and approvals into one desktop workspace. You can give 
> L21: - **Bring the right Agent to each task.** Use Claude Code or OpenCode as supported backends. Codex support is exper

## 星数曲线

```mermaid
xychart-beta
    title "ai-dvps/comate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-25 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dac35912f6cb` · [字段定义](../../DATASET.md)*
