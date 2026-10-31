# BelyaevAD/beget-hosting-mcp

⭐ 15 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/BelyaevAD/beget-hosting-mcp) · [官网](https://belyaevad.github.io/beget-hosting-mcp/) · 个人维护 · 中文 README

**Beget 主机托管 API 的 MCP 服务器：让 Agent 管理域名、DNS、站点等**

封装 Beget 官方 API 的 MCP 服务器，通过 stdio 向 MCP 客户端和自动化 Agent 暴露 4 个工具：列出文档化方法、查询单个方法文档、调用任意 Beget API 方法、获取账户信息，覆盖域名、DNS、站点、FTP、MySQL、邮件、Cron、备份与统计。项目处于 Alpha 阶段：默认只读，写操作需 BEGET_ALLOW_WRITE 环境变量加每次 confirm_write 双重确认。API 文档语料保存于 docs/ 并生成机器可读方法元数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 默认只读模式，写操作需 BEGET_ALLOW_WRITE=true 且每次调用 confirm_write=true
- 凭据仅从环境变量加载，dry-run 与错误信息中隐藏机密
- 保存 Beget API 文档语料并生成机器可读的方法元数据（docs/schema/methods.json）
- 无第三方 Python 依赖，stdio 每行一条紧凑 JSON-RPC 消息

## 适用场景

- 在 Cursor 等 MCP 客户端中通过对话管理 Beget 主机账号的域名和 DNS
- 让自动化 Agent 执行站点、MySQL、Cron、备份等运维操作
- 通过 beget_call 工具调用任意文档化的 Beget API 方法

## 场景标签

 · 领域:主机托管运维/MCP 工具

## 证据(README 行号)

> L10: MCP-сервер для официального API хостинга Beget. Он предоставляет MCP-совместимым клиентам и агентам автоматизации о
> L12: Проект предоставляет MCP-клиентам и агентам контролируемый интерфейс инструментов для управления хостингом Beget: с

## 星数曲线

```mermaid
xychart-beta
    title "BelyaevAD/beget-hosting-mcp 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-26 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ab5cdf9ec9e7` · [字段定义](../../DATASET.md)*
