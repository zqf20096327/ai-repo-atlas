# entropyvortex/meta-llm-charter

⭐ 247 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/entropyvortex/meta-llm-charter) · 个人维护

**约束 LLM 编码代理行为的精简操作宪章（核心 2,399 字节）**

面向 Claude Code、Cursor 等编码代理的行为约束规范：以一份 2,399 字节、每会话自动加载的核心宪章（一个 Bias、元规则 META-0、九条规则）替代散文式提示，将需求分解、提问门禁、复现后再修复、证据标注、不可逆操作门禁等固化为确定性规则；另含三个显式调用的技能（/zero-pause、/weave、/premortem）与可选的写范围守卫钩子。README 明示 v3 尚无已发布的评测运行，历史数值标记为未验证。供希望在编码代理会话中施加工程纪律的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 核心宪章 2,399 字节，CI 门禁 2,400 字节，每会话自动加载
- 九条规则 + 元规则 META-0（OVERRIDE 声明式偏离，两项硬底线豁免）
- 三个显式调用技能与 PreToolUse 范围守卫钩子
- 证据自标注（[executed]/[inspected]/[assumed]），README 自述 v3 尚无已发布评测

## 适用场景

- 让编码代理遵守不可逆操作确认门禁与证据标注规范
- 在架构决策或高风险计划前调用 /premortem 做预失效分析
- 为并行多线任务使用 /weave 编排与范围守卫

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: A compact, operational constitution that turns frontier coding agents (Claude Code, Cursor, etc.) from eager-junior
> L19: |`CLAUDE.md`|The core charter: one Bias, one meta-rule (META-0), nine rules. 2,399 bytes `[executed: wc -c]`, CI-ga
> L39: curl -O https://raw.githubusercontent.com/entropyvortex/meta-llm-charter/main/CLAUDE.md

## 星数曲线

```mermaid
xychart-beta
    title "entropyvortex/meta-llm-charter 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 246 --> 249
    line [248, 247, 248, 248]
```

2026-10-18 248 → 2026-10-24 248（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `63d531c13864` · [字段定义](../../DATASET.md)*
