# aliyun/alibabacloud-rds-openapi-mcp-server

⭐ 54 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/aliyun/alibabacloud-rds-openapi-mcp-server) · [官网](https://www.aliyun.com/product/rds) · 组织维护 · 中文 README

**阿里云 RDS 的 MCP 服务器：通过 OpenAPI 与 SQL 工具管理数据库实例**

阿里云官方维护的 MCP 服务器，将 RDS OpenAPI 封装为约 30 个 MCP 工具（创建实例、查性能、慢日志、白名单等），并提供只读 SQL 工具（自动创建临时只读账户执行后删除）。支持 toolsets 分组按需启用工具、SSE 传输与 API_KEY 鉴权，可接入 cherry-studio、Cline、Claude 等 MCP 客户端，另含 Skills 扩展（RDS Copilot 调用、CLI 管理脚本）。运行依赖 uv 与 Python 3.12 及阿里云凭据，建议仅绑定本地回环地址。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 30 个 OpenAPI 工具覆盖 RDS 实例创建/查询/监控/参数修改
- 只读 SQL 工具：自动创建临时只读账户执行后删除
- toolsets 分组按需启用工具（rds / rds_custom_read / rds_custom_all）
- 支持 SSE 传输与 API_KEY 鉴权，建议回环地址部署

## 适用场景

- 通过 MCP 客户端（cherry-studio/Cline/Claude）对话式管理阿里云 RDS 实例
- 查询实例性能、慢日志与 SQL 统计做数据库运维
- 对 RDS 实例执行只读 SQL 分析（EXPLAIN/SHOW 等）

## 场景标签

 · 领域:云数据库/LLM 基础设施

## 证据(README 行号)

> L3: # Alibaba Cloud RDS OpenAPI MCP Server
> L70: ## Components
> L71: ### OpenAPI Tools

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/alibabacloud-rds-openapi-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-29 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1a392cb41bf8` · [字段定义](../../DATASET.md)*
