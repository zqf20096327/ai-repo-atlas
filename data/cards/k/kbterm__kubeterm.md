# kbterm/kubeterm

⭐ 231 · 推送 2026-10-19 · [GitHub](https://github.com/kbterm/kubeterm) · [官网](https://www.kubeterm.com) · 组织维护 · 中文 README

**Kubernetes 图形化管理工具，内置 AI 助手辅助排障**

跨桌面与移动端的 Kubernetes 集群图形化管理应用：读取本地 kubeconfig 零配置接入集群，支持资源查看与增删改、弹性伸缩、节点 cordon/drain、临时容器调试、日志查看、文件传输、端口转发、Helm 管理与 Prometheus 指标集成。内置 AI Agent 可基于当前集群上下文协助排障，变更操作需用户批准；应用本身非开源，仓库承载 issue、发布与文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地运行，无需在集群内安装任何组件
- 内置 AI Agent 基于集群上下文排障，变更操作需显式批准
- 支持 GCP/Azure 账号登录导入集群、多种云凭证与 OIDC 认证
- 覆盖调试、文件传输、端口转发、Helm 管理与 Prometheus 指标

## 适用场景

- 在图形界面中查看和操作 Kubernetes 集群资源
- 排查 Pod/节点问题，查看日志与历史指标
- 通过 AI 助手基于集群上下文定位故障并经批准执行变更

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: Kubeterm is a graphical management tool for Kubernetes clusters.
> L24: - **AI Agent:**
> L73: Kubeterm includes a built-in AI Agent for Kubernetes operations and troubleshooting.

## 星数曲线

```mermaid
xychart-beta
    title "kbterm/kubeterm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 229 --> 232
    line [230, 231, 231]
```

2026-10-18 230 → 2026-10-24 231（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f1eac9029cc8` · [字段定义](../../DATASET.md)*
