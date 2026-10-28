# ContextJet-ai/awesome-llm-observability

⭐ 43 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/ContextJet-ai/awesome-llm-observability) · 组织维护

**LLM 可观测化工具策展清单，附 26 个可安装 agent 技能**

由 ContextJet.ai 维护的 LLM observability 精选清单：人工核验 75+ 个追踪/评测/护栏/监控工具，按开源、open-core、商业三类标注，星数通过 CI 每周从 GitHub API 自动刷新。另附带 26 个 SKILL.md 格式的 agent 技能（部分含单元测试并在 CI 中验证），覆盖添加追踪、评测集构建、幻觉检测、成本削减、PII 脱敏等任务；技能触发质量用自研 skillvitals 工具在 llama-3.1-8b 上测得平均 F1 0.99。提供 Claude Code 插件、npx degit 与 git clone 三种安装方式，并含一份金融/受监管行业指南和一个 vendor-neutral OTel GenAI tracer 脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 75+ 工具清单，星数由 CI 每周自动刷新
- 26 个 SKILL.md agent 技能，部分带单元测试并在 CI 验证
- skillvitals 以 llama-3.1-8b 测量技能触发质量（平均 F1 0.99）
- 平台对比表覆盖 Langfuse/Phoenix/LangSmith/Opik/Helicone 等

## 适用场景

- 为 LLM 应用选型追踪/评测/监控工具
- 给编码 agent 安装可观测化相关技能
- 比较各可观测化平台的自托管与许可条件

## 场景标签

`精选清单` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **A current, hand-checked list of 75+ LLM observability tools, plus 26 agent skills you install in one command.**
> L35: Most lists stop at links. This one also ships 26 agent skills, the `SKILL.md` kind, so your coding agent knows how 

## 星数曲线

```mermaid
xychart-beta
    title "ContextJet-ai/awesome-llm-observability 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-28 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0b7e01888112` · [字段定义](../../DATASET.md)*
