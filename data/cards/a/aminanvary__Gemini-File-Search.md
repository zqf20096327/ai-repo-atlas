# aminanvary/Gemini-File-Search

⭐ 30 · TypeScript · MIT · 推送 2025-12-26 · [GitHub](https://github.com/aminanvary/Gemini-File-Search) · [官网](https://ai.google.dev/gemini-api/docs/file-search) · 个人维护

**给普通用户的 Gemini File Search 可视化界面：管理文件库并对话**

基于 Next.js 16 与 Bun 构建的 Web 界面，封装 Google Gemini File Search API：创建/查看/删除文件库（library）、拖拽上传文件、与文档对话、切换 Gemini 2.5 Flash 与 Gemini 3 Flash 模型，并展示回答引用的来源文档。面向不想写代码或 curl 命令、需要直接操作 Gemini 文件搜索功能的用户。本地运行需安装 Bun、自备 Gemini API key（Google AI Studio 免费获取），通过 git clone、bun install、bun dev 三步启动，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件库的创建/查看/删除与拖拽导入文件
- 基于 Gemini 的文档问答并展示来源引用
- 支持 Gemini 2.5 Flash 与 Gemini 3 Flash 模型切换
- 本地三步启动（clone / bun install / bun dev）

## 适用场景

- 不写代码直接管理 Gemini 上传的文件与文件库
- 上传文档后通过界面与其问答并查看引用来源
- 需要一个替代 curl 命令的 Gemini File Search 操作入口

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L37: - 💬 **Chat with Documents** — Ask questions about your files using Gemini AI
> L87: - **AI SDK:** @google/genai

## 星数曲线

```mermaid
xychart-beta
    title "aminanvary/Gemini-File-Search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `82cf0ad4cbe8` · [字段定义](../../DATASET.md)*
