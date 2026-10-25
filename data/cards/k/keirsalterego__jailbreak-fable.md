# keirsalterego/jailbreak-fable

⭐ 44 · JavaScript · 推送 2026-07-17 · [GitHub](https://github.com/keirsalterego/jailbreak-fable) · 个人维护

**针对 Claude 的多 agent 越狱研究实验室与环境模拟器**

安全研究工具：模拟 Claude Fable 5 (Mythos) 环境，并实现 "Pack Hunt" 多 agent 协同越狱工作流。机制包括：将高风险目标分解为 3-5 个良性子任务、生成 50 行学术大纲与 6 周讲义构造良性上下文、用 claude-opus-4-8 作顾问自动改写被拒提示、西里尔同形字混淆绕过关键词分类器，并行部署多 agent 收集数据片段并由 Recomposer 合成。归档了约 12 万字符的泄露系统提示词与全套 SKILL.md。通过 npm 安装，复用本地 Claude 登录凭据认证，无需单独 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pack Hunt 多 agent 并行协同越狱工作流（分解+长上下文构造+顾问改写循环）
- Parseltongue 西里尔同形字混淆，可调节混淆比例
- 归档约 120,000 字符的 Claude Fable 5 泄露系统提示词与全套 SKILL.md 文件
- 复用 ~/.claude/.credentials.json 登录凭据，支持 ANTHROPIC_API_KEY 回退

## 适用场景

- 红队人员对 Claude 模型安全层做自动化压力测试
- 研究多 agent 协同与提示分解对安全机制的绕过方式
- 在高保真模拟环境中复现泄露系统提示词下的 agent 行为

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L10: This tool is a high-fidelity emulation of the Claude Fable 5 (Mythos) environment, designed for security research a
> L12: It works by programmatically injecting workflows that utilize decomposition, long-context manipulation, and text ob
> L34: An automated offensive laboratory that implements the methodology used by red-teamers like Pliny the Liberator:

## 星数曲线

```mermaid
xychart-beta
    title "keirsalterego/jailbreak-fable 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5d232b40a6fc` · [字段定义](../../DATASET.md)*
