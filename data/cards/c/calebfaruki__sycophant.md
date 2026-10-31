# calebfaruki/sycophant

⭐ 14 · Rust · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/calebfaruki/sycophant) · 个人维护

**在 Kubernetes 上零信任隔离运行自主 AI agent 的框架**

面向 DevOps 的自主 AI agent 运行框架，以最小权限、零知识、纵深防御为原则把 agent 跑在 Kubernetes 集群内。每租户一个 namespace，每次工具或模型调用都在短生命周期的 gVisor 沙箱 pod 中运行，凭据由 broker 分发并在输出中脱敏；对话日志由 agent 不可写的独立组件持有。组件含 Harness（运行时与 broker）、Relay（客户端网关）、Toolset（工具沙箱），以 Rust monorepo、Helm charts 与 sycoadm CLI 交付。处于 pre-release（版本 0.01）。依赖 Cilium、Kyverno、gVisor/Kata 等集群能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型/工具调用运行在一次性 gVisor 沙箱 pod，凭据仅存在于单次调用内
- 对话日志存于 agent 不可写卷，agent 无法改写自身历史
- Cilium 默认拒绝出口流量，Kyverno 在 namespace 创建时生成 RBAC 并阻止内部篡改
- 以 Chainsaw 集成测试在真实集群上验证安全规则（每条测试尝试禁止行为并检查集群拒绝）

## 适用场景

- 在企业自有 Kubernetes 集群内以隔离方式运行自主 AI agent
- 限制被攻陷 agent 的能力：不读密钥、不自由出网、不跨租户
- 多租户场景下为每个租户提供独立网络、存储与身份隔离

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Sycophant runs autonomous AI agents inside a Kubernetes cluster built on least privilege, zero knowledge, and defen
> L79: Three components, each with a single, well-defined job. The harness is the broker: the agent asks it for a tool or 

## 星数曲线

```mermaid
xychart-beta
    title "calebfaruki/sycophant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d4bbd7655bb6` · [字段定义](../../DATASET.md)*
