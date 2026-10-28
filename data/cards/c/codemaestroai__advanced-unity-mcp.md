# codemaestroai/advanced-unity-mcp

⭐ 94 · NOASSERTION · 推送 2026-03-30 · [GitHub](https://github.com/codemaestroai/advanced-unity-mcp) · 组织维护

**让 AI 助手通过自然语言控制 Unity 编辑器的 MCP 桥接工具**

由 Code Maestro 维护的 Unity MCP 桥接件：以 Unity 包形式安装，通过 Model Context Protocol 将 Unity 编辑器暴露给 AI 客户端，使开发者可用自然语言执行播放/暂停、创建材质/预制体/脚本、切换构建平台、ADB 操作、Profiler 控制等编辑器功能。提供两种连接模式：Code Maestro 桌面应用直连，或面向 VS Code/Cursor 等其他客户端的本地 TCP Bridge + 自动安装的 Relay Server。要求 Unity 2022+ 与一个 MCP 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言执行 Unity 编辑器操作：场景/材质/预制体/脚本管理、构建与平台切换
- 两种连接模式：Code Maestro 桌面应用直连、其他客户端经 Bridge + Relay Server
- 支持 GitHub Copilot (VS Code)/Cursor/Windsurf/Claude Desktop 等 MCP 客户端
- 覆盖 Unity Profiler 性能分析与 ADB 操作

## 适用场景

- 在 VS Code 或 Cursor 中用对话指令操作 Unity 场景与资源
- 让 AI 检查控制台报错并自动创建脚本或组件
- 通过语音式命令切换构建平台、执行 Android 构建流程

## 场景标签

 · 领域:游戏开发/AI 工具集成

## 证据(README 行号)

> L69: Unity MCP bridges your Unity Editor with AI assistants using the Model Context Protocol. It supports two connection

## 星数曲线

```mermaid
xychart-beta
    title "codemaestroai/advanced-unity-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-28 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `99e94010d5b9` · [字段定义](../../DATASET.md)*
