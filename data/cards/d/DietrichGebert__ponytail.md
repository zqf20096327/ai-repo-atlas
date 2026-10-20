# DietrichGebert/ponytail

⭐ 166,806 · JavaScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/DietrichGebert/ponytail) · [官网](https://ponytail.dev) · 个人维护

**给 AI 编码 agent 注入“极简优先”编码原则的提示词技能包**

以单个 SKILL.md 提示词为核心的 agent 技能：在写代码前按七级阶梯依次判断“是否需要写、仓库已有、标准库、平台特性、已有依赖、能否一行”，只在必要时写最小实现；不做代码高尔夫，验证、错误处理、安全与可访问性不在裁剪范围，含分支/循环/解析/金钱/安全的逻辑要求附带小测试。提供 /ponytail-review（读 diff 之外被触碰的代码做审查）与 /ponytail-audit（全仓库按优先级排序）等命令，以及 Claude Code 中的成本/token/复用率状态条与本地统计面板。宣称在 20 个 agent 上可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.3 天,年发版 29,128 位贡献者
- 涨星:近 1 天 **+1,217**(自 20261016 起算)

## 能力要点

- 七级阶梯决策：优先复用仓库代码、标准库与平台特性
- /ponytail-review 读取变更触碰的全部代码而非仅 diff
- Claude Code 提示条展示成本、token、agent 时间与代码复用率
- /ponytail-debt 汇集 shortcut: 注释为技术债清单

## 适用场景

- 让编码 agent 复用仓库现有组件而不是重造轮子
- 审查 diff 之外被改动波及的文件与安全隐患
- 统计并追踪 AI 编码的成本、token 与复用率

## 场景标签

`提示工程` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L96: Ponytail is one prompt: `skills/ponytail/SKILL.md`. The compact version, for agents that read a rules file, is `AGE
> L139: Commands need a skill-capable host (Claude Code, Codex, Devin CLI, OpenCode, Gemini, Antigravity CLI, pi, Hermes A

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `d4ba9a8f2849` · [字段定义](../../DATASET.md)*
