# gianlucamazza/ragfs

⭐ 14 · Rust · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/gianlucamazza/ragfs) · [官网](https://gianlucamazza.github.io/ragfs/) · 个人维护

**面向 LLM agent 的 FUSE 文件系统：结构化文件操作与本地语义搜索**

用 Rust 实现的 Linux FUSE 文件系统，供 LLM agent 通过 .ragfs/.ops/、.safety/、.semantic/ 目录执行结构化文件操作：创建等操作返回带 undo_id 的 JSON 结果，支持软删除与撤销及审计日志。语义搜索在本地完成：文件抽取文本后分块、用 gte-small（384 维，经 Candle 本地推理）嵌入、存入 LanceDB 后查询，首次运行需下载模型（约 67–100 MB）。支持 PDF、图片、OOXML 等格式抽取。限制：仅 Linux，macOS 不支持；向量检索在索引达 256 块前为精确扫描；默认抽取器跳过 .doc/RTF/EPUB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 通过 .ops/ 目录执行文件操作并获取带 undo_id 的 JSON 反馈
- 软删除、撤销与审计日志机制
- 本地语义搜索：gte-small 嵌入 + LanceDB，处理全程在本机
- 混合检索（向量+FTS）与函数/类签名级代码分块

## 适用场景

- 让 LLM agent 以结构化、可撤销的方式操作文件
- 对本地文档做语义搜索与混合检索
- 为代码库建立函数级索引并按语义查询

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L12: Agentic FUSE filesystem for LLM agents: structured file ops with JSON feedback, soft-delete and undo, audit logging
> L56: |**Agents**|`.ops/` JSON ops, `.safety/` trash + undo|Python bindings, MCP server|

## 星数曲线

```mermaid
xychart-beta
    title "gianlucamazza/ragfs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `5e1b9b937347` · [字段定义](../../DATASET.md)*
