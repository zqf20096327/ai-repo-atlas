# mindspore-ai/infrastructure

⭐ 44 · Dockerfile · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/mindspore-ai/infrastructure) · 组织维护 · 中文 README

**MindSpore 社区基础设施：部署社区组件的 dockerfile 与 yaml**

存放 MindSpore 社区各类基础设施的部署文件仓库，分 development 与 production 两目录，包含 helm chart、初始化脚本与 dockerfile。覆盖组件有：ArgoCD 部署服务、Vault 密钥服务器与 Secrets Manager（通过 AppRole 同步 Vault 密钥到 k8s secret）、基于 Docker mailman 的邮件系统、记录会议纪要的 MeetingBot、Jenkins 构建系统、官方网站、基于 prow 的 CI Bot、nginx+rsync 的 repo 系统。全部组件部署在两个华为云 CCE k8s 集群（x86 与 arm 节点）上。面向维护 MindSpore 社区基础设施的运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- development/production 两级目录管理 helm chart、脚本与 dockerfile
- 组件经 ArgoCD 统一部署，Vault+Secrets Manager 管理密钥并同步至 k8s secret
- 覆盖 Jenkins、prow CI Bot、邮件系统、repo 服务器等社区组件
- 部署于两个华为云 CCE 集群（cn-north-1 x86 与 cn-north-4 arm）

## 适用场景

- 维护 MindSpore 社区各在线服务的部署与配置
- 了解 MindSpore 社区基础设施的组成与部署方式
- 参考 k8s+ArgoCD+Vault 的社区基础设施实践

## 场景标签

 · 领域:DevOps/基础设施

## 证据(README 行号)

> L3: This project contains all necessary dockerfile and yaml files that used provision the mindspore community:
> L6: └── production #contains the final yaml file that will be used in our production environment.

## 星数曲线

```mermaid
xychart-beta
    title "mindspore-ai/infrastructure 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `c61ea04a520d` · [字段定义](../../DATASET.md)*
