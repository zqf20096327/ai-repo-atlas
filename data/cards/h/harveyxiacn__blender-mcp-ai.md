# harveyxiacn/blender-mcp-ai

⭐ 18 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/harveyxiacn/blender-mcp-ai) · 个人维护 · 中文 README

**让 AI 客户端通过 MCP 协议用自然语言控制 Blender 的服务器**

开源 Model Context Protocol 服务器，由 FastMCP 服务器与 Blender 插件两部分组成：服务器把 Blender 操作暴露为 380 个 MCP 工具（56 个模块），插件通过本地 TCP socket 接收命令并调用 Blender Python API 执行。支持 Cursor、Windsurf、Claude Desktop 等任意 MCP 兼容客户端，兼容 Blender 4.x/5.x。默认 skill 配置仅加载 38 个工具，12 个技能组按需激活以精简 AI 上下文；提供视口/渲染截图供模型自审。需 Python 3.10+ 与 uv，从源码安装（未发布 PyPI）。

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

- 380 个 MCP 工具覆盖建模、材质、动画、渲染、绑定等 56 个模块
- 动态技能加载：默认 38 个工具，12 个技能组按需激活，另有 6 档配置（35-377 工具）
- 视口截图与渲染预览支持多模态 AI 审查循环
- 检查点系统、8 种渲染风格预设、67 种程序化材质、拓扑/UV/性能质量审计

## 适用场景

- 在 Cursor/Claude Desktop 等客户端里用自然语言驱动 Blender 建模、渲染与动画
- AI agent 端到端生成角色、场景并自审迭代
- 通过分层演示脚本验证安装与工具链完整性

## 场景标签

 · 领域:3D 创作/AI 工具接入

## 证据(README 行号)

> L39: **Blender MCP AI** is an open-source Model Context Protocol server that lets AI assistants control Blender through 
> L42: - **MCP Server** (`src/blender_mcp/`) — a FastMCP server exposing Blender operations as MCP tools
> L43: - **Blender Addon** (`addon/blender_mcp_addon/`) — a Blender plugin that receives commands over TCP and executes th

## 星数曲线

```mermaid
xychart-beta
    title "harveyxiacn/blender-mcp-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `87a59399be71` · [字段定义](../../DATASET.md)*
