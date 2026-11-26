# orbi-build/orbi

⭐ 260 · Python · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/orbi-build/orbi) · [官网](https://orbi.build) · 组织维护 · 中文 README

**自托管自动化软件交付系统：标签 Issue 换取已评审合并的 PR**

面向 GitHub 仓库的自动化交付流水线：给 Issue 打 `ai-ready` 标签后，系统在隔离 worktree 中实现代码、运行测试、开 PR，并经独立评审会话修复发现项后合并；请求发布时执行发布门禁并产出标签与发布说明。以 GitHub Issues 作为唯一状态存储，无数据库、队列或守护进程，由 systemd/launchd 定时器每 5 分钟触发一次 tick。依赖 uv、Pi 及其 provider、GitHub CLI ≥ 2.99，要求 Python ≥ 3.14。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Issue 标签触发完整交付循环：实现→测试→PR→独立评审→合并→发布
- 独立评审会话与合并门禁，AI 不得合并或推送受保护分支
- GitHub Issues 为唯一状态存储，run_id 串联日志与进度评论
- 失败自动分类：可恢复回 PR 继续修复，不可恢复标记 ai-blocked 留给人工

## 适用场景

- 把打了标签的 Issue 委托给自动化流程产出已评审合并的 PR
- 在无人值守节奏下定期消化仓库积压的技术债与 bug Issue
- 希望交付记录直接沉淀在 GitHub Issues/PR/CI 中无需额外任务系统

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: Orbi is an open-source **software dark factory**: a software delivery system for GitHub. You define the goal and ac
> L63: - **Independent review + merge gates**: after a PR opens, an independent review session reviews it and fixes findin
> L72:   → Pi development: plan → implement → test → verify

## 星数曲线

```mermaid
xychart-beta
    title "orbi-build/orbi 星数(近 17 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-22", "2026-11-26"]
    y-axis "stars" 222 --> 263
    line [225, 229, 231, 233, 239, 240, 229, 247, 248, 249, 248, 254, 255, 258, 259, 260, 260]
```

2026-10-24 225 → 2026-11-26 260（+35）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `44c8d1a04dc3` · [字段定义](../../DATASET.md)*
