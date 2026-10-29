# opensearch-project/observability-stack

⭐ 43 · JavaScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/opensearch-project/observability-stack) · [官网](https://observability.opensearch.org/) · 组织维护

**面向微服务与 AI agent 的 OpenSearch 可观测性全家桶**

基于 OpenTelemetry、OpenSearch、Prometheus（Cortex 引擎）构建的开源可观测性集成栈：OTel Collector 接收 OTLP 数据，Data Prepper 转换后存入 OpenSearch，Prometheus/Cortex 存指标，Alertmanager 路由告警，Dashboards 提供统一 Web UI 与 PPL 查询。对 AI agent 遥测遵循 OpenTelemetry Gen-AI 语义约定，内置多 agent 示例服务，支持 eBPF 无侵入追踪。提供交互式安装脚本、Docker Compose、Helm 与 AWS 托管服务四条部署路径，安装约需 8-15 分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 遵循 OpenTelemetry Gen-AI 语义约定的 agent 遥测支持
- eBPF（OBI）无代码修改追踪 HTTP/gRPC/数据库调用
- 四条部署路径：install.sh、Docker Compose、Helm、AWS 托管服务（CLI/CDK）
- Cortex + Alertmanager + 统一 Alert Manager UI 的告警链路

## 适用场景

- 为微服务与 AI agent 应用统一收集日志、指标与链路
- 无侵入地为无 OTel SDK 的服务补齐追踪
- 部署到 Kubernetes 或 AWS 托管服务做可观测性基建

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: Observability Stack is an open-source stack designed for modern distributed systems. Built on OpenTelemetry, OpenSea
> L166: Observability Stack accepts telemetry data via the OpenTelemetry Protocol (OTLP) and follows the OpenTelemetry Gen

## 星数曲线

```mermaid
xychart-beta
    title "opensearch-project/observability-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `731c64781ea6` · [字段定义](../../DATASET.md)*
