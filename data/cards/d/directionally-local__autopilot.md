# directionally-local/autopilot

⭐ 222 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/directionally-local/autopilot) · [官网](https://directionallylocal.com/autopilot) · 组织维护

**开源终端编码 Agent 与 SDK：自带密钥接 25+ 模型提供商**

运行在终端里的开源编码 Agent，同时提供 headless SDK（createAgentSession API 与 JSONL-over-stdio RPC）。通过 dl 安装器或 npm/Homebrew/npx 获取；首次运行选择免费额度（GitHub 登录）、自有 API 密钥或本地 GPU 模型。机制包括 plan/edit/auto 三种权限模式、破坏性操作守卫与 /undo 恢复点、沙箱化 subagent 委派、SQLite+嵌入的跨会话记忆、LSP 与 MCP 扩展、消息队列与长时无人值守运行（检查点恢复、预算控制）。Windows 支持 OS 感知 shell。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BYOK 接入 OpenRouter 等 25+ 提供商，或由 dl 在本地 GPU 上配置 vLLM 模型
- plan/edit/auto 权限模式与凭据文件、内网地址的读写防护，/undo 恢复点与 /audit 报告
- 协调者可将任务委派给经过权限检查的 subagent
- LSP + MCP、SQLite+嵌入跨会话记忆、headless SDK 与无人值守长时运行

## 适用场景

- 在终端里让 Agent 读取、编辑代码并执行带守卫的 git 操作
- 用自有 API 密钥或本地 GPU 私有运行编码 Agent
- 通过 SDK 以编程方式构建基于 Agent 的自动化流程
- 从 Claude Code/Cursor 等迁移现有配置与 MCP 服务器

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14:  The open-source coding agent inside dl. It doesn't ask permission.
> L31: On the free tier, model calls go through Directionally Local's free tier service to its model host; it keeps usage 

## 星数曲线

```mermaid
xychart-beta
    title "directionally-local/autopilot 星数(近 12 点)"
    x-axis ["2026-10-29", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-28"]
    y-axis "stars" 173 --> 226
    line [177, 194, 216, 217, 218, 220, 221, 220, 221, 220, 222, 222]
```

2026-10-29 177 → 2026-11-28 222（+45）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c01470189087` · [字段定义](../../DATASET.md)*
