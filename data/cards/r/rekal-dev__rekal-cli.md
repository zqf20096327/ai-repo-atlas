# rekal-dev/rekal-cli

⭐ 205 · Go · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/rekal-dev/rekal-cli) · [官网](https://rekal.dev) · 组织维护

**给 AI 编码 agent 的 git 团队记忆 CLI：留存每次会话的决策推理**

命令行工具，在每次 git commit 时捕获 AI 编码会话的原始转录，存入仓库内 `.rekal/` 目录并本地后台索引与嵌入，供 Claude Code、Cursor、Copilot、Codex、Gemini、Kiro、OpenCode 等 agent 检索决策推理与已被否决的方案。团队共享通过既有 git push/fetch 在孤儿分支上传输，无服务器与账号；嵌入本地运行，转录入库前经密钥脱敏。单二进制约 170MB，内置推理引擎与嵌入模型，离线可用；支持 macOS Apple Silicon 与 Linux x86-64/arm64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次 commit 自动捕获会话并通过 git push/fetch 团队共享
- 单二进制内置嵌入模型与 DuckDB 类存储，离线本地检索，无外部服务
- 入库前做密钥脱敏与家目录匿名化
- 混合检索输出 INJECT/KNOWLEDGE/SILENCE 判定与种子摘要，~7.5K 上下文

## 适用场景

- 团队 agent 共享历史决策，避免重新提议已被否决的方案
- 在提交历史中回溯某次变更背后的推理与备选方案
- 让不同编码工具读取同一份团队记忆账本

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Rekal is a command-line tool that captures your AI coding sessions at every git
> L27: Every AI session settles decisions: why this approach, what got tried and thrown away. Then the session ends and th

## 星数曲线

```mermaid
xychart-beta
    title "rekal-dev/rekal-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 204 --> 208
    line [207, 205, 205]
```

2026-10-18 207 → 2026-10-24 205（-2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f679fd3510b3` · [字段定义](../../DATASET.md)*
