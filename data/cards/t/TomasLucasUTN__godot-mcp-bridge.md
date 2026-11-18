# TomasLucasUTN/godot-mcp-bridge

⭐ 11 · GDScript · MIT · 推送 2026-11-01 · [GitHub](https://github.com/TomasLucasUTN/godot-mcp-bridge) · [官网](https://github.com/TomasLucasUTN/godot-mcp-bridge) · 个人维护

**让 Claude/Cursor 等 MCP 客户端操作 Godot 4 编辑器的 MCP 服务器**

面向 Godot 4.5+ 的 MCP 服务器，提供 231 个工具：AI 可编辑活动场景树（经 Godot 撤销系统）、通过 DAP 设断点单步调试、走 GDScript LSP 做符号级重命名、运行游戏并回放输入/截图做试玩验证、headless 导出构建、执行 GUT 测试。特色是双向感知——AI 可轮询编辑器读取用户刚做的操作；默认仅加载 37 个工具以控制每请求 token 开销，工具集可用环境变量预置。以 fork 起家并大幅分叉。

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

- 231 个工具，默认加载 37 个，支持按工具集预置（GODOT_MCP_TOOLSETS）
- 双向感知：get_editor_activity 让 AI 读取用户的编辑器操作并区分人机行为
- DAP 断点调试、GDScript LSP 符号重命名、runtime 输入回放与截图对比
- 活动场景树编辑经 Godot 撤销系统，保护未保存改动

## 适用场景

- 让 AI 在 Godot 项目里搭场景、写脚本并接好信号
- AI 驱动断点调试，读取暂停帧的变量值定位物理穿透类 bug
- 自动 headless 导出游戏构建并跟踪状态
- 多人游戏脚手架与静默失败的 RPC 复制问题诊断

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: Every Godot MCP server lets an AI drive the editor. **This one also tells the AI what
> L122: - **Setup that explains itself** — `npx godot-mcp-bridge install` installs and enables the
> L9: 231 tools

## 星数曲线

```mermaid
xychart-beta
    title "TomasLucasUTN/godot-mcp-bridge 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-18"]
    y-axis "stars" 9 --> 12
    line [10, 11]
```

2026-10-25 10 → 2026-11-18 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `8fbb7f52a36a` · [字段定义](../../DATASET.md)*
