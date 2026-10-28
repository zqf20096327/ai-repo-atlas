# frmoretto/clarity-gate

⭐ 34 · Python · NOASSERTION · 推送 2026-03-02 · [GitHub](https://github.com/frmoretto/clarity-gate) · [官网](https://clarity-gate.org) · 个人维护

**面向 RAG 的预摄取文档认知质量校验协议与 Claude 技能**

开源的预摄取验证系统：在文档进入知识库前，按 9 个验证点检查认知质量——区分事实/假设/预测、强制前瞻性声明带不确定性标记、暴露隐式假设、检测文内数据矛盾等。提供 Verify（出报告+两轮 HITL 人工核验）与 Annotate（生成标注后的 CGD 文档）两种模式。以 SKILL.md 技能形式交付，支持 claude.ai、Claude Desktop、Claude Code、OpenAI Codex、GitHub Copilot 等平台，方法论本身工具无关。限制：只校验形式不校验真实性，PASS 前强制 HITL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 9 个验证点：假设/事实标注、不确定性标记强制、隐式假设显式化、数据一致性等
- 两轮 HITL 路由：区分快速确认与会话来源声明与需真实核验的声明
- 输出 Clarity-Gated Document（CGD）标注文档用于 RAG 摄取
- 多平台技能分发：claude.ai / Claude Code / OpenAI Codex / GitHub Copilot

## 适用场景

- 在文档进入 RAG 知识库前拦截把预测当事实的表述
- 为含草稿、会议纪要、工单的语料库建立可验证的摄取关卡
- 让 AI 助手按 9 点协议审阅并标注文档的认知问题

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L36: Clarity Gate is an **open-source pre-ingestion verification system** for epistemic quality.
> L262: Layer 2: Input/Context Verification  <-- Clarity Gate
> L82: 1. Download `dist/clarity-gate.skill`

## 星数曲线

```mermaid
xychart-beta
    title "frmoretto/clarity-gate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b00c7ebea9c6` · [字段定义](../../DATASET.md)*
