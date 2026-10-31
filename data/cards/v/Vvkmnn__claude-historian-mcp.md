# Vvkmnn/claude-historian-mcp

⭐ 179 · TypeScript · MIT · 推送 2026-06-15 · [GitHub](https://github.com/Vvkmnn/claude-historian-mcp) · [官网](https://www.npmjs.com/package/claude-historian-mcp) · 个人维护

**搜索 Claude Code 对话历史的 MCP 服务器，本地零依赖**

面向 Claude Code 用户的 MCP 服务器，提供 search 与 inspect 两个工具、11 种检索范围，可跨会话查找过往解决方案、文件改动、错误模式、工具使用序列与相似查询。实现上采用 JSONL 流式解析、LRU 缓存、TF-IDF 式评分、朴素贝叶斯式查询分类与编辑距离模糊匹配，仅依赖 @modelcontextprotocol/sdk，零外部数据库，数据不离开本机。限制：不支持 Claude Desktop（其对话存储在服务端）。通过 npx、MCP 配置、skill 或插件市场安装，另可选装 hooks 插件实现自动触发检索。

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

- search/inspect 两个 MCP 工具，覆盖 11 种检索范围
- 零外部依赖，仅读取本地 ~/.claude/ 下的 JSONL 文件
- JSONL 流式解析、LRU 缓存、TF-IDF 式评分、模糊匹配与时间衰减等 12 种检索算法
- 可选 plugin 提供 WebSearch/报错等 hook 的自动历史检索

## 适用场景

- 在 Claude Code 中查找过去解决过的同类问题与错误修复
- 回顾某次会话涉及的文件改动和工具使用模式
- 让 Claude 在搜索网页前先检索本地对话历史以复用经验

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: An Model Context Protocol (MCP) server for searching your Claude Code conversation history. Find past solutions, tra
> L85: MCP server that gives Claude access to your conversation history. Two tools, 11 scopes, zero dependencies.

## 星数曲线

```mermaid
xychart-beta
    title "Vvkmnn/claude-historian-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 178 --> 180
    line [179, 179]
```

2026-10-18 179 → 2026-10-31 179（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b242854817b7` · [字段定义](../../DATASET.md)*
