# em4nu3i69dll/service-status-api

⭐ 33 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/em4nu3i69dll/service-status-api) · 个人维护

**加密服务状态监控 API：Go 代理探测，Ollama 本地生成报告**

由 TypeScript API、Go 探测代理、Python 分析器与 Cloudflare Tunnel 组成的服务可用性监控方案：代理检查目标 URL 的可用性与延迟，经加密消息（AES-256-GCM/HKDF/HMAC）经隧道上报，API 持久化状态并通过 mTLS 客户端证书提供私有的状态/历史查询。分析器将有效读数交给本地 Ollama（默认 Qwen 3.5 0.8B）生成含摘要与观察的 JSON 报告，无效读数不送模型。支持 Docker Compose/Portainer 部署，限制内存与网络，状态文件仅支持单 API 实例，非分布式存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Go 代理探测 URL 可用性与延迟，加密消息经 Cloudflare Tunnel 上报
- 读取侧通过 mTLS 客户端证书（monitor/ia）鉴权
- Ollama 本地分析生成含摘要与观察的 JSON 报告，无有效读数时不调用模型
- Docker Compose/Portainer 部署，容器只读文件系统并限制 CPU/内存

## 适用场景

- 监控自有服务的在线状态与延迟并保留历史
- 不开放主机端口、经隧道远程上报探测数据
- 用本地模型对服务读数生成周期性分析报告

## 场景标签

 · 领域:运维监控/可观测性

## 证据(README 行号)

> L3: API de estado con telemetría cifrada, Cloudflare Tunnel, lectura privada por mTLS y análisis con IA local.
> L11: |Análisis|Python · Ollama · Qwen 3.5|Generar informes a partir de las lecturas|
> L129: El analizador consulta la API con su certificado, envía únicamente lecturas vigentes a Ollama y valida una respues

## 星数曲线

```mermaid
xychart-beta
    title "em4nu3i69dll/service-status-api 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-29 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `452618962d9e` · [字段定义](../../DATASET.md)*
