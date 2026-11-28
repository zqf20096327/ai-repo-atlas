# xavidop/hikyaku

⭐ 3 · Go · MIT · 推送 2026-11-24 · [GitHub](https://github.com/xavidop/hikyaku) · [官网](https://xavidop.github.io/hikyaku/) · 个人维护

**面向消息中继场景的 CLI：多端点读写、AI 路由、消息不丢失**

Go 编写的消息中继工具：从 webhook、WebSocket、Kafka、SQS 等端点读取消息，投递到一个或多个目标端点，整条链路由单个 YAML 文件描述。每一步具备超时、退避重试、熔断、回退链与死信队列（可重放），消息按 key 保序，磁盘缓冲可抗 kill -9。AI 路由由决策模型对每个候选目标回答是/否问题并给出校准概率，模型不确定时由规则与静态路由接管；另提供 OpenAI 兼容的 LLM 代理端点按规则或模型切换供应商。提供 brew/scoop/docker/helm/go install 安装，附 admin API、Prometheus 指标与 OpenTelemetry 追踪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 YAML 定义 sources/destinations/routes/transforms 与重试策略，带 JSON Schema 与 validate 命令
- AI 路由输出校准置信概率，规则与静态路由在模型不确定时接管
- 支持 HTTP/WS/SSE/gRPC/Kafka/NATS/MQTT/RabbitMQ/Redis/SQS 等约 18 类协议作为源或目标
- 死信队列可重放，磁盘缓冲抗 kill -9，热重载与 Prometheus/OpenTelemetry 可观测

## 适用场景

- 把 webhook 事件扇出到计费、工单等多个下游并保证不丢
- webhook 到 Kafka 的桥接、WebSocket 订阅转 HTTP 投递
- 用 LLM 对入站消息做分诊路由并保留置信记录
- 搭建 OpenAI 兼容代理在多个模型供应商间故障切换

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: hikyaku is a message relay written in Go. It reads messages from one or more endpoints (a webhook, a WebSocket, a K
> L29: - **AI routing with real confidence.** A decision model answers one yes/no question per candidate destination and g
> L32: - **An LLM proxy.** An OpenAI-compatible endpoint routes chat requests to a model by rules or by a decision model, 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `2d8208dbc9e7` · [字段定义](../../DATASET.md)*
