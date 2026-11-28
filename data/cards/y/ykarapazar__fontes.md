# ykarapazar/fontes

⭐ 24 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/ykarapazar/fontes) · [官网](https://ykarapazar.github.io/fontes/) · 个人维护

**法律检索 MCP 服务器：让 AI 应用实时查法院判例与立法**

开源的 Model Context Protocol 服务器，提供九个固定的法律研究工具（外加 report_bug），使接入的 AI 应用能在 125 个司法辖区的法院与政府官网实时检索判例和立法文本，每条结果附原文链接；另可通过 Lexifina 的托管服务器查询历史版本法条及另外 91 个国家的立法。不建数据库、不缓存，Beta 阶段源站变动可能导致检索失败。支持 Claude Desktop、Cursor、VS Code 等 MCP 客户端，提供 .mcpb 一键安装与 uvx 运行方式，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 九个固定研究工具，司法辖区为参数，覆盖 125 个辖区及国际法院
- 每个结果带原文 URL 或官方标识，可核对原始来源
- 通过 Lexifina 的 git 历史记录查询法条的历史生效版本
- 每日检查源站健康状态并提供状态页

## 适用场景

- 让 Claude 或 Cursor 用自然语言检索特定国家的最高法院判决
- 查询某法条在过去某日期的生效文本及修订历史
- 为律师或研究者出具带官方来源链接的法律检索结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Fontes is a free, open-source MCP server. It lets your AI app **look up court decisions and
> L9: publisher). It is a standard Model Context Protocol (MCP) server, so it works in any app that
> L15: - **For developers:** one MCP server with nine fixed research tools (plus `report_bug`); the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `883b23250eeb` · [字段定义](../../DATASET.md)*
