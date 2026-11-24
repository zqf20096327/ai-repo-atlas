# ZaraSheven/PaperLens

⭐ 5 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/ZaraSheven/PaperLens) · 个人维护

**给论文阅读者的逐段 PDF 阅读器，支持翻译、问答与笔记**

以段落为锚点的 PDF 论文阅读工具：将 PDF 解析为带坐标的段落块，点击任意块即可查看翻译、向助手提问（以全文为上下文并附带该块）、或将块转为阅读笔记，全部记录存入本地 SQLite，可导出 Markdown。需配置两条 OpenAI 兼容 API 路由（对话模型与翻译模型）。仅支持带文本层的 PDF，扫描件需先行 OCR；检索为关键词方式，未使用嵌入向量。技术栈为 React/TypeScript + FastAPI + PyMuPDF。

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

- 逐段锚定：翻译、问答、笔记均绑定到具体段落块并持久化存储
- 公式/表格/图片以原始裁剪图发送给支持视觉的对话模型
- 关键词检索 + LLM 的本地问答，答案经 SSE 流式返回并用 KaTeX 排版
- 七款内置皮肤，可上传壁纸自动派生明暗模式与主题色

## 适用场景

- 逐段精读长论文时对卡住的段落提问
- 阅读英文论文时查看段落级翻译
- 积累并导出整篇论文的阅读笔记与问答记录

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L22: PaperLens splits a paper into paragraphs and makes every paragraph a place you can come back to.
> L23: Click any block and a bubble opens next to it: read a translation, ask the assistant about that block
> L145: |Q&A|Local keyword retrieval + LLM|The anchored paragraph first, then keyword hits from the whole paper|

## 星数曲线

```mermaid
xychart-beta
    title "ZaraSheven/PaperLens 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-26 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `5fc0ba83a367` · [字段定义](../../DATASET.md)*
