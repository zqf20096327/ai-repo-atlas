# mikecsmith/ihj

⭐ 60 · Go · 推送 2026-06-22 · [GitHub](https://github.com/mikecsmith/ihj) · 个人维护

**fzf 风格的终端 issue 跟踪器，含 LLM 辅助待办精炼**

用 Go 编写的 TUI issue 跟踪工具，面向使用 Jira 的开发者：分栏界面、模糊搜索、vim 模式、多工作区切换，所有 TUI 操作均有对应 CLI 命令。LLM 部分：用 ihj extract 把待办导出为结构化 XML，交由外部 LLM 精炼后用 ihj apply 回写 YAML，每个字段变更经交互式 diff 逐项确认才写入。当前仅支持 Jira provider，计划支持 GitHub Issues、Linear 等。README 自称早期软件，会对 Jira 实例做写操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- extract/apply 工作流：backlog 导出为 XML 供 LLM 精炼，逐项 diff 审核后写入
- TUI 与 CLI 双形态，模糊搜索与 vim 模式键盘操作
- 令牌经 OS 钥匙串/环境变量/凭据文件三级链解析
- 多工作区可在多个 Jira 实例与项目间单键切换

## 适用场景

- 在终端中管理 Jira 看板、sprint 与 issue
- 把 backlog 交给 LLM 精炼并逐条审核变更
- 离线试用：ihj jira demo 无需连接 Jira

## 场景标签

 · 领域:开发者工具/项目管理

## 证据(README 行号)

> L8: - **LLM-assisted backlog refinement.** Extract your backlog as structured context, refine it with an LLM, and review
> L72: Extract your backlog as structured XML context with `ihj extract`, feed it to an LLM for refinement, and apply the 

## 星数曲线

```mermaid
xychart-beta
    title "mikecsmith/ihj 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-28 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6c63b8cff984` · [字段定义](../../DATASET.md)*
