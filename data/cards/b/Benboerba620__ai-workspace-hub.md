# Benboerba620/ai-workspace-hub

⭐ 82 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/Benboerba620/ai-workspace-hub) · [官网](https://mp.weixin.qq.com/s?__biz=MzcwNTA3NjkzNQ==&mid=2247484256&idx=1&sn=8b7af107a56947b1d14b944445f19d38) · 个人维护 · 中文 README

**把 AI 编程助手变成带长期记忆的投资研究工作台（文件协议）**

一套基于 Markdown 文件协议的工作区：让 Codex / Claude Code / Cursor 等能读写文件的 AI agent 进入目录后按 AGENTS.md 路由执行研究工作流。六大能力：wiki 摄入、公司/行业研究、股票筛选、daily-watch 日报、假设建档追踪、播客转 wiki。知识按 source→exploration→pattern→rule 逐级提炼，配 Research Preflight 按需加载。Core Mode 无需 API key，Enhanced Mode 可选接入 Nasdaq/Tushare/FMP 等数据源。声明不做自动交易、不构成投资建议。

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

- Markdown 文件协议驱动，任何能读写文件的 AI agent 均可接入
- Core Mode 零 API key 可运行（wiki 摄入、研究草稿、筛选、假设建档）
- 知识分级提炼（source/exploration/pattern/rule）与假设复盘闭环
- 支持 Obsidian 集成（9 个动态视图，默认不装）

## 适用场景

- 投资研究员建立带长期记忆的公司/行业研究流程
- 个人投资者用 AI agent 做股票筛选、盯盘日报与假设跟踪
- 用 Obsidian 管理 AI 摄入整理的资料库

## 场景标签

`Agent 记忆` `金融量化` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L137: > 系统不在某个模型里，而在这套文件协议里。谁读懂这套协议，谁就接上你的工作流。
> L127: wiki 变大后也不会每次全量加载。每次研究先运行 Research Preflight：按 `rule -> pattern -> exploration` 加载相关可复用知识，同时扫描 `entities / concept
> L143: |**Core**|不需要|wiki 摄入（无脚本自动标签）、研究草稿、快速筛选、假设建档、断点续传|临时未配置 API 时|

## 星数曲线

```mermaid
xychart-beta
    title "Benboerba620/ai-workspace-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-24 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e3bca8ef7f6e` · [字段定义](../../DATASET.md)*
