# rahadbhuiya/cnsl

⭐ 14 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/rahadbhuiya/cnsl) · [官网](https://pypi.org/project/cnsl) · 个人维护

**面向 Linux 的自托管 SIEM：跨日志关联检测攻击并自动封禁**

CNSL 是一个自托管的 Linux 安全监控与响应系统：同时读取 SSH、Web、数据库、云日志，将同一来源的多路行为（扫描、暴力破解、认证失败）关联为一次协同攻击并经 iptables 自动阻断，同时跟踪攻击者在 kill chain 中的进展。附加功能包括多节点联邦与统一 hub 视图、STIX 2.1 导出与内置 TAXII 2.1 服务器、Wazuh/OSSEC 集成、PostgreSQL 支持、Kubernetes Helm 部署、攻击者指纹与图式战役关联、可选的预测性阻断，以及基于机器学习的模式学习与 UEBA。通过 pip 安装，默认 dry-run 模式，需 root 或 CAP_NET_ADMIN 执行封禁。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 SSH/Web/数据库/云日志的关联检测与 iptables 自动阻断
- 多节点联邦、STIX 2.1 导出与内置 TAXII 2.1 服务器
- 自动学习新攻击模式与可选预测性阻断（UEBA/ML）
- 提供设置向导、Web 仪表盘与 Kubernetes Helm 部署

## 适用场景

- 在 Linux 服务器上检测跨多种日志的协同攻击并自动封禁
- 多台服务器间共享威胁情报并统一查看安全态势
- 以 STIX/TAXII 标准与 SIEM 连接器对接现有安全体系

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: **A self-hosted SIEM for Linux.**
> L25: It also tracks how far each attacker has progressed through the kill chain, learns new attack patterns automaticall
> L27: **Beyond core detection:** multi-node federation with a unified hub view, STIX 2.1 export and a built-in TAXII 2.1 

## 星数曲线

```mermaid
xychart-beta
    title "rahadbhuiya/cnsl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `900c9a871d2f` · [字段定义](../../DATASET.md)*
