# olyannaa/clickadvisor

⭐ 18 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/olyannaa/clickadvisor) · [官网](https://clickadvisor.lovable.app) · 个人维护 · 中文 README

**ClickHouse SQL 性能分析与规则引擎 CLI，含 MCP 服务器**

面向 DBA、数据工程师与平台团队的本地优先 ClickHouse 性能顾问：内置 119 条 ClickHouse 专用规则引擎，每条命中给出 rule_id、severity、confidence 与安全 rewrite 示例；支持单条 SQL 分析、system.query_log workload 分析（CSV/只读 live）、EXPLAIN ESTIMATE 对比，以及 stdio/Streamable HTTP MCP 服务器供 Claude 类客户端调用。AI 仅作为接口与探索工作流，production 推荐来自确定性规则引擎；默认不执行用户 SQL、不外发数据。提供 Python/poetry 源码安装与 Docker 镜像，附带 DS/ML 实验数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 119 条 ClickHouse 专用规则，命中含 rule_id/severity/confidence/rewrite 示例
- workload 分析：query_log 指纹归组、延迟与内存统计、top-N 风险报告
- 本地 stdio MCP 与远程 Streamable HTTP MCP 服务器（analyze_query 等 4 个工具）
- 默认不执行用户 SQL、不做隐藏远程 LLM 调用，可完全本地运行

## 适用场景

- 上线前检查 ClickHouse SQL 中的高风险模式
- 基于 query_log 做 workload 审查排队与风险优先级排序
- 通过 MCP 让 Claude 类 AI 客户端调用 SQL 分析能力
- 在 CI/CD 中以 JSON 输出集成自动化检查

## 场景标签

 · 领域:数据库/性能工程

## 证据(README 行号)

> L20: Это не generic SQL chatbot. Trusted runtime построен вокруг deterministic
> L23: используется как интерфейс через MCP и как исследовательский workflow, но не как

## 星数曲线

```mermaid
xychart-beta
    title "olyannaa/clickadvisor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9a37af624056` · [字段定义](../../DATASET.md)*
