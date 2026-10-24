# ThinkEx-OSS/thinkex

⭐ 55 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/ThinkEx-OSS/thinkex) · [官网](https://thinkex.app) · 组织维护

**面向研究学习的源材料工作台：文档与 AI 对话并排**

ThinkEx 是一个面向源材料密集型学习与研究的全栈 TypeScript 工作台：在界面中同时打开 PDF、文档、图片与文件夹，手动选择作为 AI 上下文的材料，并与协作者共享工作区；区别于把文件上传进聊天窗口的模式，来源保持可排列、可编辑。后端运行在 Cloudflare Workers（Durable Objects、R2、Workers AI 等），前端使用 React 19 与 Tiptap 协同编辑。MIT 许可，可从仓库本地运行；生产自部署需部署到自有 Cloudflare 账号，暂不支持 Docker/VPS，安装路径尚未官方化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PDF/文档/图片/文件夹在工作区内打开并与 AI 对话并排
- 用户手动选择供 AI 使用的上下文材料
- 支持协作者共享工作区与协同文档（Tiptap/Yjs）
- 基于 Cloudflare Workers 的全栈架构，MIT 许可可自部署

## 适用场景

- 读论文或比较多份资料时对指定材料提问
- 整理研究资料并与协作伙伴共享工作区
- 在网盘式文件与 AI 对话之间建立联动的工作流

## 场景标签

`知识库管理` `文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L16: Instead of uploading sources into a chat, you keep the actual materials in view: PDFs, docs, images, folders, and A
> L20: - Ask AI about the specific items you choose.
> L34: ThinkEx is a full-stack TypeScript app hosted on Cloudflare. The frontend is React, TanStack Start, Tailwind CSS, T

## 星数曲线

```mermaid
xychart-beta
    title "ThinkEx-OSS/thinkex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-24 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a6e7eb6353e3` · [字段定义](../../DATASET.md)*
