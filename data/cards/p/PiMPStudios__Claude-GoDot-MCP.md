# PiMPStudios/Claude-GoDot-MCP

⭐ 14 · GDScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/PiMPStudios/Claude-GoDot-MCP) · 个人维护

**让 Claude 直接控制 Godot 编辑器的 MCP 服务器（170 工具）**

面向 Claude Code / Claude Desktop 的 Model Context Protocol 服务器，由 Godot 编辑器插件（监听 3571 端口）与 Python 服务器组成，提供 170 个工具：场景/节点操作、GDScript 创建编辑、信号连接、Autoload 管理、着色器参数、运行时测试（模拟键鼠输入）、性能剖析快照、截图反馈、导出流水线、TileMap/GridMap 绘制、批量操作与音频控制等。要求 Godot 4.2+ 与 Python 3.10+，通过 uv 安装，复制插件目录到项目 addons 启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 170 个工具覆盖场景/节点/脚本/信号/资源等 Godot 开发环节
- 运行时测试：播放场景、模拟键盘鼠标输入、检查运行节点
- 性能剖析快照（FPS/内存/Draw calls + 瓶颈警告）与截图反馈
- 导出流水线：读写导出预设并触发 headless 构建

## 适用场景

- 用一句话让 Claude 在 Godot 里搭建完整游戏场景
- 让 AI 模拟输入运行并测试游戏、截图检查效果
- 通过对话批量修改节点属性或脚本内容

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: A Model Context Protocol server that gives Claude direct, real-time control over the Godot editor:
> L28: ## Quick Setup (Claude Code)

## 星数曲线

```mermaid
xychart-beta
    title "PiMPStudios/Claude-GoDot-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `72c7ab497029` · [字段定义](../../DATASET.md)*
