# nextpress-ai/nextpress

⭐ 13 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/nextpress-ai/nextpress) · [官网](https://nextpress.ai) · 组织维护

**自托管的 WordPress 兼容 CMS，以 JavaScript/TypeScript 实现**

用 JavaScript/TypeScript 构建的 WordPress 兼容内容管理系统，可自托管于任何支持 Docker 的环境。提供 39 种区块的可视化页面构建器、多站点管理、WordPress 内容导入、WordPress 兼容 REST API、模板系统与 SEO 工具。以 monorepo 形式发布 npm 包：TypeScript SDK 与供 Cursor/Claude 等 agent 编辑内容的 MCP server，开发重点包含基于 SDK 与 MCP 的 AI 辅助编辑。开发环境用 PGlite 嵌入式 PostgreSQL，生产环境支持完整 PostgreSQL，一键脚本安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 39 种区块的可视化页面构建器（拖拽编辑、多设备预览、自动保存）
- WordPress 兼容 REST API 与 WordPress 内容导入
- @nextpress-org/sdk 与 @nextpress-org/mcp（供 Cursor/Claude 等 agent 编辑内容）
- 单次安装运行多站点，自动配置各站点域名与 HTTPS

## 适用场景

- 自托管一个 WordPress 兼容的网站并用可视化编辑器建页
- 从现有 WordPress 站点迁移文章与页面
- 让 AI agent（Cursor/Claude）通过 MCP 直接编辑站点内容
- 通过 REST API/SDK 做无头 CMS 使用

## 场景标签

 · 领域:内容管理/CMS

## 证据(README 行号)

> L3: A self-hostable WordPress-compatible CMS built in JavaScript/TypeScript.
> L12: |**MCP**|`@nextpress-org/mcp`|MCP server for Cursor and Claude — agents edit content through the SDK|`packages/mcp/
> L255: |**AI-powered features**|Assisted editing and automation on SDK and MCP|

## 星数曲线

```mermaid
xychart-beta
    title "nextpress-ai/nextpress 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0bf7ce91ff02` · [字段定义](../../DATASET.md)*
