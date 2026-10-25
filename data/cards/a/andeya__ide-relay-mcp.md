# andeya/ide-relay-mcp

⭐ 72 · Rust · MIT · 推送 2026-04-27 · [GitHub](https://github.com/andeya/ide-relay-mcp) · 个人维护 · 中文 README

**给 AI 编程 agent 加人工审查检查点的 MCP 桌面工具**

基于 Tauri 2 + Rust + Vue 3 的本地桌面应用，为任意支持 MCP 的编程 agent 提供人机协同（HITL）检查点：agent 调用 relay_interactive_feedback 工具即阻塞，用户在 IDE 旁的常驻多标签窗口中审查、纠错或补充文本/截图/文件后，结果经同一 JSON-RPC 往返返回。首类支持 Cursor、Claude Code、Windsurf，提供一键 MCP 注入、规则提示安装与 Cursor 用量监控。数据全部本地，仅通过 127.0.0.1 回环通信。macOS 包未经 Apple 公证，需手动放行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一工具 relay_interactive_feedback 实现阻塞式人工确认往返
- Cursor/Claude Code/Windsurf 专项模式 + 其他 IDE 通用模式
- 常驻多标签 GUI，会话 ID 串联多轮，支持文本/图片/文件附件
- Cursor 用量监控：自动解密 token、查看配额与请求历史

## 适用场景

- 让 AI 编程 agent 每步执行前暂停，由我审查后再继续
- 在 agent 跑偏早期纠正，减少浪费的修正轮次
- 通过附件向 agent 补充截图或文件上下文

## 场景标签

 · 领域:AI 编程工具/工作流

## 证据(README 行号)

> L27: Relay adds a **human-in-the-loop (HITL) checkpoint** to any MCP-capable agent. The agent calls one tool — **`relay_
> L33: |**Works with any MCP IDE**|First-class support for **Cursor**, **Claude Code**, **Windsurf**, and a generic mode f

## 星数曲线

```mermaid
xychart-beta
    title "andeya/ide-relay-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-25 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `22c71226f305` · [字段定义](../../DATASET.md)*
