# autotraderuk/fastapi-mlflow

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/autotraderuk/fastapi-mlflow) · 组织维护

**把 MLflow 模型部署为 JSON API 的 FastAPI 库**

Python 库，提供 build_app 函数将已加载的 MLflow pyfunc 模型包装为 FastAPI 应用，自动生成 API 文档，通过 Uvicorn 等 ASGI 服务器运行；支持借 FastAPI 子应用托管多个模型，也可直接构建预测函数以自定义路由挂载。限制：仅支持含简单数据类型的扁平 MLflow schema，不支持嵌套对象或数组字段。生产运行需另行搭配 ASGI 服务器（如 Uvicorn/Hypercorn）。面向使用 MLflow 管理模型的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- build_app 将 MLflow pyfunc 模型包装为 FastAPI 应用
- 自动生成模型 API 文档并可在线测试
- 支持子应用托管多个模型与自定义路由挂载

## 适用场景

- 把训练好的 MLflow 模型快速暴露为 JSON 预测接口
- 在同一个 FastAPI 服务中托管多个模型
- 为模型端点定制路由与挂载方式

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Deploy mlflow models as JSON APIs using FastAPI with minimal new code.
> L37: from fastapi_mlflow.applications import build_app

## 星数曲线

```mermaid
xychart-beta
    title "autotraderuk/fastapi-mlflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a7c2767dee5d` · [字段定义](../../DATASET.md)*
