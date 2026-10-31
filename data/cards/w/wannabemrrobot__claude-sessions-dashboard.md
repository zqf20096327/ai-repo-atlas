# wannabemrrobot/claude-sessions-dashboard

⭐ 13 · Python · MIT · 推送 2026-07-29 · [GitHub](https://github.com/wannabemrrobot/claude-sessions-dashboard) · 个人维护

**本地浏览/搜索/恢复 Claude Code 会话的仪表盘**

单文件 Python 脚本，扫描 ~/.claude/projects 下的 .jsonl 会话文件，在浏览器中提供会话列表、全文搜索、完整对话转录（Markdown 渲染、工具调用折叠）、artifacts 文件视图（含 diff）与 token/时长统计，并支持重命名、删除、复制 resume 命令。仅用标准库、零依赖、零网络请求，仅绑定 127.0.0.1。面向积累大量 Claude Code 会话需要回溯与管理的开发者，静态模式可导出单 HTML。

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

- 读取 ~/.claude/projects 会话文件并渲染完整对话转录与 artifacts diff
- 运行中检测、token/活跃时长统计与可选成本估算
- 纯 Python 标准库、零依赖、仅监听 127.0.0.1
- --demo 演示模式与 --static 单 HTML 导出

## 适用场景

- 翻找并一键恢复历史 Claude Code 会话
- 查看某会话实际产出了哪些文件及改动
- 统计各模型的 token 用量与工作时长

## 场景标签

 · 领域:开发者工具/AI 会话管理

## 证据(README 行号)

> L13: Claude Code stores each session as a `.jsonl` file under `~/.claude/projects/…`. Over time you accumulate hundreds,
> L131: It scans `~/.claude/projects/<encoded-cwd>/<uuid>.jsonl`, extracts each session's title, project, branch, timestam

## 星数曲线

```mermaid
xychart-beta
    title "wannabemrrobot/claude-sessions-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `23e575ab96b6` · [字段定义](../../DATASET.md)*
