# KrisTHL181/zhihu-cli

⭐ 29 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/KrisTHL181/zhihu-cli) · 个人维护 · 中文 README

**知乎非官方命令行客户端：终端内浏览、下载、发布与分析知乎内容**

用 Python 编写的知乎非官方 CLI 工具，认证一次后可在终端完成浏览热榜与回答、搜索、批量下载为带 YAML frontmatter 的 Markdown、用 Markdown 写作并发布回答/文章、投票关注私信等社交操作、多账户切换，以及创作者收入数据分析与词频/词云/K-means 等 NLP 分析。请求经 ZSE v4 签名与 curl_cffi TLS 模拟处理。提供可选的 MCP server 入口与 LLM 相关扩展依赖，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知乎内容批量下载为带 YAML frontmatter 的 Markdown
- Markdown 写作一键发布回答与文章，自动 HTML 转换
- 创作者收入数据可视化与词频/词云/K-means NLP 分析
- 提供 MCP server 入口（zhihu-mcp）与插件扩展机制

## 适用场景

- 把知乎文章和回答批量存为 Markdown 供笔记系统使用
- 在终端里完成知乎的浏览、搜索与互动而不开浏览器
- 管理多个知乎账号并在本地分析创作者收入数据

## 场景标签

`数据分析` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L15: **zhihu-cli** turns your terminal into a full-featured Zhihu client. Authenticate once, then browse, search, downlo
> L106: pip install -e ".[llm]"          # openai (zhihu agora ai, zhihu chat bot, crank)
> L108: pip install -e ".[mcp]"          # mcp (the zhihu-mcp server entry point)


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `022c47fbeab0` · [字段定义](../../DATASET.md)*
