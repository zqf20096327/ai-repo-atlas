# a-tokyo/aiworkspace

⭐ 21 · JavaScript · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/a-tokyo/aiworkspace) · 个人维护

**跨多仓库工作区统一管理 AI 编程工具技能与配置**

以单一 workspace 仓库作为规范来源，通过 npm install 将配置镜像到父级根目录、为各 AI 编程工具（Cursor、Claude Code、Codex、Copilot 等 40+ 工具）symlink 技能与 MCP 服务器，并安装 git hooks 保持同步。提供 skills:add/remove 按注册表安装技能并用 skills-lock.json 锁定，MCP 服务器一次定义多处生成，遵循 nearest-wins 知识层级。要求 Node.js >= 18 与 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npm install 自动镜像配置、symlink 技能与 MCP 服务器并安装 git hooks
- skills-lock.json 锁定技能来源与哈希，重装自动恢复
- MCP 服务器一处定义，为 Claude Code/Cursor/VS Code/Codex 生成对应配置文件
- nearest-wins 知识层级：越靠近代码的配置优先级越高

## 适用场景

- 团队统一各项目与成员的 AI 工具配置，避免漂移
- 为多仓库 monorepo 场景共享技能、规则与 MCP 服务器
- 按注册表安装并锁定 agent 技能版本

## 场景标签

 · 领域:开发者工具/AI 工程化

## 证据(README 行号)

> L3: Manage shared AI agent skills, configs, and automation across multi-repo workspaces. Works with Cursor, Claude Code,
> L13: **The solution**: A single `workspace/` repo that acts as the canonical source. Running `npm install` mirrors confi

## 星数曲线

```mermaid
xychart-beta
    title "a-tokyo/aiworkspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7a55b8db7169` · [字段定义](../../DATASET.md)*
