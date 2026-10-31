# zaizaizhao/mcp-server-chart-minio

⭐ 52 · TypeScript · MIT · 推送 2026-03-07 · [GitHub](https://github.com/zaizaizhao/mcp-server-chart-minio) · 个人维护 · 中文 README

**给开发者的图表生成服务：MCP 私有化部署，22+ 图表服务端渲染**

mcp-server-chart 的私有化部署方案：基于 NestJS 的图表生成服务，通过 RESTful API 接收数据，基于 @antv/gpt-vis-ssr 在服务器端渲染 22+ 种图表（折线、饼图、桑基图、思维导图等），生成结果存入 MinIO 对象存储并自动返回访问 URL。提供 Docker Compose 一键部署（含 MinIO）与本地开发两种模式，附带 OpenAPI 文档、生产部署检查清单、诊断脚本与常见问题排查。本地开发需安装 Cairo/Pango 等系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 22+ 种图表类型的服务端渲染（基于 @antv/gpt-vis-ssr）
- MinIO 对象存储集成，自动生成图表访问 URL
- Docker Compose 一键部署完整服务（应用 + MinIO）
- 提供生产环境部署检查清单与诊断脚本

## 适用场景

- 私有化部署图表生成服务供 LLM/MCP 客户端调用
- 通过 RESTful API 批量生成图表并获取可访问 URL
- 在内网/虚拟机环境搭建带对象存储的图表服务

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: 基于 NestJS 的图表生成服务，集成 MinIO 对象存储，支持 22+ 种图表类型的服务器端渲染。
> L8: - 🚀 **服务器端渲染**：基于 @antv/gpt-vis-ssr 的高性能图表生成
> L148: curl -X POST http://localhost:3000/api/chart-generators/line \

## 星数曲线

```mermaid
xychart-beta
    title "zaizaizhao/mcp-server-chart-minio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6b29f396d505` · [字段定义](../../DATASET.md)*
