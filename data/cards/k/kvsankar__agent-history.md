# kvsankar/agent-history

⭐ 15 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/kvsankar/agent-history) · 个人维护

**浏览与导出多种 AI 编程助手对话历史的 CLI**

单文件 Python CLI（仅标准库），读取 Claude Code、Codex CLI、Gemini CLI 和 Pi 的本地会话文件（JSONL/JSON），归一化为统一的 workspace/session 模型，提供会话/工作区列表、Markdown 与离线 HTML 导出、别名管理与使用统计（token/工具/时长，SQLite 存储）。支持本地、WSL、Windows 与 SSH 远程多环境访问；附带的安装命令会部署 Claude skill 并把 cleanupPeriodDays 调大以防历史被清理。需 Python 3.6+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 AI 编程助手（Claude Code/Codex CLI/Gemini CLI/Pi）会话格式的完整读取支持
- Markdown/离线 HTML 导出，含逐轮对话与工具 I/O 视图
- 跨本地/WSL/Windows/SSH 多环境扫描与工作区别名
- 使用统计（token/工具/时长）存于小型 SQLite，仅标准库无 pip 依赖

## 适用场景

- 按项目找回过去与 AI 助手的对话记录而非靠 session ID
- 导出会话为 Markdown/HTML 用于分享、备份或审计
- 统计自己跨环境的 AI 编程时长与 token 用量

## 场景标签

 · 领域:开发者工具/AI 助手数据管理

## 证据(README 行号)

> L5: A CLI tool to browse and export AI coding assistant conversation history with multi-environment support.
> L17: |Claude Code|✅ Full support|JSONL|claude-format.md|
> L22: Use `--agent claude`, `--agent codex`, `--agent gemini`, `--agent pi`, or `--agent auto` (default) to select which 

## 星数曲线

```mermaid
xychart-beta
    title "kvsankar/agent-history 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `1d1bf7c759e3` · [字段定义](../../DATASET.md)*
