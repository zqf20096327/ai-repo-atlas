# bentoml/simple_di

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/bentoml/simple_di) · 组织维护

**Python 严格类型依赖注入库，供 BentoML 等项目使用**

simple_di 是一个简单的、带严格类型标注（PEP 类型注解）的 Python 依赖注入库。核心 API 提供 inject、Provide、Provider、container，以及 Static、Factory、Configuration 三类 Provider；支持将值通过函数/方法参数注入到 providers，并带 squeeze_none 选项（默认 False，将传入的 None 视为未传入）。以 pip 安装的 Python 库形式提供，由 BentoML 组织维护，属于其 ML 服务框架的基础组件。README 未声明独立于类型检查器的运行时功能以外的机制细节。

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

- inject / Provide / Provider / container 依赖注入 API
- Static、Factory、Configuration 三类 Provider
- 函数/方法参数级注入并支持类型标注

## 适用场景

- Python 项目中以类型安全方式管理依赖注入
- 配合配置对象（Configuration Provider）注入配置项

## 场景标签

 · 领域:软件工程/基础库

## 证据(README 行号)

> L1: # simple-di
> L3: A simple, strictly typed dependency injection library.

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/simple_di 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `63c14a3adfa5` · [字段定义](../../DATASET.md)*
