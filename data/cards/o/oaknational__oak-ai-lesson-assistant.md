# oaknational/oak-ai-lesson-assistant

⭐ 35 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/oaknational/oak-ai-lesson-assistant) · [官网](https://labs.thenational.academy) · 组织维护

**Oak 国家学院的 AI 课程规划助手（Aila）monorepo**

Oak National Academy 面向教师课程规划的 AI 助手项目仓库，以 Turborepo monorepo 组织，包含 Next.js 应用与 aila 包等组件。README 声明项目主要为内部使用，不预期外部用户运行，安装文档（pnpm、Doppler 密钥管理、Docker Postgres 数据库、Prisma schema）面向内部环境。包含 Jest 与 Playwright 测试、ESLint/Prettier/Sonar 等代码质量工具，目前不接受外部代码贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Turborepo monorepo 结构，含 Next.js 应用与 aila 包
- 使用 Doppler CLI 管理密钥
- Docker 启动 Postgres（含 pgvector）并用 Prisma 管理数据
- 提供 Jest 单元测试与 Playwright 端到端测试

## 适用场景

- Oak 内部开发与测试 AI 课程规划工具
- 了解教育机构 AI 助手项目的工程组织方式

## 场景标签

 · 领域:教育/AI 应用

## 证据(README 行号)

> L5: > **Disclaimer**
> L8: Oak AI Lesson Assistant is a project focused on experimenting with AI models and their applications. This repository

## 星数曲线

```mermaid
xychart-beta
    title "oaknational/oak-ai-lesson-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `059f61666098` · [字段定义](../../DATASET.md)*
