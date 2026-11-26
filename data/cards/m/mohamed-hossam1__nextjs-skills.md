# mohamed-hossam1/nextjs-skills

⭐ 10 · JavaScript · MIT · 推送 2026-05-30 · [GitHub](https://github.com/mohamed-hossam1/nextjs-skills) · 个人维护

**为 Next.js 工作流提供 agent 技能的仓库**

面向编码 agent 的 Next.js 技能集合，含两个技能：nextjs-cache-architecture 覆盖 App Router 项目的缓存架构设计（tag 注册表、缓存边界、revalidation 工具、过期数据调试），并附带静态审计脚本验证清单项；next-action-handler 基于 next-safe-action 和 zod 规范化 server actions（输入/输出校验、错误归一、auth 上下文、pino 日志）。通过 npx skills add 安装，要求 Next.js 16+ 与 App Router，不支持 Pages Router、Edge runtime 与静态导出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- nextjs-cache-architecture：App Router 缓存架构设计与过期数据调试
- 附带静态审计脚本 audit.mjs 验证实现
- next-action-handler：统一 server actions 的校验、错误处理与日志
- 通过 npx skills add 一条命令安装单个技能

## 适用场景

- 让编码 agent 按 SKILL.md 实现 Next.js 16+ App Router 缓存架构
- 为 server actions 项目统一接入输入校验与错误归一
- 应用技能后运行审计脚本检查清单项落实情况

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A collection of agent skills for Next.js workflows. The repository
> L23: │   ├── SKILL.md                                # Always-loaded core: architecture + steps + common mistakes

## 星数曲线

```mermaid
xychart-beta
    title "mohamed-hossam1/nextjs-skills 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `c9b326256343` · [字段定义](../../DATASET.md)*
