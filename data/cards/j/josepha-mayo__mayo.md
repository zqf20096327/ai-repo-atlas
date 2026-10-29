# josepha-mayo/mayo

⭐ 17 · Python · 推送 2026-10-15 · [GitHub](https://github.com/josepha-mayo/mayo) · [官网](https://joe-gemini.vercel.app) · 个人维护

**自主维护 GitHub 仓库的三模型 agent，每小时提交改进 PR**

部署为 GitHub App + Vercel 的自治维护引擎：每小时 cron 触发，Scanner 多层分析代码库（安全/逻辑/DX/性能/一致性），Executor 以最多 10 行的 search/replace 块产出编辑，Reviewer 校验后创建 PR。模型来自 Gemini 2.5 Flash、Fireworks AI（Llama 3.3 70B）与 Groq（Llama 3.1 8B），并维护跨仓库持久记忆。使用方式为 fork 本仓库、替换个人引用与 API key、自建 GitHub App 后部署；README 作者自述依赖多个免费额度 key 并配有大量回退配置。

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

- Scanner/Executor/Reviewer/NewCrons 四角色的三模型流水线
- search/replace 块（每块≤10行）方式产出编辑
- 跨仓库持久记忆，根据真实 PR 状态更新经验
- 每小时 cron 自主运行并创建经 Reviewer 校验的 PR

## 适用场景

- 让 agent 定期扫描并提交仓库改进 PR
- 自动发现安全问题、边界情况与文档缺失
- 多仓库间共享维护经验与教训

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L4: Mayo is a **Self-Improving Autonomous Maintenance Engine** integrated directly into your GitHub ecosystem. It uses a
> L12:     A["Hourly Cron Trigger"] --> R0["REVIEWER: Audit pending PR statuses"]
> L13:     R0 --> B["SCANNER: Deep codebase analysis"]

## 星数曲线

```mermaid
xychart-beta
    title "josepha-mayo/mayo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6c6eb61a56b4` · [字段定义](../../DATASET.md)*
