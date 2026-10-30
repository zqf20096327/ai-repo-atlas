# fangfufu/LLM-book-generator

⭐ 44 · Python · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/fangfufu/LLM-book-generator) · 个人维护

**用 LLM 自动生成整本书的命令行工具，输出 DOCX 手稿**

基于 Python 3.12+ 的命令行工具，通过 llama.cpp server（llama-server）调用 LLM，从初始概念生成完整书籍：标题、章节大纲、小节正文、前后附属内容与营销材料，并输出带自定义样式的 DOCX 文件。支持 LaTeX 数学表达式转图片、缓存 LLM 响应以加速重复运行，通过 config.yaml 配置主题、作者、风格等参数。运行需自备 llama.cpp 服务实例与 LaTeX 发行版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 llama.cpp server 生成书籍全部内容（标题/大纲/正文/前后附属）
- LaTeX 数学表达式渲染为图片并嵌入 DOCX
- 缓存 LLM 响应加速后续运行，config.yaml 配置化
- 同时生成营销材料

## 适用场景

- 自动生成一本主题书稿并得到 DOCX 成品
- 批量产出样书或草稿供后续编辑
- 为新书生成营销文案素材

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: manuscript. It leverages Large Language Models (LLMs) via llama.cpp to generate
> L6: diverse content, including titles, chapter outlines, detailed section text,

## 星数曲线

```mermaid
xychart-beta
    title "fangfufu/LLM-book-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f918ff856429` · [字段定义](../../DATASET.md)*
