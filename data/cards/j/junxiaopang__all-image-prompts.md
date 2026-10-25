# junxiaopang/all-image-prompts

⭐ 65 · TypeScript · 推送 2026-08-06 · [GitHub](https://github.com/junxiaopang/all-image-prompts) · [官网](https://prompts.kkkm.cn/) · 个人维护 · 中文 README

**多模型 AI 绘画提示词的展示与管理平台**

基于 React 19 + Vite 6 + TypeScript 构建的提示词展示网站，汇集 Gemini(NanoBanana)、Midjourney、DALL-E 3、Flux、Grok、Seedream 等多个文生图模型的提示词，数据以 JSON 文件存储并与视图分离。提供按模型分类、多选标签过滤、全局搜索、一键复制、深色模式与中英文界面。支持 Fork 后经 Vercel 或腾讯云 EdgeOne 一键部署，本地运行需 Node.js v18+ 与 pnpm，可向 src/data 添加提示词或新模型映射。提示词来源于网上收集，提供在线预览站点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 汇集 Gemini/Midjourney/DALL-E 3/Flux/Grok/Seedream 等多模型提示词
- 按模型分类、多选标签过滤与标题/内容/标签全局搜索
- 数据存于 src/data 的 JSON 文件，数据与视图分离，可自行添加条目与新模型
- 支持 Vercel 与腾讯云 EdgeOne Pages 一键部署

## 适用场景

- 浏览各文生图模型的提示词寻找创作灵感
- 按模型或标签筛选并一键复制提示词
- Fork 后自建提示词站点并贡献新提示词

## 场景标签

`提示工程` `精选清单` · 领域:Agent 开发

## 证据(README 行号)

> L5: 这是一个基于 **React 19** + **Vite 6** 构建的现代化 AI 绘画提示词展示与管理平台。它汇集了来自**Gemini** (NanoBanana) 、**Midjourney**、**DALL-E 3**、*
> L39: - **🤖 多模型支持**：完整支持并分类展示 Midjourney, DALL-E, GPT-4o, Flux, Grok, Gemini(Nano Bananan), Seedream 等多种模型的提示词。
> L117: 本项目的核心数据存储在 `src/data/` 目录下的 JSON 文件中，实现了数据与视图的分离。

## 星数曲线

```mermaid
xychart-beta
    title "junxiaopang/all-image-prompts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-25 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `20c5be8d43c5` · [字段定义](../../DATASET.md)*
