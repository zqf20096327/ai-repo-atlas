# youichi-uda/blender-mcp-pro

⭐ 31 · Python · 推送 2026-04-15 · [GitHub](https://github.com/youichi-uda/blender-mcp-pro) · [官网](https://blender-mcp-pro.abyo.net) · 个人维护

**付费 MCP 服务器：让 Claude/Cursor 等 AI 助手控制 Blender**

面向 Blender 用户的 MCP 服务器 + Blender 插件组合：AI 助手（Claude Code/Claude Desktop/Cursor/Windsurf）通过 MCP 协议以自然语言控制 Blender，覆盖 17 类共 120+ 工具，包括场景管理、材质、着色器节点、灯光、22 种修改器、动画、几何节点、渲染、导入导出、绑定诊断与 Poly Haven/Sketchfab 资产集成等。采用延迟加载机制，初始仅注册 15 个核心工具。商业产品：itch.io 一次性 $15 或 Gumroad 订阅 $5/月，Blender 插件部分为 MIT 许可。支持 stdio 与 Streamable HTTP 两种传输方式。

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

- 17 类共 120+ 工具覆盖场景、材质、修改器、动画、几何节点等
- 支持 Claude Code/Claude Desktop/Cursor/Windsurf 等 MCP 客户端
- 延迟加载：初始 15 个核心工具，按类别按需启用（另有 eager 模式）
- Poly Haven 与 Sketchfab 资产集成、FBX/OBJ/GLTF/USD 等格式导入导出

## 适用场景

- 用自然语言在 Blender 中建模、打光和渲染
- 让 AI 助手批量处理场景、绑定诊断或导出模型
- 通过远程 MCP 连接从 Web 客户端控制 Blender

## 场景标签

 · 领域:3D 创作/AI 工具集成

## 证据(README 行号)

> L3: Control Blender entirely from AI assistants (Claude Code, Claude Desktop, Cursor, Windsurf) via MCP.
> L5: **120+ tools across 17 categories** — Scene management, materials, shader nodes, lights, modifiers, animation, geome
> L47: #### Claude Code (`~/.claude.json`)

## 星数曲线

```mermaid
xychart-beta
    title "youichi-uda/blender-mcp-pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `579758f54257` · [字段定义](../../DATASET.md)*
