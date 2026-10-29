# gabe-santana/corollary

⭐ 19 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/gabe-santana/corollary) · [官网](https://pypi.org/project/corollary) · 个人维护

**以信念为状态单元的 LLM agent 运行时：事实修正自动级联更新结论**

面向开发者的 Python agent 运行时：用信念库（声明+置信度+来源+依赖）替代消息日志作为状态，底层为真值维护系统（Doyle, 1979）。模型作为无状态提议者提出结构化声明，由运行时验证、执行工具并管理上下文；修正一个事实时依赖它的结论自动撤销并重推导，矛盾以 Conflict 对象呈现，回答附带可确定性验证的证明。核心无运行时依赖，模型 SDK 为可选附加项，无需 API key 可运行离线示例。项目处于 pre-alpha，接口可能在 1.0 前变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 信念库+真值维护：修正事实后相关结论自动级联撤销与重推导
- 模型不持有状态：声明经契约校验，上下文仅由 IN 信念投影构建
- 回答附带证明子图，由确定性验证器检查算术、引用与日期
- 核心零运行时依赖，提供无需模型调用的自修复示例

## 适用场景

- 长时运行 agent 在上游数据修正后自动同步下游结论
- 需要回答可审计、带推导链的企业分析任务
- 检测并以 Conflict 形式处理多来源证据冲突

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L44: Corollary replaces the message log with a **belief base**.
> L101: Corollary is not a system prompt asking a model to "track its reasoning." A prompt is a request; a model can ignor
> L103: The key inversion: **the model doesn't own the state, the runtime does.** The model is a stateless *proposer*. It 

## 星数曲线

```mermaid
xychart-beta
    title "gabe-santana/corollary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1f6dc3a49d34` · [字段定义](../../DATASET.md)*
