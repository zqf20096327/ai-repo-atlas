# JackLuciano/claude-bridge-blender

⭐ 4 · Python · GPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/JackLuciano/claude-bridge-blender) · [官网](https://github.com/JackLuciano/claude-bridge-blender#readme) · 个人维护

**在 Blender 内对话驱动建模的 Claude 桥接插件**

Blender 4.2+ 扩展插件，在 3D 视图侧栏提供聊天面板，通过 Claude Code CLI（无头模式、使用用户自身订阅）以 MCP stdio 与本地 TCP 端口连接插件，进而经 bpy 操作场景。提供 45 个高层级 op（建模、材质、节点、灯光、动画、渲染、游戏资产导出等）替代临时 Python 脚本，支持批量执行、内置校验与一键撤销。三种聊天模式（Build/Plan first/Coach）、会话历史、截图与图片粘贴、场景上下文随消息发送。需 Blender 4.2+ 与已登录的 Claude Code，不需要 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 45 个紧凑 op 覆盖建模/材质/节点/动画/渲染/导出，批量一次调用一次撤销
- 经 Claude Code CLI 运行在用户订阅（Pro/Max）上，无需 API key
- 三种模式：Build、Plan first、Coach（只看不改，本地校验）
- 每个 op 回复内置结果校验，支持一键 Revert

## 适用场景

- 在 Blender 里用自然语言构建和修改场景
- 用 Claude Code 终端直接操控打开的 Blender 工程
- 生成游戏可用资产并导出到 Unity/Unreal/Godot

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: Drive a live Blender with Claude, **from a chat panel inside Blender** or **from Claude Code**, using
> L27:                                                                      ├─ MCP stdio ─▶ mcp_server.py ─TCP 127.0.0.1:9
> L94:  - Two MCP tools with a ~1.3k-token schema covering 45 ops.

## 星数曲线

```mermaid
xychart-beta
    title "JackLuciano/claude-bridge-blender 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-25"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-25 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `54a0f6c0f62e` · [字段定义](../../DATASET.md)*
