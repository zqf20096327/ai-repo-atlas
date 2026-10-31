# xxddpac/netra

⭐ 99 · Go · GPL-3.0 · 推送 2026-09-18 · [GitHub](https://github.com/xxddpac/netra) · 个人维护 · 中文 README

**单二进制 eBPF 网络流量观测平台，带 AI 助手**

面向 SPAN/镜像端口的内核态流量观测平台：以 XDP/eBPF 在网卡接收路径完成抓包、解析与聚合，用户态仅读取聚合结果；单二进制内嵌 SQLite 与 DuckDB，流量历史封存为小时级 Parquet 文件。提供实时仪表盘、流浏览器、威胁告警（端口扫描/DDoS/IOC）、Kafka 导出、GeoIP/DPI 被动富化。AI 为可选功能：通过 OpenAI 协议兼容模型问答观测数据，并可经 MCP 扩展外部工具。要求 x86_64、Linux 内核 4.18+、glibc>=2.28，需 root 或相应 capabilities 挂载 XDP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- XDP 原生抓包与内核态聚合，单二进制零外部依赖（内嵌 SQLite/DuckDB）
- 威胁告警（扫描/DDoS/IOC/弱口令）并可推送 WeCom/DingTalk/Feishu
- OpenAI 协议兼容的 AI 助手问答观测数据，支持 MCP 扩展
- Kafka 异步导出五元组记录供下游消费

## 适用场景

- 旁路分析镜像端口的网络流量并做威胁检测
- 通过自然语言向 AI 助手查询观测到的流量情况
- 将五元组流量记录导出到 Kafka/Grafana 做下游分析

## 场景标签

 · 领域:网络监控/可观测性

## 证据(README 行号)

> L14: Netra is a kernel-native traffic observability platform for SPAN and mirror ports. It reads an out-of-band copy of 
> L21: - **AI grounded in real traffic** — use natural language to query data observed by Netra, then extend the assistant
> L91: - **AI assistant** — ask questions about Netra's observed traffic through an OpenAI-protocol-compatible model.

## 星数曲线

```mermaid
xychart-beta
    title "xxddpac/netra 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 97 --> 100
    line [98, 99, 99]
```

2026-10-18 98 → 2026-10-31 99（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `0c261256f162` · [字段定义](../../DATASET.md)*
