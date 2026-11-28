# Samxel/geizhals-mcp

⭐ 10 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Samxel/geizhals-mcp) · 个人维护

**让 AI 查询 Geizhals 价格数据的 MCP 服务器**

封装 Geizhals 移动端 API 的 MCP 服务器，向 AI 客户端提供搜索商品、全店铺最低价、价格历史、评分、促销降价、二手广告匹配与邮件降价提醒等工具；输出紧凑 JSON 并附带商品与商家链接。支持 stdio 与 streamable HTTP 两种运行方式，无需后台常驻进程。依赖 Python 3.10+，可用 uvx 直接从 GitHub 运行或克隆后 pip 安装。项目自述为非官方独立项目，所用接口可能随时变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个 MCP 工具：搜索、商品详情、价格历史、评分、类目浏览、比价、降价清单、型号价格区间、二手匹配
- 内置 2200+ 类目的完整 Geizhals 类目树（categories.json）
- 通过 Geizhals API 无账号创建邮件降价提醒
- 支持 stdio 与 HTTP 两种传输，兼容 Claude/Cursor/VS Code 等 JSON 配置客户端

## 适用场景

- 在对话中询问某商品当前最低价与各店铺库存
- 让 AI 分析价格历史并判断现在是买还是等
- 查询当前降价促销并按折扣幅度/类目筛选
- 评估二手广告对应商品的新品价格区间

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: An MCP server that lets an AI search Geizhals price
> L62: ## Add it to Claude (and other MCP clients)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cf43e79d6f41` · [字段定义](../../DATASET.md)*
