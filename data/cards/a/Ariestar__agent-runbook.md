# Ariestar/agent-runbook

⭐ 14 · Rust · MIT · 推送 2026-10-08 · [GitHub](https://github.com/Ariestar/agent-runbook) · [官网](https://agent-runbook.pages.dev/) · 个人维护 · 中文 README

**AI 编码 agent 的本地操作契约 CLI：扫描项目与机器环境生成工具选择与护栏**

Rust 编写的命令行工具，在 AI 编码 agent 修改文件前执行预检：从 Cargo.toml、package.json 等文件检测项目要求与机器可用工具，按类别与语言给出候选工具，通过 runbook prefer 将确认的仓库偏好写入 .runbook/preferences.yaml，并针对包管理器、密钥、远程写入与破坏性工具输出护栏。内置 YAML 工具注册表（awesome-agent-cli 子模块），可作为 MCP stdio 服务器运行，支持可选的本地 System One 决策服务器做自然语言任务推荐，另附 Codex agent skill 与浏览注册表的静态站点。

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

- runbook scan 输出事实型环境清单（仅事实，不写偏好）
- category/prefer 命令管理按语言与类别的工具候选与仓库偏好
- 可作为 MCP stdio 服务器供 AI agent 调用
- 内置 YAML 工具注册表，含风险等级与操作护栏

## 适用场景

- 让 AI 编码 agent 开工前了解项目该用的包管理器、测试器与 shell
- 为团队固化仓库级工具偏好并附带理由
- 对密钥、部署、破坏性操作等高风险动作设置确认门槛

## 场景标签

 · 领域:开发工具/AI agent 基础设施

## 证据(README 行号)

> L18: Runbook scans the current project and machine before an AI coding agent starts changing files. It turns local facts
> L151: |`runbook mcp`|Run as an MCP (Model Context Protocol) stdio server for AI agents|

## 星数曲线

```mermaid
xychart-beta
    title "Ariestar/agent-runbook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5993ffff1129` · [字段定义](../../DATASET.md)*
