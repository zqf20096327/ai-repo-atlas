# oliveiracarlosadv/Lex-Vade-Mecum

⭐ 4 · HTML · CC-BY-4.0 · 推送 2026-11-25 · [GitHub](https://github.com/oliveiracarlosadv/Lex-Vade-Mecum) · 个人维护

**面向 AI 与 RAG 使用场景的巴西法律 Markdown 语料库**

将巴西官方法律文本（Planalto 官方门户）提取为 Markdown 文件，每部法律按统一结构组织：元数据、结构化正文、逐条解读、关键词与 RAG 索引元数据。脚本自动切分章节条款，发布前逐条校验与官方文本一致，并每 12 小时重新比对官方来源自动更新。提供 GitHub Pages 在线阅读页（搜索、标注、阅读进度、可安装为应用），并说明在 Claude Projects 中加载文件及按 `### Art.` 标题切分用于向量检索/RAG 的用法。面向法律从业者和使用 LLM 处理巴西法的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 法律 Markdown 文件含逐条解读与 RAG 索引元数据，按 `### Art.` 结构支持向量切分
- 每 12 小时自动与官方来源比对更新，发布前逐条校验与 Planalto 文本一致
- 配套 GitHub Pages 在线阅读页：搜索、四色标注、阅读进度、备份导入
- 每 12 小时自动与官方来源比对更新

## 适用场景

- 把法律文件加入 Claude Projects 作为知识来源
- 对巴西法律条文做 RAG 检索与语义搜索
- 在线查阅、标注和分享现行有效的巴西法律

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3:  Leis brasileiras em Markdown, fiéis ao texto oficial e prontas para IA.
> L7: Biblioteca de leis brasileiras em Markdown, extraídas do texto oficial publicado no Portal da Legislação do Planalto
> L89: - **Indexação vetorial (RAG):** divida os trechos pelos títulos `### Art.`. Cada artigo traz sua localização, o tex

## 星数曲线

```mermaid
xychart-beta
    title "oliveiracarlosadv/Lex-Vade-Mecum 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4]
```

2026-11-26 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `f84887f32389` · [字段定义](../../DATASET.md)*
