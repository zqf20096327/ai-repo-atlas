# noworneverev/graphrag-api

⭐ 113 · Python · MIT · 推送 2026-02-04 · [GitHub](https://github.com/noworneverev/graphrag-api) · 个人维护

**将 Microsoft GraphRAG 封装为 FastAPI 查询服务的 API 服务器**

基于 FastAPI 的服务器，封装 Microsoft GraphRAG v2.2.0，通过 HTTP 端点提供 Global、Local、DRIFT 与 Basic 四种检索能力，并附带 Swagger 文档页面。使用方式为克隆仓库、创建虚拟环境并 pip 安装依赖，随后将已有 GraphRAG 项目目录（含 output、prompts、settings.yaml、.env）复制到仓库根目录，在 config.py 中指向该目录后运行 python api.py。限制：不负责 GraphRAG 索引构建，需用户预先准备 GraphRAG 项目产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 /search/global、/search/local、/search/drift、/search/basic 四个 API 端点
- 基于 FastAPI，附带 /docs API 文档页
- 兼容 GraphRAG Visualizer 或自定义客户端查询

## 适用场景

- 把已构建好的 GraphRAG 索引以 REST API 形式提供给应用调用
- 配合 GraphRAG Visualizer 做图检索可视化查询
- 对比 GraphRAG 的 Global/Local/DRIFT/Basic 检索模式

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: A FastAPI-based server that provides Global, Local, DRIFT, and Basic search capabilities based on Microsoft GraphRAG
> L51: - `/search/global`: Perform a global search using GraphRAG.

## 星数曲线

```mermaid
xychart-beta
    title "noworneverev/graphrag-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-23 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `caa894a5b2f3` · [字段定义](../../DATASET.md)*
