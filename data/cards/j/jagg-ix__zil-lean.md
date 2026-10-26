# jagg-ix/zil-lean

⭐ 34 · Lean · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/jagg-ix/zil-lean) · 个人维护

**基于 Lean 4 的关系型 DSL：描述对象关系与派生规则供多方查询**

ZIL 是嵌入 Lean 4 的小型关系语言，用元组（受 Google Zanzibar 论文影响）描述对象、关系与推导规则，提供 .zc 语法与原生 Lean 声明两种写法。其 Datalog 部分有经过证明的语义：最小模型等价于可推导事实集合，另有 certificate checker 与可靠性定理。命令行工具 zil 支持 explain-query 逐步解释派生关系的来源（规则、变量绑定、输入事实）。开发者、CI、文档工具与 AI 助手可查询同一份与源码共存的关系图。安装方式为 git clone 后 lake build。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 元组式关系模型（object#relation@user），支持 userset 继承访问
- Datalog 部分具有证明语义与 certificate checker 的可靠性定理
- explain-query 输出派生关系的逐步来源（规则/绑定/输入事实）
- 宏系统支持扩展自定义 DSL，libsets 可选宏库位于 zil-lib 仓库

## 适用场景

- 需求到实现、定理到组件的追溯与依赖分析
- 跨模块的变更影响查询与证据溯源
- AI 助手跨会话延续工作，受 revision 与 action-token 检查约束

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: Developers, review tools, CI, documentation tools, and AI assistants can query the same stored relationships.
> L110: ZIL stores selected project facts with the source code. Developers, reviewers, build tools, documentation tools, i
> L137: - AI assistants continuing work across sessions, guarded by revision and action-token checks;

## 星数曲线

```mermaid
xychart-beta
    title "jagg-ix/zil-lean 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-23 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `34247b0ba4dc` · [字段定义](../../DATASET.md)*
