# secretflow/kuscia

⭐ 146 · Go · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/secretflow/kuscia) · [官网](https://www.secretflow.org.cn/docs/kuscia/latest/zh-Hans) · 组织维护 · 中文 README

**K8s 隐私计算任务编排框架，统一多方安全计算基础设施**

基于 K3s 的轻量级隐私计算任务编排框架：抽象异构基础设施与协议，提供统一的 HTTP/gRPC API 接入隐私计算能力，支持跨域网络安全通信（单公网端口复用、多任务并发安全通信），可与业内多种隐私计算系统互联互通。可在 1 CPU / 2 GB RAM 资源下完成百万级记录的 PSI（隐私集合求交）。面向需要跨机构部署隐私计算任务的开发者与企业。文档目前仅提供中文版，且官方声明非 release 版本仅用于演示，不应在生产环境使用。

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

- 基于 K3s 的轻量级部署，1 CPU / 2 GB RAM 可运行百万级记录 PSI
- 跨域网络安全通信：单公网端口复用，多任务并发安全通信
- 统一 HTTP/gRPC API 接入隐私计算能力
- 可与业内多种隐私计算系统互联互通

## 适用场景

- 跨机构部署和编排隐私计算任务
- 在异构基础设施上运行 PSI 等多方安全计算
- 通过统一 API 将隐私计算能力集成到业务系统

## 场景标签

 · 领域:隐私计算/基础设施

## 证据(README 行号)

> L7: Kuscia(Kubernetes-based Secure Collaborative InfrA) is a lightweight privacy-preserving computing task orchestration
> L13: - Unified API interface: You can integrate privacy-preserving computing capabilities using HTTP/GRPC API interfaces

## 星数曲线

```mermaid
xychart-beta
    title "secretflow/kuscia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 145 --> 147
    line [146, 146]
```

2026-10-18 146 → 2026-10-25 146（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `acc0105a86f3` · [字段定义](../../DATASET.md)*
