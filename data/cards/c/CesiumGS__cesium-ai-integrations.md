# CesiumGS/cesium-ai-integrations

⭐ 93 · TypeScript · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/CesiumGS/cesium-ai-integrations) · 组织维护

**连接 CesiumJS 与 AI 系统的参考集成与实验合集（已弃用）**

CesiumGS 维护的参考集成集合：提供 MCP 服务器、agent skills、检索管道等模式，把 Cesium 3D 地理空间能力接入 LLM 与 agent 工作流，帮助开发者构建能理解 3D 数据与地理空间上下文的应用。仓库本身未给出统一安装命令，各集成有各自的 README。仓库已标记弃用，活跃开发迁移至 cesiumjs-ai-starter-app 与 cesiumjs-skills；本仓库保留作参考但不再更新。原架构通过本地 WebSocket MCP 服务器桥接浏览器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供连接 Cesium 应用与 AI 助手的 MCP 服务器与 agent skills 参考模式
- 示例工作流覆盖数据摄取、检索与 3D 地理空间内容分析
- 收录社区 MCP 服务器与 MCP App 示例

## 适用场景

- 参考已有模式把 CesiumJS 3D 地图接入 AI 助手或 agent
- 为 AI 编码助手添加 CesiumJS 相关 agent skills
- 了解地理空间 AI 集成的社区实践

## 场景标签

 · 领域:地理空间/AI 集成

## 证据(README 行号)

> L31: Cesium AI Integrations is a collection of reference integrations, experiments, and patterns that connect the Cesium
> L49: - **mcp/** - Model Context Protocol servers and applications that integrate Cesium with AI assistants
> L50: - **skills/** - Agent skills for automatic activation of Cesium-related capabilities in AI assistants

## 星数曲线

```mermaid
xychart-beta
    title "CesiumGS/cesium-ai-integrations 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-26 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d20ae8ed6bc8` · [字段定义](../../DATASET.md)*
