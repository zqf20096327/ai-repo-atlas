# arconia-io/arconia

⭐ 198 · Java · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/arconia-io/arconia) · [官网](https://docs.arconia.io) · 组织维护

**给 Java 开发者的 Spring Boot 增强框架：开发服务/可观测/AI 文档处理**

面向用 Java 构建 Spring Boot 应用的企业开发者的附加框架：以 Maven Central 依赖形式加入现有 Spring Boot 应用，提供 Dev Services（用容器自动供给外部服务以简化本地开发与测试）、结合 OpenTelemetry 与 Micrometer 的日志/指标/链路统一观测、可插拔的 AI 可观测语义约定（OpenInference、OpenLLMetry、LangSmith 等）、基于 Docling 的 AI 文档处理（从 PDF/Office/HTML 抽取结构化内容）、多租户与扩展的数据访问支持。项目处于积极开发阶段，尚未发布首个稳定版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Dev Services 用容器自动供给外部服务，简化本地开发与测试
- 统一 OpenTelemetry 与 Micrometer 的日志、指标、链路观测
- 可插拔 AI 可观测语义约定，集成 Arize Phoenix、Grafana LGTM 等平台
- 基于 Docling 的文档处理，从 PDF/Office/HTML 抽取结构化内容供 AI 管道使用

## 适用场景

- 在现有 Spring Boot 应用中加入容器化开发服务以减少本地环境搭建
- 为 Spring Boot 应用统一接入 OpenTelemetry 与 Micrometer 观测
- 为 AI 管道观测接入多种语义约定与平台
- 构建多租户企业应用

## 场景标签

 · 领域:Java 企业应用框架/云原生

## 证据(README 行号)

> L5:  An add-on framework for Spring Boot, designed to enhance modern enterprise applications built with Java.
> L19: - **AI Observability.** Pluggable semantic conventions for AI observability, including OpenTelemetry, OpenInference

## 星数曲线

```mermaid
xychart-beta
    title "arconia-io/arconia 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 194 --> 199
    line [195, 197, 198]
```

2026-10-18 195 → 2026-10-22 198（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0c882d60c0c7` · [字段定义](../../DATASET.md)*
