# Microck/hermes-nightshift-glm

⭐ 14 · Python · MIT · 推送 2026-05-28 · [GitHub](https://github.com/Microck/hermes-nightshift-glm) · 个人维护 · 中文 README

**给 Hermes Agent 用户的 GLM 自动化夜班代码质量机器人**

单文件 Python 脚本 + 任务定义 JSON，以 cron 定时运行：检测 GLM 配额燃烧窗口（重置前 5–50 分钟），从用户的公开 GitHub 仓库挑选任务，克隆仓库后委托 GLM 5.1 编码代理执行 plan→implement→review 循环（最多重试 3 次），按任务类型产出 PR 或带 P0–P3 分级的 GitHub issue。共 63 个任务分 7 类，含冷却期、成本分层、每仓库 PR 上限等约束。需 GLM API key，PR 从独立 bot 账号的 fork 发起。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 配额门控：仅在 GLM 配额燃烧窗口内按剩余额度决定任务数
- 63 个任务（21 个 PR 任务 + 42 个 issue 分析任务），带成本分层与冷却期
- plan→implement→review 循环，review 失败带反馈重试（最多 3 次）
- 从独立 bot 账号 fork 仓库并发起 PR，保持主账号时间戳干净

## 适用场景

- 利用 GLM 订阅配额的剩余额度自动做代码维护
- 自动修复 lint、死代码、CI 问题并开 PR
- 自动生成安全/测试/性能等分析报告为 GitHub issue

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: `nightshift` runs on a cron schedule during GLM's quota burn window, selects from your public GitHub repos, and auto
> L16: 4. **execute** — clones the repo, runs the task via a coding agent (GLM 5.1)
> L61: hermes cron create "nightshift" --skill nightshift --schedule "*/15 * * * *" --model glm-5.1 --deliver discord

## 星数曲线

```mermaid
xychart-beta
    title "Microck/hermes-nightshift-glm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `07e3b70fa60b` · [字段定义](../../DATASET.md)*
