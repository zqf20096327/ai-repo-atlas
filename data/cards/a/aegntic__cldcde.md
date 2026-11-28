# aegntic/cldcde

⭐ 12 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/aegntic/cldcde) · [官网](https://cldcde.cc) · 组织维护

**为 Claude Code 开发者提供插件生态中心与 CLI 工具包**

围绕 Claude Code 的社区生态项目，包含三部分：40+ 个 shell 快捷方式（启动、续接会话、模型切换等）、实时上下文窗口 token 监控（通过 Claude hooks 集成、彩色进度条显示占用）、以及 Cloudflare Workers 上的社区平台（扩展/MCP 服务器浏览、新闻聚合、文档中心、用户主页）。另含沙箱云端代理包，支持 Docker/E2B 等隔离执行与多代理并行。需 Node.js 18+ 或 Bun。

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

- 40+ CLI 快捷方式，支持 Bash/Zsh 自动配置
- 实时 token 监控，经 Claude hooks 持久集成
- 云端代理沙箱执行（Docker/E2B/VM），最多 8 个代理并行
- cldcde.cc 社区平台：扩展与 MCP 服务器浏览与搜索

## 适用场景

- 用快捷方式管理 Claude Code 会话与模型切换
- 实时查看上下文窗口占用避免溢出
- 发现和安装社区 Claude Code 扩展与 MCP 服务器
- 在隔离沙箱中并行运行多个编码代理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L1: cldcde — The unofficial community hub for Claude Code plugins, skills, extensions, MCP servers, and some really expe
> L5: The complete productivity suite for Claude Code developers. **40+ CLI shortcuts**, **real-time context monitoring**,
> L88: - **Extension & MCP Browser**: Search, discover, and install tools


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `64afa3958808` · [字段定义](../../DATASET.md)*
