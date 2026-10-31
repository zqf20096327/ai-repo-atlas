# chuongmep/mcp-revit-sample-au2025

⭐ 14 · Python · MIT · 推送 2026-02-12 · [GitHub](https://github.com/chuongmep/mcp-revit-sample-au2025) · 个人维护

**让 MCP 客户端查询 Revit 模型获取 BIM 洞察的示例服务器**

面向 AU 2025 演示的轻量 MCP（Model Context Protocol）示例：作为 MCP 服务器向 AI 客户端（如 Claude Desktop、VS Code 中的 GitHub Copilot Chat）提供 Revit 模型查询能力，包括元素计数、类别分布、族与类型清单、房间合规启发式检查（面积/高度/荷载字段）与命名规范审查。基于 Python MCP SDK（1.2.0+）构建，附带 models/ 下示例模型数据，代码结构设计为可扩展新查询。安装通过 git clone 源码、uv 建虚拟环境并配置 Claude/VS Code 的 MCP 客户端连接。

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

- MCP 服务器向 AI 客户端提供 Revit 模型结构化查询
- 元素/类别/族与类型的统计查询
- 房间合规启发式检查与命名规范审查
- 支持 Claude Desktop 与 VS Code（MCP: Start Server）两种客户端配置

## 适用场景

- 在 Claude Desktop 或 Copilot Chat 中用自然语言查询 Revit 模型数据
- 演示和学习 MCP 模式与 AEC 数据结合的集成方式
- 教学场景中快速展示 BIM 元素洞察与房间合规检查

## 场景标签

`数据分析` `教程课程` · 领域:效率与自动化

## 证据(README 行号)

> L3: A lightweight Model Context Protocol (MCP) sample that lets AI clients query a Revit model for BIM insights like ele
> L9: - MCP-native: works with MCP-enabled clients (e.g., Claude Desktop)

## 星数曲线

```mermaid
xychart-beta
    title "chuongmep/mcp-revit-sample-au2025 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `057070ca43d8` · [字段定义](../../DATASET.md)*
