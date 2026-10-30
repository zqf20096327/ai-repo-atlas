# epicsagas/alcove

⭐ 17 · Rust · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/epicsagas/alcove) · [官网](https://epicsagas.github.io/alcove/) · 个人维护

**让 AI 编程代理按需检索私有项目文档的 MCP/HTTP 服务器**

用 Rust 编写的本地 HTTP API 服务器（端口 58301），向 Claude Code、Codex、Antigravity、Grok Build 等 AI 编程代理提供私有项目文档的按需检索：BM25 + 向量混合搜索、tree-sitter 代码索引（12 种语言）、CWD 自动检测项目切换、跨项目全局搜索，并通过 policy.toml 做文档结构校验、lint 与审计。文档存于本机独立目录，不进入公开仓库；不把文档注入上下文而是按查询返回排序结果。安装后需运行 alcove setup 完成配置，混合搜索需启用相应 feature 或使用预编译二进制。

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

- BM25 + 向量混合搜索与排序检索，按需返回而非全量注入上下文
- tree-sitter 代码索引，支持 12 种语言的模块/函数/类型结构
- policy.toml 策略校验、validate/lint/audit 文档健康检查
- 一套配置供多个 AI 代理共享，CWD 自动检测切换项目

## 适用场景

- 让 Claude Code / Codex 等代理在会话中按需检索我的架构与决策文档
- 多个项目共用一套私有文档层，避免文档散落或泄漏到公开仓库
- 检查项目文档是否缺失文件、含失效链接或过期标记

## 场景标签

`RAG` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L29: Alcove is an HTTP API server that gives AI coding agents on-demand access to your private project docs — **BM25 + v
> L264: ### Coding Agents (HTTP API)

## 星数曲线

```mermaid
xychart-beta
    title "epicsagas/alcove 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a0c25bcb070d` · [字段定义](../../DATASET.md)*
