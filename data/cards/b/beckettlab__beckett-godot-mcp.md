# beckettlab/beckett-godot-mcp

⭐ 48 · GDScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/beckettlab/beckett-godot-mcp) · [官网](https://beckettlabs.itch.io/beckett-godot-mcp) · 个人维护

**嵌入 Godot 编辑器的零 sidecar MCP 服务器，供 AI agent 开发游戏**

以 Godot 4 EditorPlugin（GDScript）形式实现的 MCP 服务器：AI 客户端（Claude Code、Cursor 等）通过编辑器内置的 TCPServer HTTP/JSON-RPC 接口驱动 Godot，无 Node/Python sidecar。免费 Lite 版（MIT）提供 56 个工具，覆盖检查、创作、运行与观察运行中游戏（截图、远程场景树、性能监视、日志），支持 GDScript 与 C#，写入前先做编译校验；付费 Full 版（$15 买断）增加输入驱动、断言与自动化测试。安装方式为 Godot 资产库安装插件或手动复制 addons 目录，要求 Godot 4.2+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 56 个反射通用工具经 ClassDB 覆盖引擎全部类，无需按领域手写封装
- validate-before-write：拒绝写入无法编译的 GDScript
- 免费版即可观察运行中游戏：截图、远程场景树、节点状态、性能监视、日志
- 场景/节点变更经 EditorUndoRedoManager 可撤销，localhost-only 带 Host/Origin 校验与项目级 token

## 适用场景

- 让 Claude Code / Cursor 等 agent 在 Godot 编辑器中直接创建场景与编写脚本
- AI 运行游戏并读取截图、场景树与日志以诊断问题
- 用 C#/.NET 进行 Godot 开发并获取结构化编译诊断

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14: **Beckett** is a **zero-sidecar** Model Context Protocol (MCP) server embedded directly in the **Godot 4** editor a
> L31: - **The AI sees your game (free)** — `screenshot` the running game, read the live remote scene tree (`get_remote_tr
> L45: > **Fewer tools, on purpose — that's the moat, not a limitation.** Most Godot MCPs hand-code one tool per task (`cr

## 星数曲线

```mermaid
xychart-beta
    title "beckettlab/beckett-godot-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-29"]
    y-axis "stars" 45 --> 49
    line [46, 47, 48, 48]
```

2026-10-18 46 → 2026-10-29 48（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1a0c24256fac` · [字段定义](../../DATASET.md)*
