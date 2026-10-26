# Fridolph/my-resume

⭐ 35 · TypeScript · GPL-3.0 · 推送 2026-10-07 · [GitHub](https://github.com/Fridolph/my-resume) · [官网](https://resume.fridolph.top) · 个人维护 · 中文 README

**教程型全栈个人简历站：三端架构含 AI 工作台与 RAG**

从旧版 Vue 简历站渐进重构的 pnpm Monorepo，含 web 公开简历展示（双语、主题、导出）、admin 后台编辑与 AI 工作台、server NestJS 业务后端（鉴权、简历、导出、AI/RAG）。AI 层支持多 Provider（mock/qiniu/deepseek/openai-compatible）与 RAG 最小链路。提供本地演示账号、Docker Compose 一键启动、构建 amd64 镜像推送 GHCR 并部署 ECS 的脚本，及 Vercel 部署说明。路线图含 AI 工作台与 RAG 增强计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- web/admin/server 三端架构，pnpm workspace + Turbo 管理
- AI 多 Provider 接入（mock/qiniu/deepseek/openai-compatible）与 RAG 最小链路
- Docker Compose 本地一键启动与 ECS 部署脚本
- Issue 驱动、里程碑式推进（M1→M20+）并配套教程文档

## 适用场景

- 搭建并持续迭代自己的工程化简历站点
- 学习 Next.js/NestJS 全栈与云服务器部署流程
- 在后台用 AI 工作台辅助编辑简历内容

## 场景标签

`教程课程` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L28: - `web`：公开简历展示（双语、主题、导出入口）
> L29: - `admin`：后台编辑、发布、AI 工作台
> L30: - `server`：唯一业务后端（鉴权、简历、导出、AI/RAG）
> L53: |AI|多 Provider（mock / qiniu / deepseek / openai-compatible）, RAG 最小链路|

## 星数曲线

```mermaid
xychart-beta
    title "Fridolph/my-resume 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c71b1cd09846` · [字段定义](../../DATASET.md)*
