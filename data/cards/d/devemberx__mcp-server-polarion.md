# devemberx/mcp-server-polarion

⭐ 17 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/devemberx/mcp-server-polarion) · 个人维护

**连接 Polarion ALM 的 MCP 服务器：AI 助手读写其文档与工作项**

面向 Polarion ALM 的 Model Context Protocol 服务器，供 Claude Code、Claude Desktop、VS Code (Copilot)、Cursor 等 MCP 兼容客户端接入。提供 46 个工具，覆盖文档、工作项、测试运行、追溯链接、评论与附件的读取和写入：文档可渲染为 Markdown、支持 Lucene/SQL 查询、分页遍历。写入均支持 dry_run，提交前校验字段与枚举值，请求按可配置速率上限发送并在 429/5xx 时自动重试。要求 Polarion 2506+ 与 Python 3.13+，通过 uvx 运行，用 Personal Access Token 认证。

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

- 46 个工具覆盖文档/工作项/测试运行/链接/评论/附件的读写
- 所有写入支持 dry_run，提交前校验字段、枚举值与链接目标
- 请求序列化并按可配置速率上限发送，429/5xx 自动重试
- 支持 Claude Code / Claude Desktop / VS Code (Copilot) / Cursor 客户端配置

## 适用场景

- 让 AI 助手在 Polarion 中创建和更新需求、任务与测试运行
- 让 AI 检索并总结需求文档和追溯链接
- 通过对话批量记录测试执行结果与管理评论

## 场景标签

 · 领域:开发工具/ALM 集成

## 证据(README 行号)

> L15: A Model Context Protocol (MCP) server for **Polarion ALM**, built for real-world instances: every write supports `d
> L21: - **46 tools** covering read and write across documents, work items, test runs, traceability links, comments, and a

## 星数曲线

```mermaid
xychart-beta
    title "devemberx/mcp-server-polarion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `43b186fdc607` · [字段定义](../../DATASET.md)*
