# deepset-ai/haystack-home

⭐ 24 · HTML · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/deepset-ai/haystack-home) · [官网](https://haystack.deepset.ai) · 组织维护

**Haystack 官网仓库：用 Hugo 构建静态网站源码与贡献指南**

deepset-ai 维护的 Haystack（开源 LLM 框架）官方网站的内容仓库，基于 Hugo 静态网站生成器构建。README 面向网站内容贡献者，说明本地构建流程：安装 Hugo、克隆项目并运行 build.sh 安装依赖、在 /content 目录编辑内容、用 hugo server -D 本地预览。教程内容维护在独立的 haystack-tutorials 仓库，合并后随部署更新；另说明重定向配置（vercel.json）、Hugo shortcodes（视频嵌入、按钮、选项卡）、主题编辑（HTML 模板与 Sass）及页面在 sitemap 中排除或隐藏的方法。仓库本体不包含框架代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Hugo 静态网站生成器构建的官网内容仓库
- 教程内容在独立的 haystack-tutorials 仓库维护，通过 PR 贡献
- 通过 vercel.json 配置重定向，支持部署于 Vercel
- 提供视频嵌入、按钮、选项卡等 Hugo shortcodes 用法说明

## 适用场景

- 为 Haystack 官网贡献或修改博客、教程等内容
- 本地预览网站改动效果
- 定制网站主题模板与样式

## 场景标签

 · 领域:LLM 框架/开发者文档

## 证据(README 行号)

> L3: # Haystack
> L5: This Haystack website is built using Hugo, a static website generator written in Go.

## 星数曲线

```mermaid
xychart-beta
    title "deepset-ai/haystack-home 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `445e620622e3` · [字段定义](../../DATASET.md)*
