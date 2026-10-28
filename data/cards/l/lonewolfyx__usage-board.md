# lonewolfyx/usage-board

⭐ 37 · Vue · MIT · 推送 2026-10-10 · [GitHub](https://github.com/lonewolfyx/usage-board) · 个人维护

**分析本地 JSON 文件的 AI 编程 token 用量仪表盘**

基于 Nuxt 构建的可视化仪表盘，读取本地 JSON 文件中的 AI 编程工具（Claude Code、Codex、Gemini 等）用量记录，展示 token 消耗、成本、会话数等核心指标，并提供按日/月/项目/会话的多维统计、token 热力图、缓存命中率与 token 效率指标。通过 npx 一行命令启动，按终端提示打开本地页面查看。适合个人或团队分析 AI 编程开销。

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

- 读取本地 JSON 文件展示 token 用量、成本与会话数
- 按日/月/项目/会话的多维统计与 token 热力图
- 缓存命中与 token 效率指标
- npx 一行命令启动，本地页面查看

## 适用场景

- 查看我在 Claude Code / Codex 等 AI 编程工具上的 token 与成本开销
- 按项目或会话分析用量分布，定位高消耗日期
- 团队或个人扩展为 AI 用量分析工具

## 场景标签

`LLM 可观测性` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: An all-in-one dashboard to quickly analyze token usage from local json files
> L18: - Overview of core metrics: AI Coding token usage, costs, session counts

## 星数曲线

```mermaid
xychart-beta
    title "lonewolfyx/usage-board 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7547a9d1d41c` · [字段定义](../../DATASET.md)*
