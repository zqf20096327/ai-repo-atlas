# hoangsonww/Post-Analyzer-Webserver

⭐ 14 · Go · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/Post-Analyzer-Webserver) · [官网](https://hoangsonww.github.io/Post-Analyzer-Webserver/) · 个人维护

**Go 微服务后端：存储并分析帖子的 CRUD 与情感分类**

基于 CloudWeGo 技术栈（Kitex/Thrift RPC、Hertz HTTP、Sonic、Netpoll）的微服务后端，提供帖子的存储、检索与两类分析：逐字符频率统计与经 Nvidia Triton（CPU）部署的 TF-IDF + LogisticRegression ONNX 情感分类模型。包含 JWT+ABAC（默认拒绝）鉴权、Kafka/RabbitMQ/RocketMQ 三种消息代理各司其职、MinIO 对象存储、Prometheus+Grafana 可观测性，并提供 Kubernetes（含 Istio、Argo Rollouts）与 Terraform（AWS/Azure/OCI/GCP）部署产物。运行完整栈仅需 Docker + Docker Compose，首启拉取约 13GB 的 Triton 镜像。同一网关二进制支持 HTTP、RPC、CLI、REPL 与内置 Web UI 五种交互面。

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

- 6 个可独立部署的微服务，17 容器 Docker Compose 全栈
- Kafka 事件日志 / RabbitMQ 工作队列 / RocketMQ 延迟消息三种代理分工
- Nvidia Triton 部署 TF-IDF + LogisticRegression ONNX 情感分类器
- JWT + 自研 ABAC 策略决策点（默认拒绝），三种演示角色

## 适用场景

- 搭建带情感分析的内容管理后端
- 学习 Go 微服务、多消息代理与 K8s/Terraform 部署的参考工程
- 通过 CLI/REPL/Web UI 对帖子做 CRUD 与分析

## 场景标签

 · 领域:后端/微服务基础设施

## 证据(README 行号)

> L5: An enterprise-grade, microservices-based backend for storing, serving, and analyzing "posts" (title/body records wit
> L54: |ML|Nvidia Triton Inference Server (CPU), serving a trained TF-IDF + LogisticRegression ONNX sentiment classifier|
> L7: It's fundamentally about **post analysis** — every piece of infrastructure here (Kafka event stream, RabbitMQ reanal

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/Post-Analyzer-Webserver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e72f5cebc185` · [字段定义](../../DATASET.md)*
