# virastack/start

⭐ 104 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/virastack/start) · [官网](https://www.virastack.com/start/) · 个人维护

**为 Next.js/TanStack Start 生成项目脚手架并配置 AI 编码规则**

交互式 CLI，用一条命令创建 Next.js 或 TanStack Start 项目：复制模板、按所用的包管理器安装依赖、生成 feature-sliced 架构基础与严格 TypeScript/Zod 配置。它询问用户使用的 AI 编码工具（Claude Code、Cursor），随后运行 @virastack/ai init 写入各工具原生格式的架构规则、AGENTS.md 及三个设计技能（emil-design-eng、better-ui、better-accessibility），并可追加 @virastack/mask、@virastack/password 工具。支持 pnpm/npx/yarn/bun 调用、非交互模式与 --skip-install、离线降级。

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

- 一条命令脚手架 Next.js 或 TanStack Start 项目（含默认状态/表单/UI/测试技术栈）
- 按所选 AI 工具（Claude Code/Cursor）写入原生格式架构规则与 AGENTS.md
- 自动安装三个设计技能到 .agents/skills/（Claude Code 下为 .claude/skills/）
- 支持 pnpm/npm/yarn/bun 与非交互模式、--skip-install、离线降级

## 适用场景

- 快速启动带预配置架构的 Next.js 或 TanStack Start 项目
- 让 Claude Code 或 Cursor 从第一天起遵循项目架构规则
- 向现有项目追加 mask/password/ai 等 ViraStack 工具

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L22: - **Built-in AI Protocols:** Asks which AI coding tools you use (Claude Code, Cursor) and sets up **ViraStack AI** 
> L58: 4. Runs `@virastack/ai init --agent <your choice>`. It never overwrites files you changed.
> L59: 5. Installs three design skills: `emil-design-eng` (Emil Kowalski), `better-ui` and `better-accessibility` (Jakub K

## 星数曲线

```mermaid
xychart-beta
    title "virastack/start 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-29 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4ed2bd04abc0` · [字段定义](../../DATASET.md)*
