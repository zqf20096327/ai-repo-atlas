# ysunyang4/Nexus

⭐ 374 · TypeScript · AGPL-3.0 · 推送 2026-11-15 · [GitHub](https://github.com/ysunyang4/Nexus) · [官网](https://blog.ycu.de5.net/) · 个人维护 · 中文 README

**本地 AI 控制中枢：让网页版 AI 经 MCP 隧道操作本地工作站**

面向 ChatGPT、DeepSeek 等 Web AI 助手的本地控制平面：通过 Streamable HTTP + Bearer 令牌的安全 MCP 隧道，把远端大模型连接到本地工作站，供 AI 智能体在沙箱边界内执行文件操作、Git、命令执行、Windows 桌面控制等 24 个维度的 332 项规范 MCP 工具。关键机制包括 WAL 预写式操作账本与崩溃恢复、AST 命令风险三级分级、多层路径沙箱与双令牌隔离、SQLite 本地记忆知识库。桌面端基于 Tauri 2 + React，提供 Windows/macOS/Linux 安装包与油猴脚本，也可从源码构建（需 Node.js 24+/pnpm 10+/Rust）。许可为 AGPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 332 项规范 MCP 工具，覆盖文件/Git/命令执行/桌面控制等 24 个维度
- WAL 预写式操作账本、崩溃恢复与幂等性防护
- AST 命令风险引擎（SAFE/CAUTION/DANGEROUS）默认拦截破坏性命令
- 多层路径沙箱、双令牌密码学隔离与敏感凭证屏蔽

## 适用场景

- 让 ChatGPT/DeepSeek 等网页 AI 直接读写本地项目文件并执行构建调试
- 通过 Cursor/Windsurf 等 MCP 客户端以受控方式操作本地工作站
- 在沙箱与命令风控约束下让 AI 智能体编排本地研发工作流

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L20: **Nexus** is an enterprise-grade Local AI Control Plane designed specifically for ChatGPT, DeepSeek, and modern AI 
> L33: #### 1. 332 Canonical MCP Tools
> L109: **Standard MCP Client Configuration (`mcp_config.json` / Client Settings)**:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `9af2f0ae1fac` · [字段定义](../../DATASET.md)*
