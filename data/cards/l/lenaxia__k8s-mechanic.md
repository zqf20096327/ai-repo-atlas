# lenaxia/k8s-mechanic

⭐ 60 · Go · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/lenaxia/k8s-mechanic) · 个人维护

**监测 K8s 故障并用 LLM agent 自动开修复 PR 的控制器**

在集群内运行的 Kubernetes 控制器：通过 K8s API 监测 Pod 崩溃、Deployment 降级、Node NotReady 等故障，按父资源去重并经稳定窗口过滤后，派生 OpenCode agent Job 以只读 RBAC 检查集群与 GitOps 仓库，定位根因并开出包含证据与置信度的修复 PR，需人工合并。兼容任意 OpenAI 兼容 LLM 端点。安全机制包括密钥脱敏、提示注入检测、短时效 GitHub App token、kubeconform 强制校验与可选 hardened 模式。需 Kubernetes>=1.28、Helm、GitHub App 与 LLM API key。原名 k8s-mendabot。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测 CrashLoopBackOff/OOMKilled/Node NotReady 等 8 类故障并按父资源去重
- 集群内 OpenCode agent 生成带证据与置信度的修复 PR，强制人工合并
- 只读 RBAC、密钥脱敏、提示注入检测、kubectl 写操作封锁等安全机制
- kubeconform/kustomize 强制清单校验，校验失败开 validation-failed 占位 PR

## 适用场景

- GitOps 集群故障后自动生成修复 PR 供人工审查
- 集群无人值守时段的故障调查与报告留档
- 借助 dry-run 模式在预发环境验证修复行为与新模型

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: k8s-mechanic is a Kubernetes controller that watches your cluster for failures,
> L12: mechanic spawns an in-cluster OpenCode agent that inspects
> L43: **OpenCode agentic workflow** — investigations are driven by OpenCode

## 星数曲线

```mermaid
xychart-beta
    title "lenaxia/k8s-mechanic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-26 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cff55b31d278` · [字段定义](../../DATASET.md)*
