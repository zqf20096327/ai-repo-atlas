# frankbria/auto-author

⭐ 13 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/frankbria/auto-author) · 个人维护

**面向长篇非虚构写作者的 AI 图书创作平台**

Auto Author 是一个自托管的全栈 Web 应用：用户输入书籍摘要（文字或语音），AI 生成层级式目录；随后以逐章问答方式收集内容（支持语音输入），再由 AI 从问答内容生成多种写作风格的章节草稿；提供 TipTap 富文本编辑、自动保存（3 秒防抖 + localStorage 备份）以及 PDF/DOCX/EPUB/Markdown 导出。技术栈为 Next.js + FastAPI + MongoDB，认证用 better-auth，AI 集成为 OpenAI（或本地 LLM，README 未给出本地运行时具体配置）。需自行部署前后端并配置 OPENAI_API_KEY。

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

- 摘要→AI 目录生成→逐章问答→AI 草稿生成的写作工作流
- Web Speech API 语音输入与多写作风格草稿生成
- PDF/DOCX/EPUB/Markdown 可定制导出
- better-auth 认证、WCAG 2.1 可访问性与 CI 强制 85% 覆盖率门槛

## 适用场景

- 从概念出发，通过问答和语音口述逐章成稿写非虚构书
- 管理书籍、章节与草稿并在完成后导出多种格式
- 多人各自账户独立管理写作项目

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: **Auto Author** is an AI-powered application designed to help users write long-form non-fiction books. It streamline
> L13: * 📝 **AI draft generation** from Q&A responses with multiple writing styles

## 星数曲线

```mermaid
xychart-beta
    title "frankbria/auto-author 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `43ae1e104868` · [字段定义](../../DATASET.md)*
