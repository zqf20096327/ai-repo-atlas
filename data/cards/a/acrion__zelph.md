# acrion/zelph

⭐ 16 · C++ · AGPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/acrion/zelph) · [官网](https://zelph.org) · 组织维护

**C++ 语义网络与推理引擎：规则、事实与数均为图中节点**

zelph 是以 C++ 编写、内嵌 Janet 脚本层的语义网络系统与推理引擎，将逻辑规则、事实与数学作为同像（homoiconic）节点统一在同一图中，使静态知识库成为可执行图。支持深度合一、构造性规则、失败即否定等逻辑编程概念；导入 1.7TB Wikidata 转储可在单机构建 9.83 亿节点并检出数千条一致性问题。整个数学栈由规则而非 C++ 算术实现。由 acrion innovations GmbH 维护，获 NLnet NGI0 与 Wikimedia 基金资助，双许可（AGPL-3.0 或商业许可）。提供全平台预编译二进制与 WebAssembly 浏览器演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则、事实、数学为同一图中的节点（同像结构）
- 单机导入 1.7TB Wikidata 转储构建 9.83 亿节点并检测矛盾
- C++ 核心无算术，数学栈（数字、多项式、符号微分）全部由规则实现
- 嵌入 Janet 脚本层并提供 Rust 绑定（同一 C ABI）

## 适用场景

- 在 Wikidata 等链接开放数据上做大规模一致性检查与约束推理
- 以图内规则构建可执行的知识库与符号数学证明
- 通过 WebAssembly 在浏览器中试用推理引擎

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: **zelph** is an innovative semantic network system and reasoning engine written in C++ with an embedded Janet script
> L11: By blending the flexibility of semantic webs (like Wikidata) with logic programming concepts (deep unification, con

## 星数曲线

```mermaid
xychart-beta
    title "acrion/zelph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d1fdcca493aa` · [字段定义](../../DATASET.md)*
