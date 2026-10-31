# fruggr/zendesk-mcp-server

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/fruggr/zendesk-mcp-server) · [官网](https://www.fruggr.io) · 组织维护

**把 Zendesk 接入 AI 助手的 MCP 服务器：工单与帮助中心全流程**

基于 Model Context Protocol 的 Zendesk 连接器：AI 助手可用自然语言检索帮助中心文章、起草/更新/翻译文章（按 h1/h2/h3 分节编辑）、管理 Support 工单（评论、分诊、附件），并支持面向终端客户的 End-user 模式（提交与跟进请求）。认证仅支持 OAuth 2.1 PKCE 按用户授权，明确不支持静态 API token；工具可按 all/namespace/single 三种模式注册并支持只读过滤。以 npm 包运行（需 Node.js>=22），也可部署为远程 HTTP MCP 服务器（含 distroless 容器镜像，标注实验性）。限制：不覆盖 Talk/Explore/Sell 等 Zendesk 产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OAuth 2.1 PKCE 按用户授权，不支持静态 API token
- 按标题分节编辑大型帮助中心文章以减少 token 往返
- 附件图片以原生 MCP 图像内容返回，服务端无视觉模型依赖
- 工具面支持 all/namespace/single 三种注册模式与只读过滤

## 适用场景

- 客服/支持团队在 Claude、Cursor 等 MCP 客户端中直接处理 Zendesk 工单
- 用对话起草和维护帮助中心知识库文章
- 厂商向客户提供 End-user 模式，让客户在助手内提交并跟进支持请求

## 场景标签

`AI 助手` `AI 写作` · 领域:对话与助手

## 证据(README 行号)

> L10: A Model Context Protocol (MCP) server that
> L87: - A lean stack: the official MCP TypeScript SDK (`@modelcontextprotocol/server`) plus `zod`, speaking to

## 星数曲线

```mermaid
xychart-beta
    title "fruggr/zendesk-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b28ae288cb14` · [字段定义](../../DATASET.md)*
