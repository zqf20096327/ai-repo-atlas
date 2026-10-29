# mr-karan/hodor

⭐ 112 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/mr-karan/hodor) · 个人维护

**给开发者的 LLM Agent 代码审查工具：自动审查 PR/MR**

面向 GitHub PR、GitLab MR、Gitea/Forgejo PR 及本地 diff 的 agentic 代码审查工具。它检出变更，给 LLM agent 提供受限的只读检查工具（git_diff/read/grep/find/ls），让其跨文件分析并产出结构化发现，以行内评论和摘要形式发布或本地打印。支持多 provider（Anthropic/OpenAI/Bedrock/OpenRouter 等），提供增量审查、diff 内嵌、identical-HEAD 复用等 token 优化，可推送 Prometheus 指标并输出 CI 日志。通过 npx/npm 或 Docker 镜像运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM agent 携带受限只读工具（git_diff/read/grep/find/ls）跨文件分析
- 支持 GitHub/GitLab/Gitea/Forgejo 及本地 diff 审查
- 增量审查、diff 内嵌、identical-HEAD 复用等 token 优化机制
- 可推送 Prometheus/VictoriaMetrics 指标，附 Grafana 面板

## 适用场景

- 在 CI 中自动审查 PR 并发布行内评论与摘要
- 推送前审查本地未提交变更
- 按 P0-P3 优先级门禁使 CI 失败
- 接入自托管或第三方 LLM 端点做代码审查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: > Agentic code reviewer for GitHub PRs, GitLab MRs, Gitea/Forgejo PRs, and local diffs.
> L5: Hodor checks out the change, gives an LLM agent confined inspection tools (`git_diff`, `read`, `grep`, `find`, `ls`)
> L75: |`--model`|`anthropic/claude-opus-5-5`|LLM model as `provider/model-id`. Tested: Anthropic, OpenAI, Bedrock, OpenRo

## 星数曲线

```mermaid
xychart-beta
    title "mr-karan/hodor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-29 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1deba95d13b6` · [字段定义](../../DATASET.md)*
