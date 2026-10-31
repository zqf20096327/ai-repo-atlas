# wellCh4n/oops

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/wellCh4n/oops) · 个人维护 · 中文 README

**面向人类与 AI Agent 的 Kubernetes 应用部署平台**

一个 Kubernetes PaaS，将人类与 AI Agent 设为同等的一等操作者：通过 Web UI 或绑定的 OOPS CLI Skill 部署应用（推送代码或上传 ZIP、构建镜像、滚动发布、一键回滚），支持多集群管理、按环境调整资源与探针、团队权限控制、实时日志与浏览器终端、飞书流水线通知、Agent 沙箱（一次性流式执行或常驻实例）、OpenAPI 与 code-server IDE。要求 Kubernetes 1.22+ 与 MySQL 8.x，Docker Compose 或源码方式运行。

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

- UI 与 OpenAPI/CLI Skill 双通道，同一操作面供人类与 Agent 使用
- Agent 沙箱：隔离工作区运行命令、安装工具、编辑文件、调试
- 多集群管理与单控制台多域名、自动 HTTPS
- 流水线状态推送至飞书（Lark）

## 适用场景

- 把代码或 ZIP 快速构建并部署到多个 Kubernetes 集群
- 让 AI Agent 通过 CLI Skill 或 OpenAPI 驱动部署与运维操作
- 团队在浏览器里查看日志、终端与资源用量的统一运维台

## 场景标签

 · 领域:DevOps/Kubernetes 平台

## 证据(README 行号)

> L6: OOPS is a Kubernetes PaaS where **humans and AI Agents are equal first-class operators**. Deploy applications, manag
> L42: ### A sandbox built for Agents
> L45: ### Programmatic OpenAPI

## 星数曲线

```mermaid
xychart-beta
    title "wellCh4n/oops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `06121f7d3bb0` · [字段定义](../../DATASET.md)*
