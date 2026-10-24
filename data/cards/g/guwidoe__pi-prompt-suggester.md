# guwidoe/pi-prompt-suggester

⭐ 53 · TypeScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/guwidoe/pi-prompt-suggester) · [官网](https://www.npmjs.com/package/@guwidoe/pi-prompt-suggester) · 个人维护

**pi 编码助手的扩展：在每次回答后建议下一条提示词**

pi-prompt-suggester 是 pi coding agent 的扩展：在每次 assistant 回答完成后，基于近期对话上下文与轻量级项目意图种子（project intent seed），以编辑器幽灵文本（ghost text）形式建议用户可能的下一条提示词。支持可编辑的持久自定义指令、项目级或用户级行为覆盖、可配置的 suggester/seeder 模型与思考级别，通过 /suggesterSettings 主界面进行配置；空编辑器下按 Space 或 Right 接受建议。以 npm 包形式经 pi install 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 回答完成后以 ghost text 形式建议下一条用户提示词
- 基于近期对话上下文与项目意图种子生成建议
- 可自定义 suggester/seeder 模型与 thinking 级别
- 项目级/用户级覆盖，配置存储于 Pi agent 数据目录

## 适用场景

- 在 pi 中编码时减少思考下一条提示词的时间
- 让建议贴合当前仓库的上下文与意图
- 通过自定义指令调整建议风格

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: `pi-prompt-suggester` suggests the user's likely next prompt after each assistant completion.
> L5: It uses recent conversation context plus a lightweight project intent seed so suggestions stay aligned with what the
> L71: - after an assistant completion, the extension may suggest the next user prompt

## 星数曲线

```mermaid
xychart-beta
    title "guwidoe/pi-prompt-suggester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-24 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `53fe68788110` · [字段定义](../../DATASET.md)*
