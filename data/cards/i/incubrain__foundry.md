# incubrain/foundry

⭐ 79 · TypeScript · 推送 2026-10-24 · [GitHub](https://github.com/incubrain/foundry) · [官网](https://foundry.incubrain.org) · 组织维护

**面向 AI-native 业务的 Nuxt 4 营销站模板，带信号采集与 agent 就绪层**

作为 Nuxt layer 发布的网站模板：写 YAML/markdown 内容即可部署营销站，站点在服务端把访问事件、意图转化（Convert 组件）与错误日志统一写入环形缓冲的 SignalRow，通过带 Bearer 鉴权的游标端点 /api/_signals/export 输出给外部消费者（如 Polaris 或 Grafana 类拉取器），本身不含图表与仪表盘。第二支柱是 agent 就绪：内置 MCP 工具（list-pages/get-page/what-changed）、llms.txt、markdown 重定向，并在服务端将每行信号分类为 human/agent/bot。隐私上无 Cookie、无存储 ID，访客按日轮换盐值哈希计数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件+日志统一为 SignalRow，游标式鉴权导出端点供外部消费
- 内置 MCP 工具、llms.txt、raw-markdown 重定向与 SEO/OG 栈
- 服务端将流量分类为 human/agent/bot
- 无 Cookie、无存储 ID 的访客哈希计数（盐值每日轮换）

## 适用场景

- 快速搭建输出行为信号流的营销/落地页站点
- 让 agent 与爬虫以 MCP/llms.txt/markdown 方式读取站点内容
- 以外部消费者拉取信号流做自有分析

## 场景标签

 · 领域:Web 开发/站点模板

## 证据(README 行号)

> L13: The second pillar is **agent-readiness**. Agentic traffic is expected to dwarf human
> L14: traffic, so Foundry sites ship MCP tools, `llms.txt`, raw-markdown redirects, and a strong
> L102: |MCP tools|`list-pages`, `get-page`, `what-changed` — auto-registered from `server/mcp/tools/`, served by `@nuxtjs

## 星数曲线

```mermaid
xychart-beta
    title "incubrain/foundry 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `106765de0dd1` · [字段定义](../../DATASET.md)*
