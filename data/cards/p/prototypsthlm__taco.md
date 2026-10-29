# prototypsthlm/taco

⭐ 32 · Svelte · MIT · 推送 2026-06-18 · [GitHub](https://github.com/prototypsthlm/taco) · [官网](https://www.tacoai.app) · 组织维护

**团队共享 API key 的 ChatGPT 开源前端（SvelteKit）**

基于 SvelteKit 构建的 ChatGPT 开源前端，面向需要团队协作使用 AI 聊天功能的组织：成员共享同一个 API key 即可访问聊天界面。后端数据层用 Prisma + PostgreSQL（通过 Docker Compose 启动数据库并执行迁移），界面用 Tailwind UI 与 Headless UI 的 Svelte 移植版，支持 class 式暗色模式切换，邮件功能通过 Postmark 发送。提供开发、构建与 Playwright E2E 测试流程，需要 Node.js 16+ 与 Docker 环境，自行部署使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 团队共享单一 API key 访问 AI 聊天
- Prisma + PostgreSQL 数据层，Docker Compose 启动数据库
- Tailwind UI + class 式暗色模式
- Playwright E2E 测试与 Prisma Studio 数据库视图

## 适用场景

- 团队或组织统一部署一个共享的 ChatGPT 聊天入口
- 通过共享 API key 控制成员的 AI 聊天访问
- 基于 SvelteKit 代码库二次开发自己的聊天前端

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: TACO is an open-source frontend for ChatGPT built with SvelteKit that allows teams to collaborate effectively by sha
> L142: Taco is maintained by Prototyp, a code lab building digital products for businesses breaking new ground.

## 星数曲线

```mermaid
xychart-beta
    title "prototypsthlm/taco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `df114790200d` · [字段定义](../../DATASET.md)*
