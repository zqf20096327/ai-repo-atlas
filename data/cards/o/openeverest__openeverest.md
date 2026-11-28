# openeverest/openeverest

⭐ 981 · TypeScript · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/openeverest/openeverest) · [官网](https://openeverest.io/) · 组织维护

**面向开发者在 Kubernetes 上部署管理数据库/存储/LLM 的平台**

OpenEverest 是运行在 Kubernetes 上的开源云原生数据库平台，提供点击式创建数据库实例、扩缩容、维护、监控、备份自动化与数据安全等能力，目标是减少数据库管理开销并控制 DBaaS 成本。支持通过 Helm chart 或 everestctl CLI（含向导与 headless 模式）安装，可管理多个 namespace 与 MongoDB/PostgreSQL/MySQL 等数据库 operator。当前 main 分支为 v2（未 GA，API 可能变动），v1.x 为当前 GA 版本，v2 GA 后 v1 再获 6 个月修复支持。提供商业支持与社区支持渠道。

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

- 提供 Helm 与 everestctl CLI 两种安装方式，支持向导与 headless 模式
- 安装时可选装 MongoDB/PostgreSQL/MySQL 数据库 operator
- 默认不暴露外部 IP，提供 Port Forwarding 与 LoadBalancer 访问方式
- 提供商业支持（认证合作伙伴）与社区支持渠道

## 适用场景

- 在云上或本地 Kubernetes 集群中自建数据库即服务（DBaaS）
- 为开发团队提供一键创建和管理数据库实例的自助平台
- 统一管理多个 namespace 下的数据库 operator 与备份策略

## 场景标签

 · 领域:云原生/数据库管理

## 证据(README 行号)

> L3: OpenEverest - Run Data Workloads on Kubernetes
> L20: OpenEverest is an open source cloud-native database platform that helps developers deploy code faster, scale deploy
> L161:    everestctl install --namespaces <namespace-name1>,<namespace-name2> --operator.mongodb=true --operator.postgres

## 星数曲线

```mermaid
xychart-beta
    title "openeverest/openeverest 星数(近 18 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 952 --> 983
    line [954, 955, 956, 957, 959, 960, 954, 964, 966, 967, 969, 972, 974, 975, 974, 978, 979, 981]
```

2026-10-26 954 → 2026-11-28 981（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `ef6ef5840042` · [字段定义](../../DATASET.md)*
