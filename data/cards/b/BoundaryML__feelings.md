# BoundaryML/feelings

⭐ 24 · BAML · 推送 2026-09-19 · [GitHub](https://github.com/BoundaryML/feelings) · [官网](https://boundaryml.com/blog/typesafe-ai-jev) · 组织维护

**BAML 扩展：用 .feels() 等类型化方法做 LLM 判断与生成**

基于 BoundaryML BAML 语言与 TypeSafe AI 的 Jev 分类器构建的工作流扩展，核心是约 20 行的 vibes.baml：为任意值提供 blanket 实现的 .feels()（阈值 0.5 返回 bool）、.how()（返回概率）、.matches<T>()/.judge<T>()（枚举/字面量联合路由）、.fill<T>()（类字段并发多问一次请求）与 .ask()（交给生成模型）。Jev 只做分类，字符串/整数/数组不能用于 .matches/.fill，文本生成需用 .ask()。因为是真实语言，可使用类型、泛型、循环、并发与离线测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .feels()/.how() 对任意值做带类型与概率的判断
- .fill<T>() 将类字段转为一次请求的多个问题
- while + feels 循环迭代生成直至满足描述
- 附 grep_with_vibes：模式为感受的 stdin shell 工具

## 适用场景

- 在 BAML 工作流中按自然语言描述路由与分类消息
- 带置信度阈值的多分支邮件分流与回复生成
- 用感受描述过滤批量文本（如 commit 信息）

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **`.feels()` on anything.** A programming language for LLM workflows where the
> L34: Everything below is ordinary BAML. The only thing this repo adds is

## 星数曲线

```mermaid
xychart-beta
    title "BoundaryML/feelings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5d5407bec60e` · [字段定义](../../DATASET.md)*
