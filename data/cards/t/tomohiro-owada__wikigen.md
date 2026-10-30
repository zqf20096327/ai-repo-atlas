# tomohiro-owada/wikigen

⭐ 34 · Go · 推送 2026-03-20 · [GitHub](https://github.com/tomohiro-owada/wikigen) · 个人维护

**用 Claude Code 从源码生成 GitHub Wiki 的单二进制 CLI 工具**

Go 单二进制命令行工具：克隆（或读取本地）仓库后调用 Claude Code（claude -p），由其用 Read/Grep/Glob/Bash 直接读源码，生成 GitHub Wiki 兼容的 Markdown（Home、_Sidebar 等），可直接 push 到 {repo}.wiki.git。面向希望自动化代码文档的开发者。支持多仓库跨库文档、并行生成、自动重试、JSON 输出，并提供 GitHub Actions 工作流在 push 时自动更新 Wiki。前置条件为 git 与已认证的 claude CLI；不依赖 Docker、Ollama 或 embedding。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Code 原生工具（Read/Grep/Glob/Bash）直接读源码，无需 RAG/embedding 基础设施
- 多仓库模式生成跨仓库架构文档
- GitHub Actions 工作流实现 push 时自动更新 Wiki
- 自动重试（每页最多3次）、增量保存与 -retry 仅重生成失败页

## 适用场景

- 为我的仓库自动生成并维护 GitHub Wiki 文档
- 多仓库项目生成跨服务架构说明
- 在 CI 中随代码变更自动更新文档

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A single Go binary CLI that generates GitHub Wiki from source code using Claude Code.
> L5: Claude Code (`claude -p`) reads the repository code directly — using Read, Grep, Glob, and Bash tools — and writes G
> L16: wikigen → git clone (SSH) → claude -p --add-dir ./repo

## 星数曲线

```mermaid
xychart-beta
    title "tomohiro-owada/wikigen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e173034fe0a2` · [字段定义](../../DATASET.md)*
