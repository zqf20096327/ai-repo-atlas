# S2thend/cursor-history-mcp

⭐ 33 · TypeScript · MIT · 推送 2026-09-08 · [GitHub](https://github.com/S2thend/cursor-history-mcp) · [官网](https://www.npmjs.com/package/cursor-history-mcp) · 个人维护 · 中文 README

**让 AI 助手通过 MCP 搜索、浏览和导出 Cursor 聊天历史**

一个 stdio MCP 服务器，将 Claude、Cursor 等 MCP 客户端连接到本地 Cursor 历史读取器 cursor-history：支持跨工作区搜索对话文本、按会话检查内容、导出 Markdown/JSON，并提供 Composer 会话的备份、恢复与迁移工具。无需嵌入、索引服务或 API key。MCP 独有的 Year in Review 功能基于历史生成年度统计与报告提示词。迁移默认为 move 模式会删除原会话，写操作前建议备份并关闭 Cursor。

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

- 8 个 MCP 工具：列表/检查/搜索/导出/备份/恢复/迁移/年度回顾
- 兼容 4 代 Cursor 存储格式（Legacy/Composer、Agent transcripts、Store、ACP）
- Year in Review 生成年度统计、主题与报告提示词（中英模板）
- 无需嵌入、索引服务或 API key，直接读取本地文件

## 适用场景

- 让 AI 助手检索过去会话中的决策与修复记录
- 导出或备份 Cursor 会话历史
- 生成年度编码活动统计与主题回顾

## 场景标签

 · 领域:开发工具/AI 客户端基础设施

## 证据(README 行号)

> L16: `cursor-history-mcp` connects Claude, Cursor, and other MCP clients to the local history reader in cursor-history. 
> L90: The MCP server delegates discovery and parsing to `cursor-history`; it does not maintain a separate conversation da

## 星数曲线

```mermaid
xychart-beta
    title "S2thend/cursor-history-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `447b2d31c2db` · [字段定义](../../DATASET.md)*
