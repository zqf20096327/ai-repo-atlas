# maxLWS/agy-memory

⭐ 4 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/maxLWS/agy-memory) · 个人维护 · 中文 README

**Antigravity 的本地零依赖跨会话记忆 MCP 插件**

为 Google Antigravity（CLI/Desktop/IDE）提供的本地 MCP 插件：让任意会话搜索并检视本机历史对话转录、Markdown 工件，并可读取 ~/.codex 与 ~/.claude 会话；提供文件编辑历史与命令错误历史查询、以纯 Markdown 文件存储的长期笔记（带 CAS 检查）。零依赖、零网络调用，工具响应控制在 8,650 字节内以避免落盘溢出，安装后在 SessionStart 注入只读快照。需 Node.js >= 20。

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

- 跨会话检索 Antigravity 转录及 Codex / Claude Code 本地会话
- 文件编辑历史与错误历史（退出码、重跑匹配）查询模式
- Markdown 笔记存储带 expectedRevision 比较并交换检查
- 提供 --cli 模式供 Swarm worker 与 shell 脚本直接调用

## 适用场景

- 让 coding agent 检索此前会话处理过的文件与结论
- 查询某个文件历史上被哪些会话编辑过
- 排查过去会话中命令失败的原因与重跑记录

## 场景标签

`多智能体` `编码 Agent` `知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: **agy-memory** is a local, zero-dependency MCP plugin for Google Antigravity (`agy` CLI, Desktop, and IDE). It lets
> L46: Or paste into any Antigravity session:
> L32: Requires **Node.js >= 20** (no `npm install` needed; pre-built ESM bundles live in `dist/`).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `8ff1ccb6ca7c` · [字段定义](../../DATASET.md)*
