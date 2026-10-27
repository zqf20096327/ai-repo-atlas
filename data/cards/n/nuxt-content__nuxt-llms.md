# nuxt-content/nuxt-llms

⭐ 171 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/nuxt-content/nuxt-llms) · 组织维护

**为 Nuxt 应用自动生成 llms.txt 文档的模块**

Nuxt 模块，自动生成并预渲染 /llms.txt 与可选的 /llms-full.txt 路由，按 llms.txt 规范输出结构化 Markdown 文档供人与 LLM 消费。通过 nuxt.config.ts 配置标题、描述、分区与链接，提供 llms:generate 与 llms:generate:llms-full 运行时钩子，供应用或其他 Nuxt 模块动态扩展文档内容。Nuxt Content ^3.2.0 内置集成，可自动将 content 目录内容写入两份文档。以 npm 包分发，MIT 许可。

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

- 自动生成并预渲染 /llms.txt，可选启用 /llms-full.txt
- 运行时钩子系统支持应用与第三方 Nuxt 模块动态扩展文档
- 与 @nuxt/content 内置集成，content 目录内容自动纳入文档
- 分区/链接/notes 均可在 nuxt.config.ts 中配置，支持动态服务替代预渲染

## 适用场景

- 为我的 Nuxt 网站生成 LLM 可读的文档端点
- 把 CMS 或 Nuxt Content 的内容聚合进 llms.txt
- 作为 Nuxt 模块开发者向下游 llms.txt 注入文档章节

## 场景标签

 · 领域:Web 开发/LLM 文档基础设施

## 证据(README 行号)

> L10: Nuxt LLMs automatically generates `llms.txt` markdown documentation for your Nuxt application. It provides runtime 
> L74: The `/llms.txt` route generates a concise, structured documentation that follows the llms.txt specification. This f

## 星数曲线

```mermaid
xychart-beta
    title "nuxt-content/nuxt-llms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 170 --> 172
    line [171, 171]
```

2026-10-18 171 → 2026-10-27 171（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `40065b33091f` · [字段定义](../../DATASET.md)*
