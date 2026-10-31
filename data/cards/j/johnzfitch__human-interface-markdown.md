# johnzfitch/human-interface-markdown

⭐ 18 · 推送 2026-03-27 · [GitHub](https://github.com/johnzfitch/human-interface-markdown) · 个人维护

**Apple 人机界面指南历史档案库：35 份文档的 LLM 就绪化数据集**

收录 1980-2014 年间 35 份 Apple 官方人机界面指南文档（Lisa、Mac、NeXT、Newton、Aqua、iOS 时代），转换为带语义分块（4,507 个 RAG 优化块）、嵌入原图与 SHA256 校验的 Markdown。实现 llms.txt 标准：提供 curl 可取的发现索引 llms.txt、全量拼接文件 llms-full.txt（约 15MB）及逐份文档目录。内容经 Marker 与 GPT-4 Vision 从官方 PDF 提取。原文版权归 Apple（研究/教育目的），仓库组织部分 MIT 许可。适合 LLM 检索、设计史研究与设计教学。

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

- 35 份 Apple HIG 文档覆盖 1980-2014 共 34 年
- 11,655 个 Markdown 文件与 4,507 个语义分块（RAG 优化）
- 实现 llms.txt 标准，提供发现索引与全量拼接文件
- SHA256 完整性校验与原文图片嵌入

## 适用场景

- 为 RAG 管线或 LLM 提供 Apple 设计规范的历史语料
- 研究 GUI/HCI 设计范式的跨年代演变
- 做复古或时代风格应用时查阅原始界面规范
- 设计课程中引用一手界面设计文档

## 场景标签

 · 领域:设计规范/知识档案

## 证据(README 行号)

> L16: This repository preserves **35 historical documents** that defined how millions of people interact with computers. 
> L219: This repository implements the llms.txt standard for optimal LLM discoverability.

## 星数曲线

```mermaid
xychart-beta
    title "johnzfitch/human-interface-markdown 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aec136c093cc` · [字段定义](../../DATASET.md)*
