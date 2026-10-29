# sanjay22-s/ai-ticket-system

⭐ 61 · Python · 推送 2026-02-26 · [GitHub](https://github.com/sanjay22-s/ai-ticket-system) · [官网](https://ticket-creation-rho.vercel.app/) · 个人维护

**带 AI 工单创建与分类的全栈客服工单系统**

FastAPI + React + PostgreSQL 构建的工单管理仪表盘，仓库描述称其具备 AI 驱动的工单创建与机器学习分类能力；README 可见部分主要覆盖工单查看、筛选、分派、备注等客服流程：后端提供 JWT 认证与工单 CRUD API，前端为 React 仪表盘，附种子数据脚本与默认测试账号。需自行配置 PostgreSQL 数据库与环境变量后分端启动。

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

- FastAPI + PostgreSQL + SQLAlchemy 后端，JWT 认证保护除登录外的全部 API
- React (Vite + TypeScript) + Tailwind CSS 前端仪表盘
- 提供种子数据脚本与默认 Agent/Admin 测试账号
- 仓库描述声明 AI 工单创建与机器学习分类能力

## 适用场景

- 客服团队查看、筛选、分派和管理工单
- 通过仪表盘统计工单数量并跟进处理进度
- 作为 AI 工单分类系统的全栈参考实现进行二次开发

## 场景标签

 · 领域:客服/工单管理

## 证据(README 行号)

> L1: # AI-Powered Ticket Creation – Agent Dashboard
> L7: - **Backend:** FastAPI (Python), PostgreSQL, SQLAlchemy, JWT
> L8: - **Frontend:** React (Vite + TypeScript), Tailwind CSS, Context API, Axios

## 星数曲线

```mermaid
xychart-beta
    title "sanjay22-s/ai-ticket-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-29 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `14a6a3fd2b96` · [字段定义](../../DATASET.md)*
