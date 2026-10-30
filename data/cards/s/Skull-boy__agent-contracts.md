# Skull-boy/agent-contracts

⭐ 23 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/Skull-boy/agent-contracts) · [官网](https://pypi.org/project/scyvera/) · 个人维护

**AI agent 运行前治理层：机器可读契约定义权限边界并强制执行**

提供机器可读的 Agent 契约规范（v1/v1.1）与 Python 治理层：通过 contract.yaml 声明系统的能力、资源、权限、副作用与审批要求。四层治理机制：CLI 静态校验与语义 lint、Default-Deny 运行时执行器（SHA-256 密封）、隔离凭证与原始 SDK 客户端的 Gateway 边界、仅追加的版本化契约注册表。面向需要在 agent 运行前声明与执行操作边界的开发者，框架无关，附 n8n/LangGraph 参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 契约静态校验 + 语义 lint（ACxxx 规则分类）
- Default-Deny 运行时执行器，未声明权限即抛异常，SHA-256 密封
- Gateway 隔离 API 凭证与原始 SDK 客户端，CI 检查防绕过
- 仅追加版本化契约注册表，支持按时间点查询

## 适用场景

- 在 agent 运行前声明其可做、需审批与禁止的操作
- 为高风险场景（金融支付上限、医疗审批门）强制执行操作边界
- 审计历史上任一时刻哪个契约治理了哪个 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: `Scyvera` provides a machine-readable specification and Python governance layer for defining and enforcing the oper
> L25: A framework-independent and domain-independent governance layer describing and enforcing system identity, capabilit

## 星数曲线

```mermaid
xychart-beta
    title "Skull-boy/agent-contracts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `71687267cf0f` · [字段定义](../../DATASET.md)*
