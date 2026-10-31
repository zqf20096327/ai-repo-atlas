# lorenzofamiglini/The-Forge-Protocol-Agent

⭐ 16 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent) · [官网](https://github.com/lorenzofamiglini/The-Forge-Protocol-Agent) · 个人维护

**防去技能化的人机协作框架：让 AI 只提问不代答**

基于 Milano-Bicocca 大学 Cabitza 实验室人机协作研究（Hounds/Rams/白盒悖论等）实现的开源框架，以 Hermes Agent 插件（9 工具+2 钩子）形式提供四种交互模式：Forge 只提问不给答案、Anvil 评审草稿不改写、Crucible 压力测试想法、Executor 用于机械任务的常规自动化。编排器 SOUL 在线判定任务是思考型还是执行型；可启用独立 Claude Sonnet 审计员对输出做合规裁决，并用固定 canary 题目按周追踪用户独立能力变化。面向教育者与学生，也面向关注认知技能保持的个人用户。需 Python 3.11+ 与 LLM 提供商（Vertex AI/OpenRouter/Anthropic API 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种模式（Forge/Anvil/Crucible/Executor）对应 Cabitza 实验室经验证的人机协作协议
- 编排器 SOUL 在线分类思考型/执行型任务，Executor 中检测思考任务会警告
- 独立审计员 LLM 实例校验模式合规，返回结构化 JSON
- canary 定时无辅助作答，从清晰度/深度/独立性三维度追踪趋势
- YAML 定义自定义模式，核心库无 Hermes 依赖

## 适用场景

- 把 LLM 变成只提问不给答案的苏格拉底式导师
- 学术写作时让 AI 评审我的草稿而不是代写
- 按周测量自己不依赖 AI 的独立思考能力变化
- 学校/课程层面部署，防止学生用 AI 代做作业

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L43: > **Forge Protocol doesn't cite these papers — it implements them.** The four modes map one-to-one onto protocols e
> L230: ├── plugin/          # Hermes Agent plugin (9 tools + 2 hooks)
> L239: - **Plugin architecture** — Registers via Hermes's native `PluginContext` API.

## 星数曲线

```mermaid
xychart-beta
    title "lorenzofamiglini/The-Forge-Protocol-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `49749a684579` · [字段定义](../../DATASET.md)*
