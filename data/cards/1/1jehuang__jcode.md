# 1jehuang/jcode

⭐ 21,987 · Rust · MIT · 推送 2026-11-22 · [GitHub](https://github.com/1jehuang/jcode) · [官网](https://jcode.sh) · 个人维护

**面向重度多 Agent 工作流的 Rust 编码 Agent 运行框架**

以 Rust 编写的终端 TUI 编码 Agent 工具，主打在同一仓库并行运行数十个 Agent 会话：内置服务器管理多 Agent 协作，当 Agent A 修改了 Agent B 已读取的文件时通知后者并可自动解决冲突；Agent 间支持私信、广播与自主生成 Swarm 分工。支持 Claude 与 OpenAI Codex 的 OAuth 接入，提供会话恢复菜单、内联图片与 LaTeX 渲染、KV cache 与 token 优化。安装提供 macOS/Linux 脚本，支持 stable/prerelease 更新通道与热更新。README 中性能数据为自测基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 100,44 位贡献者
- 涨星:近 1 天 **+62**(自 20261016 起算)
- 下载:GitHub Release 附件 累计 531,938(100 个 release)
- 平台:WINDOWS / MACOS / LINUX · 协议:—

## 能力要点

- 多 Agent 同仓库并行协作，服务器管理冲突通知与解决
- Agent 可自主 spawn Swarm，主 Agent 转为协调者
- 支持 Claude OAuth 与 OpenAI Codex OAuth 多提供商
- self-dev 模式：Agent 修改自身源码并重载二进制

## 适用场景

- 在同一代码仓库同时运行多个编码 Agent 并行开发
- 让 Agent 自主组建 Swarm 分工完成任务
- 在低内存机器上并行开多个 Agent 会话

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7:  High-performance coding agents.
> L83: Spawn two or more agents in the same repo, and they will automatically be managed by the server to allow native col
> L89: Supports a wide range of providers, including Claude OAuth and OpenAI Codex OAuth.

## 星数曲线

```mermaid
xychart-beta
    title "1jehuang/jcode 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 20942 --> 22082
    line [21037, 21094, 21124, 21164, 21183, 21199, 21223, 21254, 21283, 21306, 21327, 21365, 21392, 21183, 21618, 21683, 21701, 21727, 21753, 21774, 21794, 21821, 21855, 21890, 21914, 21945, 21972, 21987]
```

2026-10-21 21,037 → 2026-11-23 21,987（+950）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `d2f4fe09a219` · [字段定义](../../DATASET.md)*
