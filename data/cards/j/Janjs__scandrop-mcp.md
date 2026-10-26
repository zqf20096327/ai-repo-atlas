# Janjs/scandrop-mcp

⭐ 41 · TypeScript · 推送 2026-09-07 · [GitHub](https://github.com/Janjs/scandrop-mcp) · [官网](https://scandrop.janjs.dev/) · 个人维护

**让 LLM 理解 3D 空间的 MCP 服务器：解析户型扫描并提供空间工具**

MCP 服务器，读取 GLB/GLTF 户型扫描文件（如 Polycam 导出），推导出紧凑的场景图：主地板平面、XZ 地板多边形、障碍物足迹与 OBB 及启发式语义标签，并以版本化方式持久化到本地磁盘。通过确定性 MCP 工具（check_fit、find_free_spaces 等）供 Claude 等模型调用，使模型无需自行做几何计算即可回答家具摆放等空间问题。面向配置 MCP 客户端的开发者/用户，附 FastAPI 调试端点与 Web 工作台（含托管演示）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 GLB/GLTF 扫描并推导地板平面、障碍物足迹、OBB 与语义标签
- 确定性 MCP 工具：check_fit 摆放检测、find_free_spaces 空位查找
- 场景产物版本化持久化于本地磁盘
- 附带 Web 工作台（模型查看器、空间表示查看器、MCP 聊天面板）

## 适用场景

- 导入手机扫描的房间模型，问 AI 家具能摆在哪里
- 让 Claude Desktop 读取本地 GLB 并执行空间推理
- 通过 FastAPI 端点调试场景导入与查询

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: Minimal but real MCP server that ingests a GLB/GLTF floorplan scan (for example captured with Polycam https://poly.c
> L42: - Exposes deterministic MCP tools (`check_fit`, `find_free_spaces`) so the model never does geometry math.

## 星数曲线

```mermaid
xychart-beta
    title "Janjs/scandrop-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `afa1bc4121a2` · [字段定义](../../DATASET.md)*
