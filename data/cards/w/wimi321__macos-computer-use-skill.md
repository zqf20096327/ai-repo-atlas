# wimi321/macos-computer-use-skill

⭐ 20 · TypeScript · MIT · 推送 2026-04-19 · [GitHub](https://github.com/wimi321/macos-computer-use-skill) · [官网](https://clawhub.ai/wimi321/computer-use-macos) · 个人维护 · 中文 README

**让 AI agent 通过 MCP 完全控制 macOS 图形界面的独立服务器**

独立运行的 MCP 服务器（TypeScript + stdio），向 AI agent 提供 28 个 GUI 控制工具：截图与多显示器缩放、鼠标键盘操作（含 IME 安全的剪贴板路由输入）、应用启动与权限管理、剪贴板读写、批量动作与教学模式。首次运行自动创建 Python 虚拟环境并安装依赖（pyautogui、mss、Pillow、pyobjc）。需 macOS 12+、Node.js 20+、Python 3.10+ 及辅助功能/屏幕录制权限；可经 ClawHub 或仓库脚本安装为独立 skill。

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

- 28 个 MCP 工具覆盖截图、鼠标键盘、应用、剪贴板与多显示器
- 批量动作（computer_batch）与教学模式（teach_step/teach_batch）
- 首次运行自动创建 Python virtualenv 并安装依赖，无私有依赖
- 可安装为独立 skill，脱离源仓库仍可工作

## 适用场景

- 让 MCP 客户端中的 agent 操作 macOS 桌面完成自动化任务
- 基于截图与坐标的 agent 视觉-操作工作流
- 通过教学模式分步录制/执行桌面操作

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6:  Standalone MCP server that gives AI agents full GUI control over macOS — screenshots, mouse, keyboard, apps, clipbo
> L64:     A[AI Agent / MCP Client] --> B[MCP Server<br/>TypeScript + stdio]

## 星数曲线

```mermaid
xychart-beta
    title "wimi321/macos-computer-use-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8f25741e7888` · [字段定义](../../DATASET.md)*
