# Northwood-Systems/millwright

⭐ 46 · Rust · Apache-2.0 · 推送 2026-08-10 · [GitHub](https://github.com/Northwood-Systems/millwright) · [官网](https://northwoodsystems.ai/research/projects/millwright/docs) · 组织维护

**自托管的 LLM 路由器：单 Rust 二进制实现成本与缓存亲和路由**

部署在 AI 应用与模型供应商之间的开源路由器，接收 OpenAI Chat Completions 与 Anthropic Messages 请求，转发至 OpenAI 兼容 API、原生 Anthropic 或 Amazon Bedrock。用户将模型分配到 cheap/mid/frontier 角色，路由器按策略选择最低预估成本的健康路由，并按会话 ID 保持 provider/model 亲和以复用 prompt 缓存。提供 SQLite/PostgreSQL 账本记录花费与路由证据、CLI 与管理 API、成本分析报告，以单一 Rust 二进制及 Docker Compose 形式交付。声明自身不做 agent 编排、不检查提示词内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cheap/mid/frontier 角色路由，选择最低预估成本健康路由
- 会话级 provider/model 亲和保持 prompt 缓存复用，各角色独立并发车道
- 花费账本（SQLite/PostgreSQL）与 CLI/管理 API 查询
- millwright analyze 生成 HTML/Markdown/JSON 成本分析报告

## 适用场景

- 在多个模型供应商之间切换而不修改应用代码
- 控制各团队和任务的模型花费
- 保持会话缓存亲和以降低 token 成本
- 自托管 LLM 网关并保留供应商凭据在自有基础设施内

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: Millwright is an open-source, self hosted LLM router that runs between your AI applications and the model providers
> L17: You define which models belong in the `cheap`, `mid`, and `frontier` roles. Millwright selects the lowest estimated

## 星数曲线

```mermaid
xychart-beta
    title "Northwood-Systems/millwright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-29 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `23d10928eedc` · [字段定义](../../DATASET.md)*
