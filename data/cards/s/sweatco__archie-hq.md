# sweatco/archie-hq

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/sweatco/archie-hq) · 组织维护

**接入 Slack 的 AI 员工：委派任务由 Claude Agent 驱动的代理完成**

基于 Claude Agent SDK 的多代理工作系统：用户在 Slack、CLI 或 GitHub webhook 中发起任务，一个长驻 PM 代理按领域加载插件技能，把繁重工作委派给其派生的 worker 代理，并汇总回复。通过插件目录扩展领域能力，无需改核心代码。任务运行于 OS 级沙箱（bubblewrap/sandbox-exec），文件系统、网络出口与代码变更均受白名单和人工审批门控。无数据库与消息中间件，状态存于磁盘文件与 git，单机可服务约百人团队的并行任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PM 代理加载插件技能并派生 worker 的单代理委派架构
- 插件目录扩展技能/代理/钩子，无需改核心代码
- bubblewrap/sandbox-exec 沙箱 + 人工审批门控（编辑模式、MCP 工具逐次审批、PR 合并审批）
- 无数据库/消息中间件，文件与 git 存储状态，任务可检查点恢复

## 适用场景

- 在 Slack 中把工程、营销、分析等工作委派给 AI 代理执行
- 通过插件目录接入自己团队的领域技能与工具
- 让代理在受控沙箱中调查代码并自动开 PR、人工审批后合并

## 场景标签

`Agent 框架` `多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Archie is an AI employee** — you delegate real work to it in Slack, the same way you would to a colleague, and it
> L12: Under the hood a task is one long-lived agent — the PM — that loads the skill for the domain, hands bulky or specia
> L169: - **AI:** Claude Agent SDK

## 星数曲线

```mermaid
xychart-beta
    title "sweatco/archie-hq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5edef7ca1261` · [字段定义](../../DATASET.md)*
