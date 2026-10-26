# systempromptio/systemprompt-template

⭐ 29 · Rust · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/systempromptio/systemprompt-template) · [官网](https://systemprompt.io) · 组织维护

**自托管 AI 治理评估模板：网关认证、授权、限流与审计**

SystemPrompt 的本地评估模板，由 Core（Rust 编译运行时）加配置、管理 UI、扩展与可执行 demo 组成。它在 AI 客户端与模型/工具之间放置策略边界：按认证用户授予或拒绝模型访问、对受治理的 MCP 工具调用做范围/凭证模式/黑名单/限流检查，并把请求记录与工具追踪关联写入 PostgreSQL。供企业评估执行效果并作为自建部署起点；需 Docker、just、Rust 1.96+ 与 PostgreSQL 18，模板 MIT，Core 为 BSL-1.1（生产需商业许可）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Rust 编译运行时，自托管、可离线（air-gap）
- 按用户做模型访问控制、MCP 工具调用策略与限流
- 审计数据将身份、策略决定、工具活动与推理成本关联存入 PostgreSQL
- 通过编译/链接期注册的 Rust 扩展构建领域能力

## 适用场景

- 在企业内网自建 AI 网关，统一管控各客户端的模型与工具访问
- 评估策略拒绝、凭证泄露拦截等治理执行效果
- 保留带身份与成本关联的 AI 交互审计记录

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L15: SystemPrompt puts a policy boundary between your AI clients and the models and tools you connect. Permissions follo
> L25: This repository is the **evaluation template**: Core plus configuration, an admin UI, extensions and executable dem

## 星数曲线

```mermaid
xychart-beta
    title "systempromptio/systemprompt-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5ee5ba9b0ca0` · [字段定义](../../DATASET.md)*
