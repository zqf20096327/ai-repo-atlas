# marcusschiesser/vectorstores

⭐ 18 · TypeScript · MIT · 推送 2026-03-16 · [GitHub](https://github.com/marcusschiesser/vectorstores) · [官网](http://vectorstores.org) · 个人维护

**轻量向量数据库框架：统一接口连接数据与 AI 应用**

TypeScript 向量数据库框架，基于 LLamaIndexTS 分叉，聚焦向量数据库场景并提供统一接口。功能覆盖：从多种来源摄取数据、载入向量数据库、后续查询检索；可作为 LLamaIndexTS 的直接替代，包体积 77.5kb (gzip)。支持 Node.js>=20、Deno、Bun、Nitro、Vercel Edge Runtime、Cloudflare Workers 等 JS 环境，可与 Vercel AI SDK 配合使用，通过 @vectorstores/core 及各 provider 包（如 weaviate）以 npm 安装。

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

- 基于 LLamaIndexTS 分叉，可作为其直接替代
- 统一接口完成数据摄取、载入向量库与查询
- 支持多种 JS 运行环境（Node/Deno/Bun/Nitro/Edge/Workers）
- 提供 provider 包体系扩展向量数据库与文件读取器

## 适用场景

- 在 TypeScript 项目中统一接入不同向量数据库
- 为 AI 应用构建数据摄取与检索管线
- 替换现有 LLamaIndexTS 以减小包体积

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L7: Context engineering made easy: Vectorstores provides a unified interface for connecting data to your AI application.
> L13: It's based on a fork of LLamaIndexTS, so you can use it as a drop-in replacement for LLamaIndexTS in your existing 

## 星数曲线

```mermaid
xychart-beta
    title "marcusschiesser/vectorstores 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7530d3321b92` · [字段定义](../../DATASET.md)*
