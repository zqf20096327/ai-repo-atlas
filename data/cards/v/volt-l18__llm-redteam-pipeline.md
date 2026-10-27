# volt-l18/llm-redteam-pipeline

⭐ 27 · Python · NOASSERTION · 推送 2026-08-12 · [GitHub](https://github.com/volt-l18/llm-redteam-pipeline) · 个人维护

**自动化多轮 LLM 红队评测管线：攻防对话评估模型安全边界**

由 Attacker、Target、Evaluator 三模型组成的红队评测框架：Attacker 依据 JSON 定义的攻击策略（如 Crescendo 渐进升级）生成多轮诱导对话，Evaluator 按安全评分规则输出 Breached/Secure 判定，会话日志自动聚合为 HTML 漏洞面板。经 litellm 支持本地 Ollama 模型与云 API（Gemini/OpenAI/Anthropic）混配路由，含速率限制退避、越狱早退检测。面向防御性安全研究与授权测试，Python 3.10+ 源码安装，CLI 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Attacker/Target/Evaluator 三模型对抗架构
- JSON 定义攻击策略与评判规则，无需改核心代码即可扩展
- LLM-as-a-Judge 输出 Breached/Secure 判定
- litellm 路由：本地 Ollama 与云 API 模型混配

## 适用场景

- 授权测试自研 LLM 的安全边界与对齐情况
- 研究多轮社会工程攻击（如 Crescendo）对模型的影响
- 生成含成功指标与完整对话记录的 HTML 漏洞报告

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: An automated, multi-turn red-teaming framework designed to evaluate the safety boundaries and alignment of Large Lan
> L22: * **LLM-as-a-Judge Evaluation:** Uses a strict, objective Evaluator model to grade Target responses against a defin

## 星数曲线

```mermaid
xychart-beta
    title "volt-l18/llm-redteam-pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f47effc9354b` · [字段定义](../../DATASET.md)*
