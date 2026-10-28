# seuros/skipper

⭐ 23 · Rust · BSD-2-Clause · 推送 2026-10-28 · [GitHub](https://github.com/seuros/skipper) · 个人维护

**面向 agent 的 git/代码托管 MCP 服务器，本地 git 加四大 forge**

用 Rust 编写的 MCP server（stdio），向 agent 暴露约 20 个精选工具：本地 git 经 gitoxide 进程内读写，GitHub/GitLab/Gitea/Forgejo 经 CLI 凭据接入，覆盖 CI 状态、PR 阅读/合并、issue 资源读取。默认所有工具只读（写操作 pr_merge/git_push 等需在全局配置开启并逐次确认）。工具可见性跟随仓库 remotes 动态变化。面向使用 MCP 客户端的开发者；限制：需对应 CLI（gh/glab/tea）认证后才有 forge 工具，部分 PR 功能仅限 GitHub。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 git 经 gitoxide 进程内操作，无需 git 二进制
- 默认全部只读，merge/push 等写操作需全局配置开启并经 MCP elicitation 逐次确认
- 工具可见性按仓库 remotes 动态评估，无需重启
- 自托管 forge 实例可通过配置映射 host

## 适用场景

- 让编码 agent 查看仓库状态、diff、日志与 CI 结果
- 让 agent 在受确认流程约束下合并 PR 或推送分支
- 跨 GitHub/GitLab/Gitea/Forgejo 用同一套工具词汇操作仓库

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: MCP server for working in a git repository: local git in-process, and
> L151: Either way you get the `skipper-mcp` binary. Skipper is a server, not a
> L157: Skipper speaks MCP over stdio. Add it to your client config:

## 星数曲线

```mermaid
xychart-beta
    title "seuros/skipper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `86b1e920eb24` · [字段定义](../../DATASET.md)*
