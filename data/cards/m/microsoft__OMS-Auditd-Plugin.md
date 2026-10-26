# microsoft/OMS-Auditd-Plugin

⭐ 29 · C++ · NOASSERTION · 推送 2026-08-20 · [GitHub](https://github.com/microsoft/OMS-Auditd-Plugin) · 组织维护

**将 Linux auditd 审计事件转发至 OMS Agent 的插件**

Auditd 插件，读取 Linux 审计事件并转发给 OMS Agent for Linux，用于将系统审计数据接入 OMS 监控管道。构建流程为：克隆 pal 与本仓库源码，用 Docker 构建 64 位与 32 位构建镜像，再通过脚本在容器内编译生成 auoms 产物。README 仅包含环境准备与构建说明，面向在 Linux 环境部署 OMS 审计采集的开发者或运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 auditd 插件形式转发审计事件到 OMS Agent for Linux
- 提供基于 Docker 的 64 位与 32 位构建流程
- 依赖 Microsoft pal 源码仓库共同构建

## 适用场景

- Linux 服务器上把 auditd 审计事件接入 OMS 监控
- 构建部署 auoms 审计采集组件

## 场景标签

 · 领域:系统运维/安全审计

## 证据(README 行号)

> L2: Auditd plugin that forwards audit events to OMS Agent for Linux
> L13:  docker build -t auoms-build auoms-build

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/OMS-Auditd-Plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a01d024059a0` · [字段定义](../../DATASET.md)*
