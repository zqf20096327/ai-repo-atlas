# zernie/vigiles

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/zernie/vigiles) · [官网](https://vigiles.sh) · 个人维护

**审计/测试 AI agent 配置（CLAUDE.md、技能与钩子）的 CLI 工具**

面向 Claude Code 与 Codex 用户的命令行工具：检查 agent 配置（CLAUDE.md/AGENTS.md、skills、subagents、hooks）中的引用是否真实存在、工具契约是否有效、技能是否冲突、是否存在数据泄露路径。提供 audit（A–F 评分报告）、lint（CI 门禁）、test（脚本替身驱动行为测试）、eval（用用户自己的 Claude 订阅做 A/B 评测）四个命令；除 eval 外均本地运行、无需 key。以 npx 方式使用，另有 vigiles.sh 浏览器演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- audit 按 6 类标准（真实性/触发/结构/安全/测试/评测）给出 A–F 评分
- lint/test 本地确定性运行，无需模型调用与 API key
- eval 在用户自己的 Claude 订阅上做技能 A/B 评测，输出 token 账单与正确性
- 以 Claude Code 插件形式安装 skills 与 hooks，可接入 CI workflow

## 适用场景

- 检查我仓库里的 CLAUDE.md/AGENTS.md 规则与技能配置是否真实有效
- 在 CI 中对 agent 配置做结构校验门禁
- A/B 评测某技能是否真的降低 token 成本且不破坏正确性
- 发现 agent 配置中的安全隐患（如可外发 secrets 的 subagent）

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L22: vigiles[^name] checks your harness is _real_, not just well-formed — Claude Code and Codex alike. One command, no k
> L60: |Command|Answers|Needs a model?|When to run|
> L92: Point it at any harness change that claims a number — does a compression skill pay for itself, is a subagent worth 

## 星数曲线

```mermaid
xychart-beta
    title "zernie/vigiles 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a968f78d678` · [字段定义](../../DATASET.md)*
