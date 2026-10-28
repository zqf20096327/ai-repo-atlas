# instill-ai/console

⭐ 41 · TypeScript · NOASSERTION · 推送 2026-06-17 · [GitHub](https://github.com/instill-ai/console) · [官网](https://www.instill-ai.com) · 组织维护

**Instill Core 的 Web 控制台：浏览器中管理 AI 流水线与模型**

基于 Next.js、TypeScript 与 TailwindCSS 开发的前端应用，作为 Instill Core 的统一界面，在 Docker 容器中与其他组件一同运行；用户可在浏览器中创建、管理和观测流水线、模型与制品。仓库采用 monorepo 结构，包含 design-system、design-token、toolkit 等共享包；已支持 Slack 与 GitHub 的 OAuth 集成连接。运行需前往 instill-core 仓库，本仓库未给出独立的安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器中创建、管理与观测流水线、模型和制品
- 以 Docker 容器形式与 Instill Core 其他组件协同运行
- 共享 design-system/toolkit 前端包的 monorepo 结构
- 已支持 Slack 与 GitHub OAuth 集成连接

## 适用场景

- 通过可视化界面搭建和管理 AI 数据流水线
- 在浏览器中观测模型与制品的运行状态
- 为 Instill Core 部署提供统一操作入口

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: The console, developed using Nextjs, Typescript, and TailwindCSS, operates in a docker container alongside other **🔮
> L9: The primary objective of the console is to offer a unified, streamlined, and user-friendly interface for **🔮 Instill

## 星数曲线

```mermaid
xychart-beta
    title "instill-ai/console 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7ad1acac3e8e` · [字段定义](../../DATASET.md)*
