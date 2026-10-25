# HideyoshiNakazone/jambo

⭐ 95 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/HideyoshiNakazone/jambo) · [官网](https://jambo.readthedocs.io/) · 个人维护

**将 JSON Schema 转换为 Pydantic 模型的 Python 库**

Jambo 是一个 Python 包，读取 JSON Schema 定义并动态生成 Pydantic 模型，用于模式校验与类型安全。支持字符串、数值、数组、嵌套对象、allOf/anyOf/oneOf、ref、enum、const 等结构，并落实 minLength、pattern、minimum、uniqueItems 等约束。项目定位为简化为 LangChain、CrewAI 等 AI 框架动态生成 Pydantic 模型的过程。提供静态 API 与带引用缓存的实例 API 两种用法，零配置；通过 pip 安装，文档托管于 readthedocs，采用 MIT 许可。

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

- JSON Schema 动态转换为 Pydantic 模型，零配置
- 支持 allOf/anyOf/oneOf/ref/enum/const 与嵌套结构
- 实例 API 提供基于 $id 命名空间的引用缓存与子类型复用
- 落实 minLength/pattern/minimum/uniqueItems 等约束校验

## 适用场景

- 为 AI 框架（LangChain/CrewAI 等）从 JSON Schema 动态生成校验模型
- 复用与共享生成的子类型及引用缓存
- 将既有 JSON Schema 迁移到 Pydantic 校验体系

## 场景标签

 · 领域:开发者工具/数据校验

## 证据(README 行号)

> L20: **Jambo** is a Python package that automatically converts JSON Schema definitions into Pydantic models.
> L23: Created to simplify the process of dynamically generating Pydantic models for AI frameworks like LangChain, CrewAI,

## 星数曲线

```mermaid
xychart-beta
    title "HideyoshiNakazone/jambo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-25 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `06f6b0690aa7` · [字段定义](../../DATASET.md)*
