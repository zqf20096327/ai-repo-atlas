# metareflection/claimcheck

⭐ 33 · JavaScript · MIT · 推送 2026-07-05 · [GitHub](https://github.com/metareflection/claimcheck) · 个人维护

**核验 Dafny 引理是否忠实表达自然语言需求的审计工具**

面向形式化验证开发者的 CLI/Node 库：当外部代理（如 Claude Code 或人类）声称"需求 X 由引理 Y 覆盖"时，claimcheck 通过回译往返核验——先在不看需求的前提下将引理非形式化为英语（默认 haiku），再与需求比对（默认 sonnet），输出 confirmed/disputed 判定；单提示模式附加真空性分析与更细分裁决。支持 --verify 调用 dafny 验证，可选 Vertex AI / AWS Bedrock 后端，默认直连 Anthropic API。需要 Node.js 18+ 与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 回译往返：非形式化（不看需求）→ 比对，防止锚定偏差
- 双阶段与单提示两种模式，单提示含真空性分析与细分裁决
- 可用 --verify 对每条引理运行 dafny verify
- 5 个测试域 36 对需求-引理的基准（含 8 条故意伪造引理）

## 适用场景

- 核验他人提交的 Dafny 引理是否真的覆盖了需求
- 审计形式化验证结果与自然语言需求的一致性
- 比较不同 LLM 调用策略在声明核验上的准确率

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Someone else (Claude Code, a human, any agent) writes the lemmas and claims "requirement X is covered by lemma Y." C
> L160: By default, claimcheck calls the Anthropic API directly using `ANTHROPIC_API_KEY`. You can route through other bac

## 星数曲线

```mermaid
xychart-beta
    title "metareflection/claimcheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c9f9ccbd4319` · [字段定义](../../DATASET.md)*
