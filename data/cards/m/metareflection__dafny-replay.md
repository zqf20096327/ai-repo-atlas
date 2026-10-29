# metareflection/dafny-replay

⭐ 41 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/metareflection/dafny-replay) · [官网](https://midspiral.com/blog/from-intent-to-proof-dafny-verification-for-web-apps/) · 组织维护

**Dafny 编写、编译为 JS 的形式化验证状态内核，供交互式 Web 应用**

以 Dafny 语言编写并编译为 JavaScript 的可复用验证内核集合：涵盖本地回放（undo/redo）、服务器权威、离线客户端多协作、客户端效应编排（有界重试）与跨项目操作五类内核，全局不变量证明一次后由构造保持。附带 Kanban 看板、图表约束求解、费用分摊等具体领域应用及 React 演示流水线，后端支持 Supabase 或 Cloudflare。仓库同时充当 Dafny + LLM 证明辅助的基准测试。给需要正确性构造保证的 Web 应用开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五类通用验证内核（回放/权威/多协作/效应状态机/多项目）
- 全局不变量证明一次，undo/redo 正确性自动获得
- JS 层仅处理 I/O，状态转换全部经验证的 Step 函数
- 兼作 Dafny + LLM 证明辅助的非局部不变量基准

## 适用场景

- 为看板、协作清单等交互应用提供经验证的状态内核
- 构建服务器权威的离线协作客户端
- 评估 LLM 辅助 Dafny 证明能力的基准任务

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **Verified kernels, written in Dafny and compiled to JavaScript, for correct-by-construction state in interactive we
> L34: It also doubles as a **benchmark for Dafny + LLM proof assistance**, exercising non-local invariants and sequence/m

## 星数曲线

```mermaid
xychart-beta
    title "metareflection/dafny-replay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-29 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `760bfa575de5` · [字段定义](../../DATASET.md)*
