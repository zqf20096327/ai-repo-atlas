# bke-daniel/next-llms-txt

⭐ 15 · TypeScript · 推送 2026-10-07 · [GitHub](https://github.com/bke-daniel/next-llms-txt) · [官网](https://next-llms-txt-website.vercel.app) · 个人维护

**Next.js 生成 LLM 优化文档（llms.txt）的工具库**

next-llms-txt 生态的 monorepo，主包为发布到 npm 的 Next.js 插件（当前版本 3.0），用于生成面向 LLM 的优化文档；仓库还包含 App Router 测试服务器、演示 Next.js 应用与 Cypress E2E 测试套件，通过 npm workspaces 管理。要求 Node.js 22 或更新版本（.nvmrc 固定 24）与 npm，构建后以测试服务器与演示应用验证插件行为；发布流程为本地机器手动执行，CI 中无发布工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- npm 发布的 Next.js 插件库，当前版本 3.0
- 含演示应用与 Cypress E2E 集成测试
- npm workspaces 管理多包，支持 TypeScript 5.9/6.0/7.0 类型检查

## 适用场景

- 在 Next.js 站点中生成 LLM 优化文档
- 查看插件用法的演示应用
- 基于测试服务器验证 llms.txt 输出

## 场景标签

 · 领域:Web 开发工具/LLM 文档

## 证据(README 行号)

> L79: The main library package, currently at version 3.0. See packages/next-llms-txt/README.md for the documentation, UPG
> L83: A Next.js application demonstrating the plugin in action.

## 星数曲线

```mermaid
xychart-beta
    title "bke-daniel/next-llms-txt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `19ea7a3c204f` · [字段定义](../../DATASET.md)*
