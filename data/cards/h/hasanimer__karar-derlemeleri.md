# hasanimer/karar-derlemeleri

⭐ 4 · Python · 推送 2026-11-27 · [GitHub](https://github.com/hasanimer/karar-derlemeleri) · 个人维护

**面向 AI/RAG 的土耳其判例汇编数据集（35 册，约13.4万条判决）**

将 Av. Hakan Dimdik 在 X 上分享的土耳其上诉法院（Yargıtay/BAM/Danıştay）判例汇编 PDF 转换为 Markdown 与 JSONL 结构化数据：35 个汇编、66,332 页、约 134,000 条判决引证，按债法、不动产、家事继承、执行破产、赔偿、劳动、调解仲裁等主题组织。提供按主题分文件夹的 md 文件、供 NotebookLM/ChatGPT/Claude Projects 上传的分卷生成脚本与指令模板、每判决一条记录的 JSONL 数据，以及 shell 检索脚本和转换可复现流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35 个判例汇编约 134,000 条判决引证，按法律主题分类组织
- 提供 md/、分卷上传文件与 JSONL（每判决一条记录）三种数据形态
- 转换结果经第二提取引擎逐字符比对验证，34 册完全匹配
- 内置 Türkçe 字符不区分的检索脚本 ara.py

## 适用场景

- 为土耳其法律检索类 RAG 系统提供判决语料
- 把汇编分卷上传到 ChatGPT/Claude Projects/NotebookLM 做法律问答
- 在 Obsidian 或代码助手中按主题阅读与检索判例
- 对土耳其判例做数据分析研究

## 场景标签

`RAG` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: **35 derleme · 66.332 sayfa · yaklaşık 134 bin karar künyesi.** İndirme ve dönüştürme tarihi: 27.11.2026.
> L19: |Veri|`veri/kararlar/<kod>.jsonl.gz`: karar başına bir kayıt; veri/README.md|Geliştiriciler (RAG, analiz)|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `dec058aedd10` · [字段定义](../../DATASET.md)*
