# microsoft/typescript-skills

⭐ 12 · JavaScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/microsoft/typescript-skills) · 组织维护

**为 AI 编码代理提供 TypeScript/JS/Node 技能的插件库**

微软维护的 Agent Skills 格式技能仓库，以 typescript 插件形式提供 5 个技能：项目脚手架与配置、发布类型声明、配置 project references 与增量构建、启用严格类型检查并修复报错、按版本迁移升级 TypeScript。支持 Copilot CLI、Claude Code、VS Code、Codex CLI 与 Cursor 的插件市场安装，部分技能通过 npx 调用外部检查工具。仓库本身不含自动化评估流程，上游实验结果不代表本仓库技能的评估。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个技能覆盖 TS 项目搭建、声明发布、构建引用、严格检查与版本升级
- 遵循 Agent Skills 格式与 dotnet/skills 的市场/插件布局
- 支持 Copilot CLI、Claude Code、VS Code、Codex CLI、Cursor 五种宿主安装
- README 声明无仪表盘、定时评估或自动发布流程

## 适用场景

- 让编码代理按推荐配置初始化新的 TypeScript 项目
- 在 monorepo 中配置 project references 与增量构建
- 发布可被消费者解析的类型声明包
- 在不弱化类型、测试或运行时行为的前提下开启严格检查

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Skills for coding agents working with TypeScript, JavaScript, and Node.js.
> L5: Skills use the Agent Skills format.
> L24: The skills provide instructions for configuring projects, managing build


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e1c0d6302354` · [字段定义](../../DATASET.md)*
