# csmarvz/claude-resume

⭐ 4 · Go · MIT · 推送 2026-11-04 · [GitHub](https://github.com/csmarvz/claude-resume) · 个人维护

**为 Claude Code 用户提供会话查找、预览、恢复与删除的 CLI 工具**

读取 Claude Code 存储在 ~/.claude/projects 的会话文件，提供交互式 picker 与命令行两种方式，列出、预览、搜索、恢复、重命名、置顶、归档、删除会话，并支持导出 Markdown、ZIP 备份与恢复、回收站 30 天保留、通过 /pin 或 /archive 防止 Claude Code 自动清理。单文件无依赖安装，恢复会话依赖 claude CLI。作者自述为 alpha 软件，直接读取非公开的内部文件格式，Claude Code 更新可能使其失效；macOS 与 Windows 构建未经真机测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 交互式 picker：预览、过滤、/ 命令（pin/archive/fork/export/delete 等）
- 会话导出为 Markdown、ZIP 备份与校验式恢复
- pin/archive 对抗 Claude Code 默认 30 天清理
- 跨平台安装脚本，二进制自更新并校验 SHA-256

## 适用场景

- 在任意目录快速找到并恢复之前的 Claude Code 会话
- 删除或归档不需要的会话，管理 ~/.claude 占用
- 备份重要会话防止 Claude Code 自动清理
- 把会话内容导出为 Markdown 存档

## 场景标签

 · 领域:开发者工具/AI 会话管理

## 证据(README 行号)

> L5: List all your claude sessions and resume them in the folder they were started in.
> L27: The only other requirement is the `claude` CLI, to resume sessions. Updates use the system `curl`.

## 星数曲线

```mermaid
xychart-beta
    title "csmarvz/claude-resume 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-11-20", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-30 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ad1e7d14e3fd` · [字段定义](../../DATASET.md)*
