# mlte-team/mlte

⭐ 21 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/mlte-team/mlte) · [官网](http://mlte.rtfd.io/) · 组织维护

**机器学习模型测试与评估框架（Python 库+Web UI）**

面向机器学习模型与系统的评估框架：以 Python 库形式使用，通过 set_context/set_store 指定模型版本与工件存储位置，管理评估工件；支持四种存储后端、可选的关系数据库存储与 GPU 测量依赖；另提供 Web UI（backend + ui 命令启动，默认 localhost:8000）用于查看/编辑存储工件、审阅模型与测试目录，内置用户登录机制。安装通过 pip（PyPI 提供 mlte 包），也可在 Docker 隔离环境从源码构建 wheel。附 ICSE-NIER 2023 论文可供引用。

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

- Python 库形式管理评估工件，需先设定 context 与 store
- 可选 frontend/backend/rdbs/gpu 依赖扩展 Web UI 与 GPU 测量
- Web UI 支持查看/编辑工件、审阅模型与测试目录，含用户体系
- 可用 make build-in-docker 在 Docker 隔离环境构建 wheel

## 适用场景

- 在模型开发流程中记录和管理评估工件
- 通过 Web UI 审阅模型与测试目录
- 团队协作环境下以关系数据库存储评估结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: `MLTE` (pronounced "melt") is a framework and infrastructure for evaluating machine learning models and systems. To 
> L77: The `MLTE` Python package is best used in conjunction with the `MLTE` process framework. For more details on using 

## 星数曲线

```mermaid
xychart-beta
    title "mlte-team/mlte 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `45c57b93c24b` · [字段定义](../../DATASET.md)*
