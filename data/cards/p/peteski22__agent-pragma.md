# peteski22/agent-pragma

⭐ 24 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/peteski22/agent-pragma) · 个人维护

**给 AI 编程 agent 的规则注入与合规校验技能插件**

面向 Claude Code 与 OpenCode 的技能/插件集：通过 /implement、/validate、/review 等命令把项目规则机械注入会话，并由确定性验证器（安全、状态机、错误处理、Go/Python/TS 语言风格）自动检查实现合规性，输出按 HARD/SHOULD/WARN 分级的报告。支持 monorepo 路径级规则作用域，两个 agent 共享同一套 .claude/rules 规则文件。/star-chamber 提供多 LLM 共识评审，需额外 API key。Claude Code 经插件市场安装，OpenCode 经 git clone 与 make 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则注入 + 确定性验证器自动校验，验证器优先于规则文件
- 安全/状态机/错误处理及 Go/Python/TS 语言验证器按改动文件类型分发
- HARD/SHOULD/WARN 三级严重度分级，HARD 阻断 /implement 完成
- monorepo 路径级规则作用域，Claude Code 与 OpenCode 共享规则文件

## 适用场景

- 让 AI 编程 agent 在编码过程中强制执行项目规范
- 对代码改动自动跑安全与风格校验并出分级报告
- 团队通过提交 .claude/rules 文件统一项目规则

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: **The solution:** agent-pragma provides skills that mechanically inject rules and validate compliance. Rules aren't 
> L7: **Works with both Claude Code and OpenCode.**

## 星数曲线

```mermaid
xychart-beta
    title "peteski22/agent-pragma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e151229bc138` · [字段定义](../../DATASET.md)*
