# yazinsai/auto-maintainer

⭐ 54 · TypeScript · MIT · 推送 2026-04-23 · [GitHub](https://github.com/yazinsai/auto-maintainer) · [官网](https://www.npmjs.com/package/auto-maintainer) · 个人维护

**用 Markdown 写仓库规则、由 Claude 自主维护仓库的工具**

面向仓库维护者的 npm CLI：通过 npx init 生成四个 GitHub Actions 工作流与策略文件，AI 按规则自动分派 issue、审查 PR、写修复并提 PR、CI 通过后自动合并、打版本发布；高风险或含糊事项标记 awaiting-human 交人工决定。规则用纯 Markdown 编写，可使用 Claude 订阅或 Anthropic API key，triage bot 无代码写入权限，Actions 固定到 commit SHA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Markdown 策略文件驱动 AI 维护行为
- 四个 GitHub Actions 工作流覆盖 triage/implement/merge/release 全流程
- 高风险、重大版本、可疑内容自动升级给人工
- triage bot 无 shell 与文件编辑权限，Actions 固定 commit SHA

## 适用场景

- 积压 issue 和 PR 较多的仓库做自动分派与处理
- 按自定义规则自动审查 PR、写修复并合并
- 自动判断版本号并发布 patch/minor 版本

## 场景标签

`工作流自动化` `编码 Agent` `代码审查` · 领域:效率与自动化

## 证据(README 行号)

> L11: auto-maintainer triages issues, reviews PRs, fixes bugs, merges code, and cuts releases — autonomously. It reads a 
> L27: - **Use your existing Claude subscription** — works with Claude Pro, Max, or Team plans. No separate API billing re

## 星数曲线

```mermaid
xychart-beta
    title "yazinsai/auto-maintainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-28 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `751a4abd45b4` · [字段定义](../../DATASET.md)*
