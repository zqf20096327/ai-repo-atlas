# huggingface/paperswithcode

⭐ 269 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/huggingface/paperswithcode) · [官网](https://paperswithcode.co) · 组织维护

**重建 Papers with Code：追踪 AI 论文、代码、数据集与榜单的目录站**

Hugging Face 维护的 Papers with Code 重启版：聚合 arXiv 论文、官方代码、模型、数据集、任务、方法与基准榜单，通过来自 Hugging Face、arXiv、GitHub 及公开榜单的自动化导入保持更新。提供论文目录、分类浏览、原生评测榜单、混合词法+语义（pg_trgm/pgvector）检索、兼容原版 API 客户端的 REST API，以及基于目录的 MCP 研究问答助手（可选）。技术栈为 React 前端 + FastAPI 后端 + PostgreSQL 16，本地开发需 uv、Node.js 18+ 与 pgvector 扩展，附带 pwc 维护 CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 论文-代码-数据集-榜单聚合目录，自动化每日导入与策展
- 混合检索：pg_trgm 词法 + pgvector 语义
- 兼容原 Papers with Code API 客户端的 REST API（/api/v1/）
- pwc CLI 支持索引、查询与目录维护

## 适用场景

- 查找 AI 论文对应的官方代码、数据集与评测结果
- 按任务/方法/会议浏览与对比基准榜单
- 通过 API 或 CLI 程序化访问论文目录

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Papers with Code makes open AI research and its artifacts accessible: papers,
> L4: code, models, datasets, tasks, methods, and benchmark leaderboards. It recreates
> L5: the original paperswithcode.com, which Meta retired in 2025, and keeps it up to

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/paperswithcode 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-28", "2026-10-29"]
    y-axis "stars" 38 --> 290
    line [59, 238, 269]
```

2026-10-26 59 → 2026-10-29 269（+210）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `abebb6c75168` · [字段定义](../../DATASET.md)*
