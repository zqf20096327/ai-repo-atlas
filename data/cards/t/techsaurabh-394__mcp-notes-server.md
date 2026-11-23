# techsaurabh-394/mcp-notes-server

⭐ 3 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/techsaurabh-394/mcp-notes-server) · 个人维护

**给 Claude 等 AI 助手提供本地可搜索笔记记忆的 MCP 服务器**

TypeScript 编写的 Model Context Protocol 服务器，通过 stdio JSON-RPC 向 Claude Desktop、Claude Code 等 MCP 客户端暴露 8 个类型化工具（增删改查、关键词搜索、标签列表、Markdown 导出）及资源与提示。数据存于单个本地 JSON 文件，写入用锁文件+临时文件+原子重命名保证一致性，支持多客户端并发；输入用 zod 校验并带 MCP 工具注解。搜索为关键词加权打分，非语义检索；单文件上限 5,000 条笔记。需 Node.js 18+，无网络调用。

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

- 8 个 zod 类型化 MCP 工具，含 readOnlyHint/destructiveHint 注解
- 单 JSON 文件本地存储，锁文件+重命名的崩溃安全写入
- 关键词加权搜索（标题+3、标签+2、正文+1），非语义检索
- 可选 mcp-safe-actions 实现删除前人工审批与审计日志

## 适用场景

- 让 Claude 跨会话保存并检索个人笔记
- 用自然语言管理带标签的本地知识片段
- 导出 Markdown 格式的笔记合集做备份

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L13: `mcp-notes-server` is a Model Context Protocol (MCP) server written in TypeScript. Connect it to Claude Desktop, Cl
> L15: Architecture: Claude Desktop to MCP client to mcp-notes-server (7 tools) to notes.json

## 星数曲线

```mermaid
xychart-beta
    title "techsaurabh-394/mcp-notes-server 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-23 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `70c6032ab702` · [字段定义](../../DATASET.md)*
