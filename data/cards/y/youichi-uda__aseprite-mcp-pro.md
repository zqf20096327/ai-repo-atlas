# youichi-uda/aseprite-mcp-pro

⭐ 35 · Lua · MIT · 推送 2026-07-20 · [GitHub](https://github.com/youichi-uda/aseprite-mcp-pro) · [官网](https://aseprite-mcp.abyo.net/) · 个人维护

**通过 MCP 让 AI 助手直接操作 Aseprite 像素画编辑的扩展**

由 Lua 扩展与 Node.js MCP 服务器组成的桥接层，把 AI 客户端（如 Claude）连接到运行中的 Aseprite 编辑器，使其能以自然语言创建精灵、绘制像素、管理图层/帧/调色板、操作瓦片地图并导出 PNG、精灵表、GIF 等格式，含 8 个 Godot 集成工具（生成 SpriteFrames .tres、AtlasTexture、TileSet）。本仓库仅含免费扩展部分，MCP 服务器属完整付费版（标注 coming soon），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 96 个工具覆盖精灵、图层、帧、调色板、瓦片地图与导出等类别
- 8 个 Godot 集成工具：SpriteFrames .tres、AtlasTexture、TileSet 生成
- 通过 stdio / MCP 协议连接 AI 客户端与运行中的 Aseprite

## 适用场景

- 让 AI 助手用自然语言在 Aseprite 里画像素画、做动画
- 自动导出精灵表并生成 Godot 资源文件导入游戏项目
- 用 AI 批量操作调色板、切片与瓦片地图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: Aseprite MCP Pro connects AI assistants (Claude, etc.) directly to your running Aseprite editor. The AI can create s
> L33:     ↕ stdio / MCP Protocol

## 星数曲线

```mermaid
xychart-beta
    title "youichi-uda/aseprite-mcp-pro 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-25 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bb86238bb86b` · [字段定义](../../DATASET.md)*
