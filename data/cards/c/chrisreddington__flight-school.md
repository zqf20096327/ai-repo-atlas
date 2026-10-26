# chrisreddington/flight-school

⭐ 30 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/chrisreddington/flight-school) · 个人维护

**基于 Copilot SDK 的开发者编码练习学习平台示例**

单开发者探索性示例项目：用 GitHub Copilot SDK 构建面向开发者的编码练习平台。通过 GitHub App OAuth 认证并读取用户 GitHub 画像与仓库，生成个性化每日练习、沙盒挑战与实时 AI 评估、渐进式提示和 AI 教练对话。架构上采用多租户隔离：每用户独立的 Copilot CLI 子进程与 COPILOT_HOME，公共路由经私有 Copilot worker 执行。技术栈为 Next.js/TypeScript 与 Aspire AppHost，本地运行需注册 GitHub App 并持有 Copilot 订阅。README 明确声明非生产就绪、不作为参考架构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 GitHub 画像生成个性化每日挑战、实时 AI 评估与渐进式提示
- 多租户隔离：每用户独立 Copilot CLI 子进程与 COPILOT_HOME
- 接入 GitHub Remote MCP Server 实现基于真实仓库的上下文对话
- Aspire AppHost 编排 web 与 worker，OpenTelemetry 双进程追踪

## 适用场景

- 开发者通过个性化挑战与 AI 教练提升编码技能
- 学习 GitHub Copilot SDK 的会话管理、MCP 集成与流式响应模式
- 参考多租户 Copilot 执行边界的架构探索（作者声明不作为参考）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: Flight School is a sample implementation showing how to build AI-powered developer tools using the GitHub Copilot SD
> L134: Flight School gathers data from your GitHub profile and repositories through the Octokit package and uses the Copi

## 星数曲线

```mermaid
xychart-beta
    title "chrisreddington/flight-school 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2375adb4b9b4` · [字段定义](../../DATASET.md)*
