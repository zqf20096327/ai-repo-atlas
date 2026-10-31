# aivanelabs/ai-rpa

⭐ 14 · Python · MIT · 推送 2026-09-09 · [GitHub](https://github.com/aivanelabs/ai-rpa) · 组织维护 · 中文 README

**桌面或 AI agent 局域网控制 Android 手机的自动化工具（Beta）**

AIVane Android REPL Beta：手机端运行轻量 HTTP 服务，桌面 CLI（agent-android）通过局域网直连，实现 UI 检查、点击、输入、启动应用、截屏等 inspect-act-inspect 工作流；同时提供可安装的 agent-android skill，供 Codex、Claude Code、OpenClaw 等编码 agent 驱动手机。含 Python 客户端、模板与模板 linter、示例和协议文档。限制：仅限 LAN、不支持 iOS、非云手机农场。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 手机作为本地 HTTP 服务，桌面经 LAN 直连控制（UI 检查/点击/输入/截屏）
- 面向人类的 REPL 与面向 AI agent 的 skill 双路径
- 模板校验 linter（aivane-template-lint）与应用包（application bundle）执行机制
- 上传与模板内 http.download/http.get 的文件同步能力

## 适用场景

- 在桌面用 REPL 手动探索和操作 Android 手机
- 让 Codex/Claude Code 等 agent 通过 skill 执行手机任务（如加日历、搜索）
- 编写并 lint 模板化的手机自动化工作流

## 场景标签

`GUI 自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Control an Android phone from your desktop or AI agent in minutes: inspect UI, tap, type, launch apps, and capture s
> L7: This repository is the public home for `aivanelabs/ai-rpa`. The current public surface is **AIVane Android REPL Beta
> L72: Use the skill when you want Codex, Claude Code, or another coding agent to drive the phone:

## 星数曲线

```mermaid
xychart-beta
    title "aivanelabs/ai-rpa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `df5c301b8174` · [字段定义](../../DATASET.md)*
