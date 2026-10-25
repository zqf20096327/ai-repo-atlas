# laxmariappan/abilities-scout

⭐ 45 · PHP · 推送 2026-08-04 · [GitHub](https://github.com/laxmariappan/abilities-scout) · 个人维护

**扫描 WordPress 插件静态代码，发现可注册为 AI abilities 的候选**

WordPress 插件（WP 6.0+/PHP 8.0+），用 PHP tokenization 静态分析已安装插件源码（不执行代码），抽取 hooks、REST 路由与 shortcodes，按积分引擎评分排序，输出建议名称、置信度、类型分类与源码位置；hooks/shortcodes 记为 primitive abilities，REST 路由归为 orchestrators。提供 MCP 两种能力（scan/draft）供连接站点的 AI agent 调用，并支持 Markdown/JSON 导出供 Claude、Cursor 等离线编码工具使用。只读、仅管理员、无外部调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PHP tokenization 静态分析，不执行插件代码
- 积分引擎区分 primitive abilities 与 REST orchestrators 并输出置信度
- 注册 MCP 能力 lax-abilities-scout/scan 与 /draft 供 agent 直接调用
- Markdown/JSON（schema v1.2）导出供离线 AI 编码工具消费

## 适用场景

- 为 Abilities API 改造现有插件时找到可注册的候选 abilities
- 通过 MCP 连接的 agent 直接扫描站点插件并生成实现
- 把扫描结果导出到 Claude/Cursor 让 AI 生成 abilities 代码

## 场景标签

 · 领域:WordPress 开发工具

## 证据(README 行号)

> L30: If your AI agent is connected to your WordPress site via the Model Context Protocol, Lax Abilities Scout registers 
> L49: When you're working in Claude.ai, Cursor, or any AI coding tool that isn't connected to your live site, use the exp

## 星数曲线

```mermaid
xychart-beta
    title "laxmariappan/abilities-scout 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1c89dfddf821` · [字段定义](../../DATASET.md)*
