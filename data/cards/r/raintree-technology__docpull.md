# raintree-technology/docpull

⭐ 29 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/raintree-technology/docpull) · [官网](https://raintree.technology/portfolio#docpull) · 组织维护

**本地优先的 CLI/MCP 服务器：为 AI 代理生成带引用的版本化上下文**

DocPull 是 Python 3.11+ 的命令行工具与 MCP 服务器，将公开网页与本地文档获取、索引为带引用、可复现、可 diff 的代理上下文：来源声明存于 docpull.yaml，解析结果锁定在 context.lock.json，后续同步产生基于哈希的差异。提供 CLI、Python/TypeScript SDK、MCP 服务器与代理插件四种接口。获取、索引、校验、导出默认本地运行，无需账号或付费 API；浏览器/云渲染需显式选择且可被零预算阻止。默认路径不处理 CAPTCHA 与复杂浏览器交互，安全默认含 HTTPS-only、robots.txt 遵循与 SSRF 防护。

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

- 来源→获取→版本化证据→diff→导出的本地流水线，产出锁定文件与稳定哈希
- CLI / Python SDK / TypeScript SDK / MCP 服务器 / 代理插件多种接口
- context-pack v3 契约分级校验与 context-ci 门禁（新鲜度、引用覆盖、质量）
- 无账号或付费 API 即可运行，凭据不持久化于项目工件

## 适用场景

- 为 RAG 或代理应用构建可复现、带引用的文档上下文
- 跟踪文档、产品页、政策等来源变更并检测漂移
- 在 CI 中对上下文包做引用覆盖与质量门禁校验

## 场景标签

`网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L7: DocPull turns changing public web sources into cited, reproducible context for AI
> L76: |MCP server|Give local agent clients source tools|MCP server|

## 星数曲线

```mermaid
xychart-beta
    title "raintree-technology/docpull 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-30 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bfa6670752ba` · [字段定义](../../DATASET.md)*
