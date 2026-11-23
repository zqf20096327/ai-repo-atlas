# whaaaley/opencode-search

⭐ 20 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/whaaaley/opencode-search) · [官网](https://www.npmjs.com/package/opencode-search) · 个人维护

**OpenCode 插件：给 agent 提供免 key 的十路搜索工具**

为 OpenCode agent 提供十个无需 API key 和账号的搜索工具：Firecrawl 无 key 通用网页搜索（按 IP 每日限额）、Google News RSS、Wikipedia、MDN、AWS 文档、Bluesky 与 standard.site（经 AT Protocol）、IETF RFC、W3C 与 WHATWG 规范索引。通过 opencode.json 声明插件名后重启即自动安装；0.0.9 为 OpenCode 1 的最后一个版本，新功能集中在要求 OpenCode 2 的 1.x。Firecrawl 超限时报错而非返回空结果。

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

- 十个搜索工具均无需 API key 或账号
- 经 AT Protocol 检索 Bluesky 帖子与 AT Protocol 平台长文
- 覆盖 MDN、AWS 文档、IETF RFC、W3C 与 WHATWG 规范等开发者资料源
- 支持 OpenCode 1 与 OpenCode 2 两种插件配置方式

## 适用场景

- 让编码 agent 直接检索网页、新闻和维基百科资料
- 查询 Web 标准与规范文档（RFC/W3C/WHATWG）
- 搜索 Bluesky 上关于某话题的帖子

## 场景标签

 · 领域:LLM 基础设施/agent 工具

## 证据(README 行号)

> L3: An OpenCode plugin that gives your agent access to Firecrawl web search, Google News, Wikipedia, Bluesky, standard.s
> L9: Ten search tools that work without an API key or an account. OpenCode 1 has no web search at all unless you use its 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `c1fb89834d25` · [字段定义](../../DATASET.md)*
