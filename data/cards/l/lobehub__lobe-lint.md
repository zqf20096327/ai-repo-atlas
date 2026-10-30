# lobehub/lobe-lint

⭐ 45 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/lobehub/lobe-lint) · [官网](https://lint.lobehub.com/) · 组织维护

**LobeHub 系项目的共享 Lint/格式化/提交规范配置包**

由 LobeHub 维护的代码风格工具集：以 @lobehub/* 系列包形式提供 ESLint、Prettier、Stylelint、Commitlint（Gitmoji 规范）、Remarklint 与 semantic-release 配置，可整包安装 @lobehub/lint 或按需单独引入；配套 create-lobe-lint CLI 自动检测包管理器与框架（Next.js/Remix/Vite/Expo 等）并写入配置文件，支持 --preset -y 非交互模式供编码 agent 一步执行。面向 JavaScript/TypeScript 项目，本仓库开发需 Node.js 22+ 与 pnpm。

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

- 覆盖 ESLint/Prettier/Stylelint/Commitlint/Remarklint/semantic-release 六类配置
- create-lobe-lint 一条命令完成检测与配置写入
- 支持 Next.js、Remix、Vite、Expo/React Native 等技术栈
- 提供非交互模式与 AGENTS.md，供编码 agent 调用

## 适用场景

- 给团队项目统一 Lint、格式化与 Gitmoji 提交规范
- 在多个 LobeHub 项目间复用同一套代码风格配置
- 让编码 agent 一步完成 lint 配置并自动修复问题

## 场景标签

 · 领域:前端开发工具

## 证据(README 行号)

> L5: Shared ESLint, Prettier, Stylelint, Commitlint, Remarklint and semantic-release configs from LobeHub, plus the `crea
> L31: Lobe Lint is the code style toolkit behind every LobeHub project: one set of ESLint, Prettier, Stylelint, Commitlin

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/lobe-lint 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-30 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f2b34200bf16` · [字段定义](../../DATASET.md)*
