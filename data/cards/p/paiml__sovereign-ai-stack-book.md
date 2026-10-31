# paiml/sovereign-ai-stack-book

⭐ 15 · Makefile · MIT · 推送 2026-08-28 · [GitHub](https://github.com/paiml/sovereign-ai-stack-book) · [官网](https://paiml.github.io/sovereign-ai-stack-book/) · 组织维护

**纯 Rust 主权 AI 技术栈书籍：23 章可复现代码讲解 EU 合规 ML 基础设施**

Pragmatic AI Labs 出品的技术书籍，用 mdBook 组织 23 章 6 部分，讲解名为 Sovereign AI Stack 的纯 Rust ML 生态：trueno 计算、aprender 算法、realizar 推理、entrenar 训练等组件，以及 bash/Python/C 到 Rust 的转译器。采用 EXTREME TDD 方法，读者 git clone 后 make test 即可本地验证书中全部声明；覆盖 EU AI Act 第 10/13/15 条合规主题。要求 Rust 1.75+，支持 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 23 章 6 部分覆盖 ML 计算、训练、推理、转译器与基础设施组件
- EXTREME TDD：95%+ 覆盖率、80%+ 变异分数、make test 可验证全部声明
- 针对 EU AI Act 第 10/13/15 条的合规代码讲解
- 章节示例可 cargo run 执行并运行基准测试

## 适用场景

- 学习用纯 Rust 搭建可控的 ML 基础设施
- 为 EU AI Act 合规需求寻找可审计的技术方案参考
- 通过可运行代码验证书中性能与质量声明

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L21: This book documents the **Sovereign AI Stack**, a complete pure-Rust ecosystem for organizations requiring full con
> L25: - **Scientific Reproducibility**: `git clone` → `make test` → all claims verified
> L105: The book covers 23 chapters across 6 parts:

## 星数曲线

```mermaid
xychart-beta
    title "paiml/sovereign-ai-stack-book 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b4135472325b` · [字段定义](../../DATASET.md)*
