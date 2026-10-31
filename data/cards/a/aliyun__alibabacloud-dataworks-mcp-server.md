# aliyun/alibabacloud-dataworks-mcp-server

⭐ 54 · TypeScript · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/aliyun/alibabacloud-dataworks-mcp-server) · [官网](https://www.aliyun.com/product/bigdata/ide) · 组织维护 · 中文 README

**让 AI agent 通过 MCP 操作阿里云 DataWorks 的服务器**

阿里云维护的 Model Context Protocol 服务器：将 DataWorks Open API 封装为标准化工具接口，供 Cursor、Cline 等 AI 客户端中的 agent 管理云上数据开发资源（项目、节点、元数据等）。基于 Node.js（v16+）实现，通过环境变量配置地域与 AccessKey，支持按工具类别/名称过滤。提供 npm 全局/本地安装与源码构建两种途径，Apache 2.0 许可。另有官方 DataWorks Agent 作为免配置的替代入口。

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

- 实现 MCP 规范，AI agent 通过标准化接口调用 DataWorks Open API
- 通过环境变量配置 Region/AccessKey，支持 TOOL_CATEGORIES 与 TOOL_NAMES 过滤
- 提供 npm 安装与源码构建（pnpm）两种方式

## 适用场景

- 在 Cursor/Cline 等 IDE 中用 AI 管理阿里云 DataWorks 资源
- 把 DataWorks 数据开发能力嵌入自有 AI 工作流
- 让 AI agent 以标准化协议执行云端数据开发运维操作

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L19: A Model Context Protocol (MCP) server that provides tools for AI, allowing it to interact with the DataWorks Open A
> L30: The server implements the Model Context Protocol specification to standardize cloud resource interactions for AI ag

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/alibabacloud-dataworks-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-31 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `14badebf9b2b` · [字段定义](../../DATASET.md)*
