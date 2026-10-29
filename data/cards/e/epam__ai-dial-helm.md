# epam/ai-dial-helm

⭐ 23 · Go Template · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/epam/ai-dial-helm) · [官网](https://dialx.ai) · 组织维护

**AI DIAL 平台的 Helm Chart 仓库，用于 Kubernetes 部署**

EPAM 维护的 AI DIAL Helm Chart 仓库，通过 charts.dialx.ai 提供 AI DIAL 相关 Chart 的分发、检索与安装卸载。Chart 仓库地址已从 charts.epam-rail.com 迁移至 charts.dialx.ai，旧地址不再更新且即将不可用，用户需更新本地 Helm 仓库配置。要求先安装 Helm，随后以 helm repo add / search / install 命令使用；Apache 2.0 许可。

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

- Helm Chart 分发：repo add / search / install / delete 工作流
- 仓库地址已迁移至 charts.dialx.ai，旧地址将停用
- Apache 2.0 许可并在 Artifact Hub 发布

## 适用场景

- 在 Kubernetes 上部署 AI DIAL 相关组件
- 通过 Helm 检索并安装 DIAL Chart

## 场景标签

 · 领域:AI 平台部署/DevOps

## 证据(README 行号)

> L1: # EPAM AI DIAL Helm Repository
> L36: helm install my-release dial/<chart-name>

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-helm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a8c50f52e2d4` · [字段定义](../../DATASET.md)*
