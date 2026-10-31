# fabricioctelles/astro-webmcp

⭐ 19 · TypeScript · MIT · 推送 2026-09-19 · [GitHub](https://github.com/fabricioctelles/astro-webmcp) · [官网](https://www.npmjs.com/package/astro-webmcp) · 个人维护

**Astro 集成：一行代码让站点内容通过 WebMCP 暴露给 AI agent**

面向 Astro 站点开发者的集成插件：安装后在构建时生成静态 manifest JSON，客户端脚本在每个页面检测 document.modelContext 并注册 search_content、list_sections、go_to、get_page_info 四个内置工具，使 AI agent 可直接发现、搜索和导航站点内容。支持三种搜索后端（manifest/pagefind/orama）、自定义工具、跨域 exposedTo 控制与提示注入清洗。要求 Chrome 149+（flag 或 origin trial），Edge 支持尚未落地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 构建时生成静态 manifest，客户端注册 4 个内置工具
- search_content 支持 manifest/pagefind/orama 三种后端并自动回退
- 安全选项：跨域 exposedTo 白名单、输出长度限制、提示注入清洗
- 支持自定义工具与 readOnlyHint/consequentialHint 等工具注解

## 适用场景

- 让博客或文档站的 AI agent 直接搜索与导航内容
- 为站点内容声明结构化工具供浏览器内 agent 调用
- 在表单上叠加 Declarative API 让 agent 填写提交

## 场景标签

 · 领域:Web/AI agent 基础设施

## 证据(README 行号)

> L12: Astro integration that automatically exposes your site's content via WebMCP — allowing AI agents to discover, searc
> L16: WebMCP is a proposed web standard by Chrome that lets websites declare structured "tools" for AI agents. Instead of

## 星数曲线

```mermaid
xychart-beta
    title "fabricioctelles/astro-webmcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5272c3bb15b8` · [字段定义](../../DATASET.md)*
