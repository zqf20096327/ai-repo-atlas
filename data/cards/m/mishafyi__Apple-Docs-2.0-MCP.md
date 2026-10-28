# mishafyi/Apple-Docs-2.0-MCP

⭐ 26 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/mishafyi/Apple-Docs-2.0-MCP) · [官网](https://www.npmjs.com/package/apple-docs-2.0-mcp) · 个人维护

**给 AI 编程助手读 Apple 开发者文档的 MCP 服务器**

通过 Model Context Protocol 向 Claude、Cursor、VS Code、Zed 等 MCP 客户端提供 Apple 开发者文档访问：API 参考、文章、示例代码、Human Interface Guidelines、App Store Connect 帮助与 2014–2026 共 1,700 场 WWDC session（含 1,416 份字幕与 715 份代码示例，离线读取）。内置 336,723 页的离线索引（search_docs_map），文档页通过单一 HTTP 客户端抓取 developer.apple.com，带缓存、限速（100 次/分钟、搜索间隔 15 秒）与重试。为 kimsungwhee/Apple-Docs-MCP 的 fork。npm 分发，无需 API key。

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

- 336,723 页离线 docs map，可按名称查找 API、文章、Info.plist 键与 web-service 端点
- 1,700 场 WWDC session（2014–2026）离线可查：字幕、章节、带时间戳的代码示例
- 文档页渲染为 Markdown，含完整签名、继承关系、平台兼容版本与弃用替代
- 限速、重试、缓存机制，无需 API key 或账号

## 适用场景

- 让 Claude/Cursor 里的编程助手在写 iOS 代码前先查 Apple 官方文档
- 通过 API 名或错误信息直接定位对应文档页
- 查找 WWDC session 中介绍某 API 的讲解与示例代码
- 按主题（如机器学习）浏览全部 Apple 框架目录

## 场景标签

 · 领域:开发者工具/文档接入

## 证据(README 行号)

> L22: Apple Developer Documentation for AI assistants, through the Model Context Protocol: API reference, articles, sampl
> L24: Store Server API and others) and 1,700 WWDC sessions with their transcripts and code, in Claude, Cursor, VS Code or

## 星数曲线

```mermaid
xychart-beta
    title "mishafyi/Apple-Docs-2.0-MCP 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-24", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-19 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e53611cbc095` · [字段定义](../../DATASET.md)*
