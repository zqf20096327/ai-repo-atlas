# midspiral/lemmafit

⭐ 67 · JavaScript · MIT · 推送 2026-06-02 · [GitHub](https://github.com/midspiral/lemmafit) · [官网](https://lemmafit.com) · 组织维护

**让 AI agent 用 Dafny 形式化验证代码并编译为 TypeScript**

面向使用 Claude Code 的开发者的开发工作流工具：业务逻辑、状态机等以 Dafny 编写，由守护进程调用 dafny verify 做数学验证，验证通过后自动编译为 TypeScript（.cjs/.ts）接入 React 应用；通过 `/guarantees` 技能（需 claimcheck）生成保障报告。提供 CLI（init/add/sync/daemon/logs），npm 全局安装时自动下载 Dafny 与 dafny2js。当前面向绿地项目与 Claude Code 优化，未来计划支持其他语言与 agent 无关化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Dafny 形式化验证通过后自动编译为 TypeScript
- 守护进程监听 .dfy 文件并运行 dafny verify
- 提供 init/add/sync/daemon 等 CLI 命令
- npm 安装时自动下载 Dafny 与 dafny2js 到 ~/.lemmafit/

## 适用场景

- 让 Claude Code 生成的业务逻辑经过数学验证再接入应用
- 绿地项目中以 Dafny 编写并验证状态机等核心逻辑
- 为已验证项目生成 guarantees 保障报告

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: Lemmafit integrates Dafny formal verification into your development workflow via Claude Code. Business logic, state 
> L31: 3. The **daemon** watches `.dfy` files, runs `dafny verify`, and on success compiles to `src/dafny/Domain.cjs` + `s

## 星数曲线

```mermaid
xychart-beta
    title "midspiral/lemmafit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-26 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `60826a80c6d5` · [字段定义](../../DATASET.md)*
