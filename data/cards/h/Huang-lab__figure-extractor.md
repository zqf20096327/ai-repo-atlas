# Huang-lab/figure-extractor

⭐ 18 · Python · 推送 2025-12-29 · [GitHub](https://github.com/Huang-lab/figure-extractor) · 组织维护

**包装 PDFFigures 2.0 的图表提取服务：面向 RAG 流水线**

基于 PDFFigures 2.0 的学术 PDF 图表提取工具，将原引擎包装为模块化 Python 架构：提供 Flask REST API（含限流、请求跟踪、Swagger 文档）、CLI 与 Docker 三种使用方式，输出图表、表格、标题及坐标的 JSON 元数据，处理速度约 1.5 秒/页。支持本地 JVM 直调或远程 API 双模式，附自动环境搭建脚本（Java 11 检测、sbt 构建）。面向文档处理与 RAG 流水线的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提取图表、表格、标题及精确坐标，输出标准化 JSON 元数据
- Flask REST API（限流、请求 UUID 跟踪、Swagger 文档）+ CLI + Docker 三种部署方式
- 本地 JVM 直调或远程 API 双模式执行
- 批量处理整目录 PDF，后台自动清理临时文件

## 适用场景

- 为 RAG 流水线预处理学术 PDF 中的图表与表格
- 批量提取论文图表并获取坐标元数据
- 以 Docker 服务形式部署文档提取 API

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: A high-performance, modernized wrapper for PDFFigures 2.0, designed for seamless integration into modern AI workflow
> L5: This project takes the robust extraction capabilities of the Allen Institute for AI's PDFFigures 2.0 and wraps them 

## 星数曲线

```mermaid
xychart-beta
    title "Huang-lab/figure-extractor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `940fcc3c1483` · [字段定义](../../DATASET.md)*
