# pinecone-io/pulumi-pinecone-byoc

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/pinecone-io/pulumi-pinecone-byoc) · 组织维护

**用 Pulumi 在自有云账号部署 Pinecone 向量数据库的 IaC 工具**

Pinecone 官方的 BYOC（Bring Your Own Cloud）基础设施即代码组件：通过交互式 bootstrap 脚本生成 Pulumi 项目，在用户自己的 AWS/GCP/Azure 账号内部署 Pinecone 向量数据库集群，部署约需 25-30 分钟。采用拉取式控制面模型，集群组件本地拉取并执行索引操作，客户数据不离开用户云账号，仅回传运行指标与状态；Pinecone 在后台自动管理升级。面向需要数据驻留与网络策略自控的企业基础设施/平台团队。以 PyPI 包（uv add）与源码两种方式提供，需 Python 3.12+、uv、Pulumi、kubectl 及对应云 CLI 作为前置条件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 AWS/GCP/Azure 三朵云的自有账号部署
- 拉取式控制面：数据不离开用户云账号，通信均为集群出站方向
- setup 向导生成 Pulumi 项目，可配置 region、AZ、VPC CIDR、删除保护、公网开关等
- 提供 PyPI 包与 Python SDK 形式的程序化集成（PineconeAWSCluster 等组件）

## 适用场景

- 在满足数据驻留要求的自有云账号内运行 Pinecone 向量数据库
- 用 Pulumi 将 Pinecone 集群纳入现有基础设施代码管理
- 通过 PrivateLink/Private Service Connect 限制集群网络访问

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5: Deploy Pinecone in your own cloud account (AWS, GCP, or Azure) with full control over your infrastructure.
> L72: Pinecone BYOC uses a **pull-based model** for control plane operations:
> L80: - **Your data never leaves your cloud account** - only operational metrics and cluster state are transmitted

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/pulumi-pinecone-byoc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ac55fdb1f703` · [字段定义](../../DATASET.md)*
