# goshops-com/opsagent

⭐ 10 · TypeScript · MIT · 推送 2026-04-13 · [GitHub](https://github.com/goshops-com/opsagent) · [官网](https://github.com/sjcotto/opsagent#readme) · 组织维护

**运维人员的服务器监控守护进程，AI 分析告警并自动修复**

基于 Bun 的系统监控 agent，使用 NetData 采集 1 秒粒度指标并产生告警，将告警交给 LLM 分析并给出修复建议；安全动作自动执行，高风险动作（kill_process、restart_service 等）需人工在 Discord 或控制面板批准。支持 readonly/limited/standard/full 四级权限控制、告警聚合为 issue 防止通知刷屏、MongoDB/PostgreSQL/Redis/MySQL 数据库监控，以及多机部署加中央控制面板。安装脚本会自动安装 Bun、PM2 与 NetData。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 分析 NetData 告警并生成修复建议，低风险动作自动执行
- 七类动作按风险分级，配合四级 permissionLevel 控制 agent 权限
- 多机部署与带密码保护的中央控制面板
- 通过 NetData 采集器监控 MongoDB/PostgreSQL/Redis/MySQL

## 适用场景

- 给多台服务器部署统一监控，AI 分析告警减少人工排查
- 深夜告警自动清理缓存，高风险操作留人工审批
- 通过 Discord 接收需要人工介入的服务器问题通知

## 场景标签

 · 领域:DevOps/系统监控

## 证据(README 行号)

> L10: An intelligent system monitoring agent that uses NetData for metrics collection and AI to analyze alerts and recomm
> L61: - **AI-Powered Remediation** - Uses LLMs to analyze alerts and recommend actions


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `481bebf268bb` · [字段定义](../../DATASET.md)*
