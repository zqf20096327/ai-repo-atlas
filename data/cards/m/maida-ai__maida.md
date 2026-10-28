# maida-ai/maida

⭐ 31 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/maida-ai/maida) · [官网](https://maida.ai) · 组织维护

**AI agent 行为回归门禁：合并前检查 agent 变更是否破坏行为**

面向在仓库中使用编码 agent 的开发团队：Maida 在 merge 前捕获 agent 执行任务时的工具调用与生命周期，检查成功完成、循环与 guardrail 事件，维护基线与策略并输出 PASS/FAIL/INCONCLUSIVE 裁决；可识别重写测试以隐藏缺陷等行为。本地优先运行，默认不上传任务证据，默认开启脱敏与大字段截断。以 PyPI 包提供引擎、CLI 与公共契约，支持 Claude Code、LangChain/LangGraph、OpenAI Agents SDK 集成，可加 GitHub Actions PR 门禁。限制：捕获不比较基线正确性也不覆盖完整模型调用，INCONCLUSIVE 也退出 0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 合并前行为回归门禁，输出 PASS/FAIL/INCONCLUSIVE 裁决
- 本地优先：无云账户，任务证据默认不上传，默认脱敏
- 支持 Claude Code / LangChain / LangGraph / OpenAI Agents SDK 集成适配器
- 提供 maida demo --regression 离线演练与时间线查看器

## 适用场景

- 编码 agent 改动合并前拦截行为回归（如循环、跳过验证、改写测试）
- 为 agent 仓库配置 GitHub Actions PR 必需检查
- 查看 agent 任务执行时间线以定位回归原因

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: Your coding agent returns a plausible answer and the tests pass, but it now loops, skips verification, or rewrites 
> L51: The first `maida check` checks successful completion, recorded loops, and guardrail events. It does not compare a b
> L59: Read the comparative verdict: **PASS**, **FAIL**, or **INCONCLUSIVE**. It applies to the observed evidence and sele

## 星数曲线

```mermaid
xychart-beta
    title "maida-ai/maida 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `552b5ce08352` · [字段定义](../../DATASET.md)*
