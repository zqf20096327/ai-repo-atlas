# bentoml/BentoSentenceTransformers

⭐ 15 · Python · 推送 2026-07-14 · [GitHub](https://github.com/bentoml/BentoSentenceTransformers) · 组织维护

**BentoML 示例工程：用 SentenceTransformers 构建句向量推理 API**

BentoML 官方示例项目，演示如何将 SentenceTransformers 模型（all-MiniLM-L6-v2）封装为句嵌入推理 API 服务。克隆仓库并 pip 安装依赖后，通过 bentoml serve 启动 HTTP 服务，提供 /encode 端点，可用 curl 或 Python 客户端调用，并暴露 Prometheus 指标。支持部署到 BentoCloud，也可用 BentoML 生成 OCI 兼容镜像在自有基础设施部署。面向想在生产环境运行嵌入模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SentenceTransformers 模型 all-MiniLM-L6-v2 的嵌入推理服务
- 提供 /encode HTTP 端点，支持 curl 与 Python 客户端调用
- 内置 Prometheus 指标暴露
- 支持 BentoCloud 部署或生成 OCI 兼容镜像自部署

## 适用场景

- 快速搭建句向量/文本嵌入 API 服务
- 学习如何用 BentoML 封装 transformer 模型为生产服务
- 为检索或语义搜索系统提供嵌入计算后端

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: This is a BentoML example project, demonstrating how to build a sentence embedding inference API server, using a Sen
> L19: We have defined a BentoML Service in `service.py`. Run `bentoml serve` in your project directory to start the Servi

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/BentoSentenceTransformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `deb93abc9e8b` · [字段定义](../../DATASET.md)*
