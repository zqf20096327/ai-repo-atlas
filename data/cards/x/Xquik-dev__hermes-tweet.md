# Xquik-dev/hermes-tweet

⭐ 37 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Xquik-dev/hermes-tweet) · [官网](https://docs.xquik.com/guides/hermes-tweet) · 组织维护

**Hermes Agent 的 X/Twitter 搜索与操作插件**

面向 Hermes Agent 的插件，附带 Skill 与 2 个斜杠命令，通过 Xquik API 提供 102 个 OpenAPI 生成的端点访问（33 个预付费读取、7 条直连 MPP 路由）。读取与操作分离：tweet_read 调用目录端点，tweet_action 调用私有或变更类端点且默认关闭，需设置 HERMES_TWEET_ENABLE_ACTIONS=true。通过 hermes plugins 命令安装，唯一依赖 httpx 已由 Hermes 核心提供；需配置 XQUIK_API_KEY。声明与 X Corp 无关联。

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

- tweet_explore/tweet_read/tweet_action 三工具，读取与变更操作分离
- tweet_action 默认禁用，需环境变量显式启用，凭证不作参数传入
- 102 个 OpenAPI 生成端点（33 个预付费读取、7 条 MPP 路由）
- 附 /xstatus 与 /xtrends 两个斜杠命令

## 适用场景

- 在 Hermes Agent 中搜索和读取 X/Twitter 帖子与时间线
- 导出关注者/关注列表、监控指定账号
- 在代理流程中发帖或回复

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L6: Add Twitter API search, monitoring, and approved X actions to
> L14: The plugin bundles a Hermes Skill and 2 slash commands.

## 星数曲线

```mermaid
xychart-beta
    title "Xquik-dev/hermes-tweet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 35 --> 38
    line [37, 36, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf51b4d6ddc0` · [字段定义](../../DATASET.md)*
