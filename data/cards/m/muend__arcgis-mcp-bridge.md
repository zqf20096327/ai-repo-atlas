# muend/arcgis-mcp-bridge

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/muend/arcgis-mcp-bridge) · [官网](https://pypi.org/project/arcgis-mcp-bridge/) · 个人维护

**面向 Claude Desktop 等 MCP 主机的 ArcGIS Pro ArcPy 桥接服务器**

本地优先的异步 MCP 服务器，通过 stdio JSON-RPC 将 ArcGIS Pro 的 ArcPy 引擎以 100 个声明式地理处理工具（10 个门类）暴露给 Claude Desktop、Cursor 等 MCP 主机。采用双进程隔离架构：Layer A 为 FastMCP 协议宿主，Layer B 为 ArcPy 工作进程；包含 PathGuard 沙箱路径校验、10 个破坏性工具的 confirm 确认门与结构化错误分类。运行要求 Windows、已授权的 ArcGIS Pro 安装与 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100 个声明式地理处理工具，覆盖 10 个门类（数据管理、几何分析、栅格运算、网络分析等）
- 双进程隔离：FastMCP 协议层与 ArcPy 工作进程分离，原生崩溃不终止服务器
- PathGuard 沙箱在两层进程内校验读写路径，破坏性工具需显式 confirm: true
- 86 个单元测试在无 ArcGIS 安装环境下运行（arcpy 以 MagicMock 注入）

## 适用场景

- 通过自然语言让 Claude 操作 ArcGIS Pro 执行缓冲、 dissolve、栅格分析等地理处理
- 将手绘地块边界照片配准并提交到地理数据库（extract_sketch_to_gis）
- 在 MCP 主机中列出图层、导出 PDF/PNG 地图版面

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L50: A secure, local-first, asynchronous MCP server exposing ArcGIS Pro's ArcPy
> L51: engine to Claude Desktop and other MCP hosts over stdio JSON-RPC.
> L103:     A[Claude Desktop / Cursor] -->|JSON-RPC over stdio| B[Layer A · MCP Protocol Host]

## 星数曲线

```mermaid
xychart-beta
    title "muend/arcgis-mcp-bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-27 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9d1c5cf082fe` · [字段定义](../../DATASET.md)*
