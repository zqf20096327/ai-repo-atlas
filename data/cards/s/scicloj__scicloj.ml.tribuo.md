# scicloj/scicloj.ml.tribuo

⭐ 13 · Clojure · EPL-1.0 · 推送 2026-04-05 · [GitHub](https://github.com/scicloj/scicloj.ml.tribuo) · 个人维护

**把 Tribuo 机器学习库集成进 scicloj.ml/metamorph 的 Clojure 库**

Clojure 库，将 Java 机器学习库 Tribuo 接入 scicloj.ml / metamorph 框架：通过配置 map 使用 Tribuo 的全部模型（如分类训练与预测），训练产物可封装进 metamorph pipeline 管理状态。各模型分布在不同的 maven artifact 中，使用时需添加对应 maven 依赖。提供基于 clojure CLI 的构建、测试与 Clojars 部署流程。面向 Clojure 数据科学开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | EPL-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过配置 map 支持 Tribuo 的全部模型
- 模型可作为普通函数调用，也可封装进 metamorph pipeline
- 配置 map 的值须为字符串类型
- 提供 clojure -T:build 测试/构建/Clojars 部署流程

## 适用场景

- 在 Clojure 数据流水线中用 metamorph 方式训练与预测 Tribuo 模型
- 复用 scicloj.ml 生态时以 Tribuo 作为机器学习后端

## 场景标签

 · 领域:机器学习/Clojure 库

## 证据(README 行号)

> L8: Integration of tribuo ML library into the scicloj.ml / metamorph framework.
> L12: All models of tribuo are supported out of the box, via a configuration map. See tribuo website for details.

## 星数曲线

```mermaid
xychart-beta
    title "scicloj/scicloj.ml.tribuo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `867bfc6cb2e2` · [字段定义](../../DATASET.md)*
