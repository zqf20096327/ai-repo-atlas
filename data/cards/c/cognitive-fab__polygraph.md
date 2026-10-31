# cognitive-fab/polygraph

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/cognitive-fab/polygraph) · [官网](https://cognitivefab.com) · 组织维护

**面向有状态代码的 LLM 形式化验证插件：自动建模并穷举检查**

Claude Code 插件（兼独立 CLI），用于查找有状态代码（工作流、reducer、协议处理器、计费流程等）中的缺陷：LLM 从源码推导可执行的独立规格，随后重放真实执行轨迹验证规格忠实性，并在声明的有限（动作，数据）域上做穷举模型检查，报告违反规则的状态并给出最短反例路径。规则以纯 JavaScript 谓词书写。另有 polygen 生成新代码、polyvers 版本门控等共五个引擎。作者明确声明为实验性、未经同行评审技术，结果仅为需人工核查的线索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 从源码推导独立可执行规格（SAM v2 严格模式），多规格独立投票
- 在有限声明的（动作，数据）域上穷举模型检查，输出最短反例路径
- 重放真实执行轨迹确认规格忠实性
- 五个共享工件族的引擎：审计/polygen 生成/polyrun 执行/polyvers 版本/polyynv 规则引出

## 适用场景

- 对计费流程、会话管理等有状态代码做穷举式缺陷检查
- 在代码变更时用版本门控核验状态机兼容性
- 让 LLM 依据一句话需求生成带通过验证的状态机代码

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: Polygraph is a Claude Code plugin (and standalone CLI) that finds bugs in
> L58: - **Audit existing code** (`/polygraph:verify`). An LLM reads your source and
> L61:  against that spec to confirm it's faithful, and (2) **model-checks** it:

## 星数曲线

```mermaid
xychart-beta
    title "cognitive-fab/polygraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `95d1a9d66734` · [字段定义](../../DATASET.md)*
