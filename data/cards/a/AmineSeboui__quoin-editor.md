# AmineSeboui/quoin-editor

⭐ 4 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/AmineSeboui/quoin-editor) · [官网](https://quoincloud.com) · 个人维护

**React 的 Notion 风格 Markdown 块编辑器组件库**

为 React 提供的富文本块编辑器组件：文本块以 markdown 形式存于受控的 QuoinBlock[] 数组中，通过 blocks/onChange 与应用状态交互。内置斜杠菜单、拖拽手柄、气泡工具栏、快捷键与无障碍支持（CI 中 axe 测试）。协作通过应用自带的 Yjs provider 同步；AI 功能由调用方传入模型输出流写入文档，Quoin 本身不调用模型。npm 安装，支持按入口拆分的可选功能包与七种语言包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档以 markdown 块数组存储，可直接保存、git diff 或交给 LLM
- 实时协作经由调用方自备的 Yjs provider，评论线程锚定文本
- AI 流式写入文档，由调用方提供模型流，产品本身不调用模型
- 多入口可选功能：表格/公式/图表/目录/导出 docx/pdf 等

## 适用场景

- 在 React 应用中嵌入 Notion 风格的块编辑器
- 团队文档协作编辑并保留 markdown 源文件进版本库
- 为编辑器接入自有模型的改写/续写/翻译能力

## 场景标签

 · 领域:开发者工具/编辑器组件

## 证据(README 行号)

> L5: Quoin is a rich markdown editor and block editor for React. Every text block stays readable markdown inside a typed 
> L27: **AI that writes into the document.** Select text and ask AI to fix, rewrite, shorten, translate or continue it. Th

## 星数曲线

```mermaid
xychart-beta
    title "AmineSeboui/quoin-editor 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-12", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9d435dd0fa64` · [字段定义](../../DATASET.md)*
