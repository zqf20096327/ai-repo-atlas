# yohanvillarp/metamorph

⭐ 20 · TypeScript · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/yohanvillarp/metamorph) · [官网](https://metamorph.nikelyh.tech/) · 个人维护

**多 Agent 编排的代码/框架自动迁移 CLI 工具**

基于 npm 全局安装的 TypeScript CLI，用 Mapper/Worker/Reviewer/PackageManager 等多个自主 Agent 对代码库做语义级重构与框架迁移，替代正则或手工 AST 改写。核心机制：项目智能引擎（PIE）自动映射 monorepo 结构、多态包管理引擎适配 npm/pnpm/yarn/bun、文件变更先在影子工作区沙箱内编译验证再由用户审阅应用，另有 React 实时监控面板、token 成本统计与 --mock 离线模式。前端支持 Vue/Svelte/Angular、后端支持 Express/Fastify/NestJS/Hono 等迁移目标。限制：迁移目录列表需查外部文档，本地开发需 Node.js≥20 并配置 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mapper/Worker/Reviewer/PackageManager 多 Agent 协作完成语义级迁移
- 影子工作区沙箱：变更先编译验证，原代码在审阅应用前不被修改
- 支持 monorepo（Turborepo/pnpm/npm/yarn workspaces/Lerna）与多包管理器（含 bun）
- --mock 离线零成本迁移与 --dry-run 迁移预览
- React 实时面板监控 Agent 操作、成本与差异

## 适用场景

- 把项目从旧框架自动迁移到新框架（如前端 Vue/Svelte/Angular、后端 Express/NestJS 目标）
- 在大型 monorepo 中自动化架构调整与依赖升级
- 先预览迁移计划与包变更再决定是否应用
- 离线模拟迁移流程以评估方案

## 场景标签

 · 领域:软件开发/代码迁移

## 证据(README 行号)

> L26: **Metamorph** is an advanced CLI tool designed to completely automate complex architectural shifts and framework mi
> L31: - **Deterministic Mock LLM Provider**: Offline $0.00 migrations simulating token metrics with zero external API cre

## 星数曲线

```mermaid
xychart-beta
    title "yohanvillarp/metamorph 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-23 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `349bb8213a55` · [字段定义](../../DATASET.md)*
