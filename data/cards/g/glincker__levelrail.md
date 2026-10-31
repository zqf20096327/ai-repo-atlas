# glincker/levelrail

⭐ 129 · Go · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/glincker/levelrail) · [官网](https://levelrail.com) · 个人维护 · 中文 README

**自托管 PaaS：git push 部署到自有服务器，含 HTTPS/日志/回滚**

面向开发者与小团队的开源自托管 PaaS，单个 Go 二进制加 Docker 运行时，在自有 Linux 服务器上提供 Git push 部署（forge webhook）、HTTPS（内嵌 Caddy）、数据库与校验备份、指标、日志、告警与回滚，不依赖 Kubernetes。控制平面用 SQLite 存期望状态，reconciler 调度 Docker；节点以反向拨出的 agent 经 mTLS 通信。另提供 MCP server（240+ 工具）与 agent skill 供编码代理操作部署。状态为 pre-1.0，多节点为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 Go 二进制 + Docker 运行时，无 Kubernetes
- MCP server 含 240+ 工具（按需工具集）与 agent skill
- readiness 门控发布、固定镜像回滚、金丝雀与审批/冻结
- Coolify/Dokploy/CapRover/Dokku 迁移 dry-run

## 适用场景

- 在自己的 VPS/裸机上获得 Vercel/HeroKu 风格的部署流程
- 小团队搭建带指标、日志与告警的私有部署平台
- 让编码代理通过 MCP 执行部署与回滚
- 从 Coolify/Dokku 等平台做迁移演练

## 场景标签

 · 领域:DevOps/自托管部署

## 证据(README 行号)

> L3:  Self-hosted PaaS: deploy on git push to your own servers, with logs, metrics, HTTPS and rollback.
> L169: - **Built for AI agents.** An MCP server with over 240 tools in on-demand toolsets (small default list, about 2.4k


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b103be8d9554` · [字段定义](../../DATASET.md)*
