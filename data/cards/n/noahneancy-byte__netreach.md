# noahneancy-byte/netreach

⭐ 35 · Python · MIT · 推送 2026-08-18 · [GitHub](https://github.com/noahneancy-byte/netreach) · 个人维护 · 中文 README

**给 AI Agent 的免登录网络访问能力层，覆盖 7 个平台**

面向 AI Agent 的只读网络访问能力层：收录无需登录、爬虫风险低的公开数据源，覆盖网页、YouTube、RSS、GitHub、V2EX、B站与全网语义搜索 7 个平台。定位为能力层而非工具，负责选型、安装、体检与路由，实际读取由 Agent 直接调用上游工具（yt-dlp、gh、feedparser、Jina Reader 等）完成。每个平台为有序后端列表，doctor 命令真实探测可用后端并给出修复处方。限制：B站字幕需浏览器登录态，不在范围内。提供 CLI 安装与 SKILL.md 供 Agent 读取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个零配置、无需登录的公开数据源平台接入
- 能力层设计：负责选型/安装/体检/路由，读取由上游工具直接完成
- 每平台为有序后端列表，doctor 命令真实探测并报告当前后端
- 默认安全模式只检查不安装，支持 dry-run 预览与代理配置

## 适用场景

- 让 AI Agent 具备读网页、搜视频、查 GitHub 等只读网络能力
- 不想配置各平台账号凭据时给 Agent 接入公开数据源
- 用 doctor 体检并切换各平台的后端接入方式

## 场景标签

`网页抓取` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L3: > 给你的 AI Agent 一键装上互联网「只读 + 搜索」能力 —— 只收录**无需登录、爬虫风险低**的公开数据源。
> L21: **NetReach 是一个能力层（capability layer），不是又一个工具。**
> L23: 它负责**选型、安装、体检、路由**，不负责底层读取本身。读取由 Agent 直接调用上游工具（yt-dlp、gh、feedparser、bili-cli 等）完成，没有包装层。

## 星数曲线

```mermaid
xychart-beta
    title "noahneancy-byte/netreach 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4dcd6f3bc359` · [字段定义](../../DATASET.md)*
