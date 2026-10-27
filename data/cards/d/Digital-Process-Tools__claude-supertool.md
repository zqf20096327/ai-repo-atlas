# Digital-Process-Tools/claude-supertool

⭐ 26 · Python · NOASSERTION · 推送 2026-10-05 · [GitHub](https://github.com/Digital-Process-Tools/claude-supertool) · [官网](https://github.com/Digital-Process-Tools/claude-marketplace) · 组织维护

**Claude Code 的批量操作插件：合并文件/git/看板调用减少轮次**

面向 Claude Code 用户的插件：将多次文件读取、grep、git 状态、PR/MR 看板等操作合并为一次 Bash 往返，以减少输出 token、缓存增长与耗时。仅用标准库，无第三方依赖。内置约四十个操作，覆盖文件、git、GitHub、GitLab 及 Claude Code 会话日志，另可按项目添加 preset。通过 Claude Code 的 plugin marketplace 安装；本构建不含涉及凭据外发的 bluesky/slack/youtube 等 preset。

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

- 将 N 次读取/grep/glob 合并为一次 Bash 往返
- 约 40 个内置操作，覆盖文件、git、GitHub、GitLab 与会话日志
- 仅标准库，无第三方依赖
- 含检测疑似 prompt 注入文本的操作

## 适用场景

- Claude Code 自主运行时降低 token 消耗与调用次数
- 一次调用获取 PR/MR 看板或批量读文件加搜索
- 检查文本中疑似操纵 agent 的指令

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L3: Cuts your Claude Code bill by batching file, git and tracker operations into one
> L8: Claude Code's default tools read one file, grep one pattern, or print a bare git
> L21: /plugin marketplace add Digital-Process-Tools/claude-marketplace

## 星数曲线

```mermaid
xychart-beta
    title "Digital-Process-Tools/claude-supertool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fb96a2874fca` · [字段定义](../../DATASET.md)*
