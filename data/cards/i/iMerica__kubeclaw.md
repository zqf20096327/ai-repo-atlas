# iMerica/kubeclaw

⭐ 41 · Go · Apache-2.0 · 推送 2026-06-29 · [GitHub](https://github.com/iMerica/kubeclaw) · [官网](https://kubeclaw.ai) · 个人维护

**在 Kubernetes 上生产化部署 OpenClaw 的 Helm chart**

将 OpenClaw agent 封装为 Helm chart 的部署与运维层：提供 StatefulSet 持久化存储、镜像 tag+digest 钉扎、Gateway API 路由、Chromium 浏览器自动化 Deployment、LiteLLM 代理子 chart（虚拟密钥/预算/模型回退）、Wide Events 可观测性（ClickHouse + HyperDX + OTel）、Blocky 出口 DNS 过滤、容器加固、NetworkPolicy、S3 备份及 Tailscale 接入。面向在 Kubernetes 1.25+ 与 Helm 3.12+ 环境下运维 OpenClaw 的平台/DevOps 团队，项目自标注为 Alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- StatefulSet + 分离 workspace PVC 与声明式 openclaw.json 配置
- LiteLLM 子 chart 提供按 agent 虚拟密钥、预算上限与模型回退路由
- Wide Events 统一日志/指标/追踪到 ClickHouse，附 HyperDX 与 OTel
- 出口 DNS 过滤（Blocky）、NetworkPolicy 默认拒绝与容器加固

## 适用场景

- 在自有 Kubernetes 集群中按 GitOps 方式部署和升级 OpenClaw
- 对 agent 出口流量做默认拒绝与白名单管控
- 统一收集 agent 运行的日志、指标与事件用于审计

## 场景标签

`模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L10: Production-grade OpenClaw on Kubernetes.
> L30: KubeClaw wraps OpenClaw with the operational guardrails that production deployments need: secure defaults, pinned i
> L106: |**LiteLLM proxy subchart**|Per-agent virtual keys, budget caps, model fallback routing, and semantic caching (Red

## 星数曲线

```mermaid
xychart-beta
    title "iMerica/kubeclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-28 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `65191b79c86a` · [字段定义](../../DATASET.md)*
