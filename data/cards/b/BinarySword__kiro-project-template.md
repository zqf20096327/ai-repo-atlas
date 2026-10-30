# BinarySword/kiro-project-template

⭐ 20 · TypeScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/BinarySword/kiro-project-template) · 个人维护

**面向 Kiro AI agent 的项目脚手架模板：47 篇 steering 文档、48 个 hooks 与 CLI**

为 Kiro AI agent 提供开箱即用的项目配置模板：包含 47 篇 steering 指导文档（核心规则、开发流程、领域标准等）、48 个按 IDE 事件触发的 hooks、spec 模板与示例、以及 CLI 脚手架。CLI 支持 13 种技术栈预设（T3、Supabase+Next.js、Vite+React、SvelteKit、Nuxt 3、Flutter 等），可交互或 headless 模式运行，并可调用各栈官方 scaffolder。另有 setup.sh 向导完成项目标识、包管理器选择与文档清理。通过 npx/pnpm create/bunx 安装。

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

- 47 篇 steering 文档与 48 个事件触发 hooks
- CLI 脚手架支持 13 种技术栈预设，支持交互与 headless 模式
- setup.sh 五步向导，支持 --dry-run 与环境变量预填
- 4 个示例 spec 展示完整 spec 生命周期

## 适用场景

- 为新项目快速生成规范的 .kiro/ 配置
- 向既有项目注入 .kiro/ 配置（CLI --add 模式）
- 按团队技术栈定制 steering 文档与 hooks

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: An opinionated project template with comprehensive Kiro AI agent configuration — 47 steering docs, 48 hooks, spec te
> L79: .kiro/                    # Kiro AI agent configuration

## 星数曲线

```mermaid
xychart-beta
    title "BinarySword/kiro-project-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3181f38b455a` · [字段定义](../../DATASET.md)*
