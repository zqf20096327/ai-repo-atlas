# Dishant27/linkedin-mcp-server

⭐ 54 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Dishant27/linkedin-mcp-server) · 个人维护

**连接 LinkedIn API 与 LLM 的 MCP 服务器**

用 TypeScript 实现的 Model Context Protocol (MCP) 服务器，把 LinkedIn 官方 HTTP API（OAuth 2.0 认证）封装为 MCP 工具，供 Claude Desktop 等 MCP 兼容 LLM 调用，功能覆盖人员搜索、档案获取、职位信息与消息。README 明确说明 LinkedIn API 限制：client_credentials 两腿 OAuth 对多数开发者应用不可用，search-people 调用的端点非公开文档化接口，需合作方权限。通过 git clone 源码加 npm 安装运行。

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

- 将 LinkedIn API 封装为 MCP 工具（搜索/档案/职位/消息）
- OAuth 2.0 认证流程，凭据经 POST body 传递
- 提供 Claude Desktop 的 mcpServers 配置示例
- README 详细标注 LinkedIn API 访问限制与合作伙伴权限要求

## 适用场景

- 在 Claude 等 MCP 客户端中直接调用 LinkedIn 数据能力
- 招聘场景下检索候选人与获取档案信息
- 销售与商务拓展中查找目标公司决策人

## 场景标签

 · 领域:LLM 工具接入/社交数据集成

## 证据(README 行号)

> L1: # LinkedIn Logo LinkedInMCP: Revolutionizing LinkedIn API Interactions
> L51: #### `claude_desktop_config.json` (for Claude Desktop)
> L104: - **Standardized Protocol**: Follows Model Context Protocol specifications

## 星数曲线

```mermaid
xychart-beta
    title "Dishant27/linkedin-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-30 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3d33093469b4` · [字段定义](../../DATASET.md)*
