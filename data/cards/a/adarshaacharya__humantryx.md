# adarshaacharya/humantryx

⭐ 31 · TypeScript · MIT · 推送 2026-04-03 · [GitHub](https://github.com/adarshaacharya/humantryx) · [官网](https://humantryx.vercel.app) · 组织维护

**AI 增强的开源人力资源管理系统：员工/考勤/假勤/薪酬一体化**

基于 Next.js 15 + React 19 + TypeScript 构建的人力资源管理系统（HRMS），功能覆盖员工全生命周期管理、打卡考勤与加班计算、多级审批的假勤管理、薪酬与工资单生成、组织架构与公司新闻。AI 能力包括简历筛选、基于 Pinecone 向量库的文档知识检索、自然语言请假解析，使用 OpenAI API、LangChain.js 与 Groq。提供 Better-Auth 认证与 CASL 权限体系，支持 Docker 与 Vercel 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 员工管理、考勤、假勤、薪酬四大模块一体化
- AI 简历筛选、自然语言请假解析、文档知识库检索（OpenAI + LangChain + Pinecone）
- Better-Auth 认证 + CASL 细粒度权限 + 三种角色（Super Admin/HR Manager/Employee）
- 提供 Vercel 与 Docker 两种部署路径

## 适用场景

- 我需要一套可自托管的 HR 管理系统管理员工、考勤与假勤
- 我希望用自然语言提交请假申请并由 AI 解析
- 我想搭建带权限体系的中小型企业 HR 后台

## 场景标签

 · 领域:人力资源管理系统

## 证据(README 行号)

> L7: > **Humantryx** is an AI-powered Human Resource Management System built with Next.js and modern technologies. It str
> L68: - **Resume Screening**: Automated candidate evaluation
> L69: - **Document Knowledge Base**: AI-driven document search and retrieval

## 星数曲线

```mermaid
xychart-beta
    title "adarshaacharya/humantryx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b1a89d7dc029` · [字段定义](../../DATASET.md)*
