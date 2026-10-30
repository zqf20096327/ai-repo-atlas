# ZachRouan/gridhand

⭐ 17 · Rust · MIT · 推送 2026-10-02 · [GitHub](https://github.com/ZachRouan/gridhand) · [官网](https://crates.io/crates/gui-tool) · 个人维护

**面向 AI agent 的零依赖 Rust GUI 自动化 CLI：截图/窗口/键鼠控制**

跨平台（GNOME/Wayland、macOS 10.15+、Windows 8+）Rust 命令行工具，为 AI 桌面 agent（Claude Code、Codex、Gemini CLI）提供截图、窗口管理、鼠标与键盘控制，所有命令 JSON 输出。核心机制是在截图上叠加带标记的网格，agent 按网格单元名点击而非猜测像素坐标，支持递归缩放与单元间定位；不依赖系统辅助功能树，纯 OS API 实现（约 9,100 行，无外部 crate），编译为单一二进制。附 Agent Skills 标准 SKILL.md 可装入 Claude Code。已知限制：macOS 窗口前置仅激活所属应用、截图 API 在 macOS 14 已标记弃用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网格定位：截图叠加标记网格与十字准星，按单元名点击，支持递归缩放（如 B2.C1）与单元间定位（D3+E3）
- 零依赖纯 std Rust，直连 OS API（CoreGraphics、user32.dll、D-Bus），单二进制
- 原生支持 GNOME/Wayland（XDG Portal + window-calls 扩展）
- 提供符合 Agent Skills 标准的 SKILL.md 供 Claude Code 等使用

## 适用场景

- 让 AI agent 自动化无 CLI/API 的 GUI 软件（安装器、设置面板、专有工具）
- 点击辅助功能树缺失或不完整的界面：游戏、canvas/WebGL、Flutter、远程桌面
- 让 agent 通过点击复现并截图调试 GUI 应用问题

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: Built for AI desktop agents (Claude Code, Codex, Gemini CLI, and friends), but it works fine as a general-purpose G
> L21: **Why it's different:** agents are bad at guessing pixel coordinates from a screenshot, and every other automation 
> L102: A skill definition following the Agent Skills standard is included in `skills/gridhand/SKILL.md`.

## 星数曲线

```mermaid
xychart-beta
    title "ZachRouan/gridhand 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ba40228fd723` · [字段定义](../../DATASET.md)*
