# devdezzies/neocode

⭐ 19 · TypeScript · 推送 2026-03-16 · [GitHub](https://github.com/devdezzies/neocode) · [官网](https://neocode-one.vercel.app) · 个人维护

**用单条提示词驱动 AI agent 生成网站的建站工具**

开源网站构建器，通过 AI agent 在 E2B 沙箱环境中从零生成网站：用户给出单条提示词，系统调用多个 LLM 进行代码生成与任务总结，基于预装的 NextJS 模板产出站点。技术栈为 NextJS、TypeScript、tRPC、Postgres、Prisma、Tailwind、Vercel，集成 Clerk 计费。运行前需自备 git、NodeJS/NPM、E2B、Gemini API key、Neon 数据库 URL 与 Clerk 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条提示词从零生成完整网站
- E2B 沙箱环境运行预装 NextJS 模板
- 多个 LLM 分别负责代码生成与任务总结
- 集成 Clerk 计费与 Neon 数据库

## 适用场景

- 不懂前端开发也想用一句话生成网站
- 快速搭建 NextJS 技术栈的站点原型
- 作为带计费的可部署 SaaS 模板二次开发

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3:  NeoCode is a website builder powered by AI agents for building website only using single prompt. NeoCode utilizes s
> L4:  Currently, NeoCode is capable of building a website from scratch using pre-installed NextJS template in a sandbox e

## 星数曲线

```mermaid
xychart-beta
    title "devdezzies/neocode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `61e32af97769` · [字段定义](../../DATASET.md)*
