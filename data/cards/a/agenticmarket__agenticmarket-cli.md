# agenticmarket/agenticmarket-cli

⭐ 10 · JavaScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/agenticmarket/agenticmarket-cli) · [官网](https://agenticmarket.dev) · 组织维护

**MCP 服务器 CLI：一键创建/安装到各 IDE 并变现**

面向 MCP（Model Context Protocol）生态的命令行工具，三个核心动作：create 一键脚手架生成基于 Hono + TypeScript 的 MCP 服务器项目（内置安全中间件、限流、部署配置，支持从零开始或将现有 REST API 封装为 MCP）；install 自动检测本机已装的 IDE（VS Code、Cursor、Claude Desktop 等 9 种）并写入对应 MCP 配置文件，免去手动编辑 JSON；另有 skill 子命令分发 SKILL.md 技能包。平台侧承担分发、鉴权、计费与分成（创作者获 80% 每次调用收入），采用预付点数计费，仅在调用成功时扣费。

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

- create 命令 ~30 秒脚手架 Hono+TypeScript MCP 服务器，含 9 项默认安全层
- install 自动检测本机 IDE 并写入 MCP 配置，免手动 JSON 编辑
- 支持 API wrapper 模式将现有 REST API 转为 MCP 服务器
- 创作者发布服务器后按调用获得 80% 收入分成，支持 Wise/Razorpay 提现

## 适用场景

- 一条命令把 MCP 服务器装进多个 IDE，不手动改 JSON
- 把已有 REST API 快速封装成 MCP 服务器并发布
- 发布自建的 MCP 服务器获取调用分成收入
- 给多个 agent 批量安装 SKILL.md 技能包

## 场景标签

 · 领域:AI 开发者工具/MCP 基础设施

## 证据(README 行号)

> L3: > The CLI for Model Context Protocol servers. Create production-ready MCP servers from scratch, or install existing 
> L56: The Model Context Protocol (MCP) is the open standard that lets AI assistants — in VS Code, Cursor, Claude Desktop,
> L44: `install` writes MCP entries into VS Code, Cursor, Claude Desktop, and every other IDE you have — automatically.

## 星数曲线

```mermaid
xychart-beta
    title "agenticmarket/agenticmarket-cli 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `318c3a3ee7db` · [字段定义](../../DATASET.md)*
