# mmTheBest/arxie

⭐ 114 · Python · MIT · 推送 2026-06-17 · [GitHub](https://github.com/mmTheBest/arxie) · [官网](https://github.com/mmTheBest/arxie) · 个人维护

**面向科研者的文献扎根 AI 助手：综述/基准/批判生成**

自托管的科研支持应用：导入个人论文库 PDF，解析全文/图表/表格并抽取研究信号，在 Study 中固定关键论文并附加草稿、代码、结果文件等自有材料，随后生成 11 类研究产物（文献综述、论文对比、领域模式、基准计划、实验计划、假设、批判、假设图、实验待办、修改计划等）。默认单用户本地运行，arxie-local 启动 PostgreSQL/MinIO/Redis/API/worker，可选 Elasticsearch 检索；需 Python 3.10+ 与 Docker。项目自述处于活跃开发期，产物质量与部署流程仍在改进。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PDF 论文解析与全文/图表/表格证据抽取
- 11 类研究产物生成（综述/对比/基准计划/批判/假设等）
- Study 可挂载草稿路径、代码路径、结果文件与文本笔记作为上下文
- arxie-local 一键启动本地栈，支持双击快捷方式

## 适用场景

- 为新方法设计实验前整理领域基线、数据集与消融清单
- 检查我的草稿哪些声明缺乏文献支撑
- 在多条会话间维持项目专属的阅读与证据上下文

## 场景标签

`科研工具` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: Most AI assistants become shallow when the question depends on a specialized literature. They can summarize a paper,
> L51: Arxie currently supports these research artifact types:

## 星数曲线

```mermaid
xychart-beta
    title "mmTheBest/arxie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-29 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5fed9e5c6bb3` · [字段定义](../../DATASET.md)*
