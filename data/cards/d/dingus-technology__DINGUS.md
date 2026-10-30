# dingus-technology/DINGUS

⭐ 23 · Python · GPL-3.0 · 推送 2025-11-23 · [GitHub](https://github.com/dingus-technology/DINGUS) · [官网](https://www.dingusai.dev) · 组织维护

**把生产日志编译为可读修复建议的运维调试工具**

面向开发与运维人员的生产问题调试工具：汇总日志、指标、代码与提交记录构建事件全貌，定位重要问题、追踪根因并给出可执行的修复建议，替代在仪表盘与日志中人工检索的方式。通过 Helm 部署到 Kubernetes 集群，或用 Docker Compose 从源码构建启动，需将 kube config 放置在仓库顶层目录以观察集群，UI 经端口转发访问 8501 端口；另提供模拟日志仓库用于本地试用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 汇总日志、指标、代码与提交记录构建事件全貌
- 自动定位重要问题、追踪根因并给出修复建议
- 支持 Helm 部署到 Kubernetes 与 Docker Compose 本地运行
- 提供模拟仓库生成本地测试用假日志

## 适用场景

- 生产故障时快速定位根因而不是翻日志和仪表盘
- 在 Kubernetes 环境中部署获得问题修复建议
- 本地用模拟日志试用产品能力

## 场景标签

 · 领域:运维/可观测性

## 证据(README 行号)

> L6: Dingus is a tool to gather critical insights and recommend fixes, making it easier and faster to resolve production 
> L12: Dingus reviews logs, metrics, code, commits and more in order to build a holistic view of what casued a production 
> L34: ## 🐳 Run Dingus with Docker

## 星数曲线

```mermaid
xychart-beta
    title "dingus-technology/DINGUS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0009bfb2b7c8` · [字段定义](../../DATASET.md)*
