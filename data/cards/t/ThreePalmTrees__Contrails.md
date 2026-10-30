# ThreePalmTrees/Contrails

⭐ 19 · Go · MIT · 推送 2026-10-11 · [GitHub](https://github.com/ThreePalmTrees/Contrails) · [官网](https://getcontrails.com) · 个人维护

**桌面应用：自动将 AI 编码代理会话存为可检索的 Markdown**

基于 Wails v2（Go + React + TypeScript）的开源桌面应用（macOS/Windows/Linux），实时监视 VS Code Copilot、Claude Code、Cursor、OpenCode 四种编码代理的会话文件（JSONL/SQLite），解析为保持原始顺序的 Markdown 写入项目仓库 contrails/ 目录，使代理对话进入仓库历史。发现机制含 fsnotify 文件监听与 Claude Code Stop hook 信号文件（每 5 秒校验并重装）。支持多代理项目、删除会话打标记、可选匿名遥测（可开关）。Linux 需 WebKit2GTK/GTK3 运行库。

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

- 支持 VS Code Copilot、Claude Code、Cursor、OpenCode 四种代理会话捕获
- fsnotify 实时监听 + Claude Code Stop hook 信号捕获（自动重装校验）
- 解析保留文本、thinking 块、工具调用与文件编辑的原始顺序，输出 Markdown
- 同一项目可同时接入多个代理来源

## 适用场景

- 把编码代理的推理过程和修 bug 思路归档到仓库，便于日后参考
- 让后续相关任务中代理可引用此前的会话推理
- 统一管理多个 IDE/代理的工作区会话记录

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L15: Contrails is an opensource app (macOS, Windows and Linux) that:
> L16: 1. Watches your coding agent sessions _(VS Code Copilot, Claude Code, Cursor, and OpenCode)_
> L17: 2. Parses them into readable Markdown

## 星数曲线

```mermaid
xychart-beta
    title "ThreePalmTrees/Contrails 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4b629bb14a87` · [字段定义](../../DATASET.md)*
