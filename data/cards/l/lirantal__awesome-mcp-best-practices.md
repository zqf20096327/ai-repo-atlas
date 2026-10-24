# lirantal/awesome-mcp-best-practices

⭐ 84 · Apache-2.0 · 推送 2026-06-14 · [GitHub](https://github.com/lirantal/awesome-mcp-best-practices) · 个人维护

**MCP 服务器/客户端构建最佳实践策展清单**

由 Liran Tal 维护的 Model Context Protocol（MCP）最佳实践清单：围绕 MCP Server 与 MCP Client 的构建，给出工具命名规范与别名、工具描述标准、避免 not found 响应、服务器指令编写、能力抽象与避免 1:1 API 映射等条目，每个条目以反例/正例代码与理由说明；另含 Docker 容器化部署、依赖安全扫描等运维与安全建议。MCP Clients 部分与部分架构示例标注为 TBD，尚在编写中。面向构建 MCP 服务器/客户端的开发者阅读使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 工具命名规范（camelCase 推荐）与反例对照
- 工具描述标准与别名写法，含代码示例
- 架构建议：能力抽象、避免 1:1 API 映射
- Docker 容器化部署与依赖安全实践条目

## 适用场景

- 开发 MCP Server 时查阅工具命名与描述规范
- 设计 MCP 服务器架构时参考抽象与映射原则
- 部署与安全审计 MCP 服务器的实践参考

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: A curated and opinionated list of awesome Model Context Protocol (MCP) best practices as they pertain to building MC
> L34: ## 1 MCP Server Tools

## 星数曲线

```mermaid
xychart-beta
    title "lirantal/awesome-mcp-best-practices 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-24 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a9dc66d2969f` · [字段定义](../../DATASET.md)*
