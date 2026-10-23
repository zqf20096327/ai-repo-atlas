# Shannon-Data/ShannonBase

⭐ 199 · C++ · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/Shannon-Data/ShannonBase) · [官网](https://www.shannonbase.org) · 组织维护 · 中文 README

**面向 AI 的 MySQL 兼容数据库：SQL 内完成训练/推理/向量检索/RAG/Agent**

基于 MySQL 8.0 扩展的 HTAP 数据库，行存 InnoDB 与内存列存 Rapid 通过 Redo Log 双通道同步，按代价与 ML 算法自动路由查询。AI 能力嵌入数据库进程内：内置 LightGBM/XGBoost 训练与预测存储过程、原生 VECTOR 类型与距离函数、嵌入 ONNX Runtime 本地运行 Llama/Qwen/DeepSeek 等模型、sys.ML_RAG 一条 SQL 完成 RAG，另有 JerryScript JavaScript 存储过程与内置 Agent 执行框架。MySQL 线协议兼容，现有驱动/ORM 可直接使用。提供 Docker 镜像与源码编译（需 Boost）两种安装方式；Lakehouse/Parquet 查询标注为企业版功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程内 ML 运行时：ML_TRAIN/ML_PREDICT_ROW 直接在库内训练预测，无 ETL
- 嵌入 ONNX Runtime，本地运行 Llama/Qwen/DeepSeek 等 ONNX 模型
- sys.ML_RAG 一条 SQL 完成 embed/索引/检索/生成
- InnoDB + Rapid 内存列存的 HTAP 架构，Redo Log 实时同步

## 适用场景

- 在 MySQL 协议内直接做向量检索与 RAG，免去独立向量库部署
- 用 SQL 在活数据上训练/预测 ML 模型，替代导出-训练-导入流程
- 本地运行 LLM 推理并用 SQL 定义执行 Agent

## 场景标签

`RAG` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L13:  **Train ML models. Run LLMs. Search vectors. Build RAG pipelines. Run Native-Agent or User-defined Agents.
> L86: |🤖 **LLM / ONNX Runtime**|Run Llama, Qwen, DeepSeek, MiniLM and more **locally inside the DB** via embedded ONNX Ru
> L98: ShannonBase: The Next-Gen Database for AI—an infrastructure designed for big data and AI. As the MySQL of the AI er

## 星数曲线

```mermaid
xychart-beta
    title "Shannon-Data/ShannonBase 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 193 --> 200
    line [194, 196, 198, 199]
```

2026-10-18 194 → 2026-10-23 199（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8fbfa88eedd2` · [字段定义](../../DATASET.md)*
