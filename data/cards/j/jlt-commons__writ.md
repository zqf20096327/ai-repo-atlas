# jlt-commons/writ

⭐ 15 · Clojure · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/jlt-commons/writ) · 组织维护

**给 Clojure 开发者的规格验证 DSL：用证明和性质检验 LLM 写的代码**

面向 LLM 生成代码的 Clojure 验证工具：先写问题规格（公共函数签名、状态图、定律），再写普通 Clojure 实现，writ 作为两者之间的门禁。行为检查有两条路径：经 test.check 在规格类型生成的输入上运行定律；以及通过重写、归纳、符号执行加求解器对定律给出证明，证明由独立小检查器回放、求解器答案带可验证证书。静态规则来自 Bend（纯代码、可证终止递归、顺序定义、类型匹配）。它还检查规格本身：拒绝空洞定律，并用替身与变异体暴露规格未钉死的函数。以 test 依赖（deps.edn git 坐标）形式接入，生产代码不加载 writ。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定律既经 test.check 性质测试，也可由重写/归纳/符号执行加求解器给出证明，证明由独立检查器回放
- 检查规格本身：拒绝空洞定律，用固定替身家族与可选变异体（:adequacy :mutants）暴露规格缺口
- 静态规则来自 Bend：纯代码、可证终止递归、按序定义、类型匹配
- 实现前可单独检查规格（'no implementation yet'），规格作为 clojure.test 命名空间持续把守每次改动

## 适用场景

- AI agent 生成代码后，用规格证明实现是否符合意图，替代逐例测试
- 在实现前固化问题规格，提前发现规格与示例的矛盾
- 把规格留在测试套件中，作为每次代码变更的门禁

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: It is built for code an LLM writes. The spec is the intent: the problem's
> L10: person, writes it first; then the implementation. writ is the gate

## 星数曲线

```mermaid
xychart-beta
    title "jlt-commons/writ 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a10e149d2d0` · [字段定义](../../DATASET.md)*
