# tt-a1i/archify

⭐ 85,301 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/tt-a1i/archify) · [官网](https://archify.si) · 个人维护 · 中文 README

**面向 coding agent 的交互式架构图生成 skill**

Archify 是一个可安装到 AI 编码代理的 skill：用户用自然语言描述想法、计划或让代理读取仓库，生成可交互的独立 HTML 图（架构、时序、数据流、ERD 等 10 种类型），支持主题切换、路径追踪、PNG/分享卡导出。输出为单文件 HTML，查看者无需安装 Archify。通过 npx skills 安装，支持 Claude Code、Codex CLI、Cursor、OpenCode，社区另有 DSH 插件接入；更新检查为可关闭的可选网络请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 22,84 位贡献者
- 涨星:近 1 天 **+571**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800

## 能力要点

- 支持 10 种图类型（架构、工作流、时序、数据流、ERD 等）
- 输出自包含 HTML，查看无需安装本工具
- 支持读取仓库生成带来源依据的架构图
- 通过 npx skills 一条命令安装，支持 4 种 agent

## 适用场景

- 让 agent 读取仓库生成带来源链接的架构图
- 把旅行计划或学习地图做成可交互 HTML 页面
- 在对话中迭代调整图表（加节点、高亮路径）

## 场景标签

 · 领域:开发者工具/图表生成

## 证据(README 行号)

> L9:  Start with an idea, a question, or a plan. Describe it to your AI agent, and Archify turns it into an interactive H
> L26:  Works with Claude Code, Codex, Cursor, and OpenCode
> L48: npx skills add tt-a1i/archify -g

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `a4bb8c2672f0` · [字段定义](../../DATASET.md)*
