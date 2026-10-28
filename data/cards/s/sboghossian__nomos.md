# sboghossian/nomos

⭐ 23 · TypeScript · NOASSERTION · 推送 2026-04-21 · [GitHub](https://github.com/sboghossian/nomos) · [官网](https://nomos.dashable.dev) · 个人维护

**面向法律推理的实验性编程语言：带类型规则、LLM 事实抽取与可溯源证明树**

Nomos 是一门用 TypeScript 实现的领域编程语言，用于把法律规则编码为代码。规则可声明管辖权、生效日期、优先级与击败关系；内部采用可废止逻辑（优先级→特殊性→新法→声明顺序）做冲突裁决；LLM 抽取（extract<T> using llm）作为一等语言原语放在边界，低置信度结果路由到人工队列；每个判定输出可追溯到法条与判例的证明树。经 OpenRouter 桥接多家模型，提供 CLI、VS Code 扩展与浏览器 Playground。自述为实验性 v0.1.1，声明不适用于生产级法律意见。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 带管辖权/生效日期/优先级/击败关系的类型化规则与可废止逻辑裁决
- extract<T> using llm 为一等语言原语，置信度低于阈值路由人工队列，另有 extractEnsemble 跨模型一致性机制
- 判定附带可回溯到法条与判例的证明树
- 提供 CLI（run/parse/check/resolve）、VS Code LSP 扩展与浏览器 Playground，附 CUAD 基准

## 适用场景

- 让法律 AI 代理的条款判定输出可审计的证明树供合规官核验
- 按日期与管辖权运行合规规则（如以签约日为准适用当时有效规则）
- 带置信度门控的结构化合同抽取，分歧样本转人工

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L54: 1. **Typed LLM bridges** — `extract<Party>(pdf) using llm(...) verified_by human if confidence < 0.95` is a languag
> L206: - **LLM bridge**: first-class primitive (`extract<T> using llm(...) verified_by human`)

## 星数曲线

```mermaid
xychart-beta
    title "sboghossian/nomos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `009a2f11d508` · [字段定义](../../DATASET.md)*
