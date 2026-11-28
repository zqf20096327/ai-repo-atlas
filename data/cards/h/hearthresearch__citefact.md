# hearthresearch/citefact

⭐ 10 · Python · MIT · 推送 2026-09-15 · [GitHub](https://github.com/hearthresearch/citefact) · [官网](https://pypi.org/project/citefact/) · 组织维护

**面向研究者的引文审计工具：核验引用与原文献是否相符**

对 Markdown 手稿与其所引来源全文做三层检查：引文是否存在于书目中、直接引用是否逐字出现在原文、来源是否实际支持所述论断。前两层为确定性检查，免费且可离线运行；论断层由用户自备 key 的 LLM 逐条判定并附逐字证据。通过 Zotero 本地 API 读取文献与 PDF，或使用 BibTeX 加 PDF 目录；PDF 经 Docling 转换并按内容哈希缓存。输出单文件 HTML 报告与供 CI 使用的 JSON，以退出码支持流水线门禁。仅支持 APA 式作者-年份引用与 Markdown 手稿。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层检查：引文存在性、逐字引用比对、论断支持性判定
- 无 key 离线模式可完成引文与引用检查
- 支持 Anthropic、OpenAI 或经 Ollama 本地运行 LLM
- 单文件 HTML 报告附逐字证据与逐词 diff

## 适用场景

- 提交或评审前核查手稿是否存在编造引文与改动引用
- CI 流水线中以退出码门禁论文仓库的引用合规
- 核对论断是否被所引文献实际支持

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: LLMs made it trivial to produce manuscripts with fabricated citations, altered quotes, and claims the cited sources
> L67: 3. **Check** - citations and quotes are verified deterministically; claims are extracted verbatim and judged per (c
> L168: - Author-year (APA-like) citation styles only; numeric styles (Vancouver/IEEE) are on the roadmap


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `888b66b63926` · [字段定义](../../DATASET.md)*
