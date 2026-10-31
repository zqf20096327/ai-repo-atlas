# xoryouyou/bsi-technical-guidelines-markdown

⭐ 18 · Python · 推送 2026-10-02 · [GitHub](https://github.com/xoryouyou/bsi-technical-guidelines-markdown) · 个人维护

**BSI 技术指南 PDF 转 Markdown 的文档库与同步转换工具**

将德国联邦信息安全局（BSI）发布的全部技术指南（TR）与 IT-Grundschutz 模块集中到一个仓库，内容不改写、保留原版权声明，仅做 PDF 到 Markdown 的格式转换，便于全文检索和在 Obsidian 等工具中使用。附带 Python 脚本（基于 uv 环境管理）：scraper.py 抓取 PDF 链接并按校验和做版本历史同步，convert.py 用 pymupdf4llm 批量转换为 Markdown 并抽取图片；此前尝试过 marker、docling、mineru 等方案。

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

- 集中收录 BSI TR 与 IT-Grundschutz 文档（PDF+Markdown 双格式）
- 基于校验和的本地同步与版本历史追踪
- pymupdf4llm 批量转换并抽取图片

## 适用场景

- 在 Obsidian 等工具中检索和引用 BSI 技术指南
- 本地镜像 BSI 文档并跟踪版本更新
- 获取文本化的德国信息安全标准用于搜索与处理

## 场景标签

`文档解析` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L6: This repository contains all BSI technical guidelines (TRs) which are published here.
> L8: It was created out of necessity to provide all BSI TRs at a single location which can be adapted arbitrarily for the

## 星数曲线

```mermaid
xychart-beta
    title "xoryouyou/bsi-technical-guidelines-markdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e09d4b5ce398` · [字段定义](../../DATASET.md)*
