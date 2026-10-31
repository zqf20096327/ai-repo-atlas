# CheswickDEV/claude-fable-5-prompt-optimizer

⭐ 14 · MIT · 推送 2026-07-22 · [GitHub](https://github.com/CheswickDEV/claude-fable-5-prompt-optimizer) · 个人维护

**面向 Claude Fable 5 的提示词优化器（claude.ai Project 形式）**

以 claude.ai Project（说明文件 + 7 个知识文件）或拼接为 API 系统提示词两种方式使用：输入 `prompt: <原文>`，返回优化后的提示词、0–100 输入评分、逐条引用规则编号的变更日志、开放问题块；API 目标额外给出参数建议块（effort/max_tokens/streaming/fallbacks 等）。核心机制为 43 条标注来源的规则（全部指向官方 Anthropic 文档）、六阶段处理流程（目标检测、分析评分、复杂度路由 S/M/L/XL、转换、质量门、结构化输出）与 4.x 习惯清理。无独立安装软件，需在 claude.ai 中搭建 Project 或通过 Anthropic API 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 43 条规则均标注 [DOCUMENTED]/[DERIVED] 并可溯源至官方 Anthropic 文档
- 0–100 输入评分与逐条引用规则编号的可审计变更日志
- S/M/L/XL 四级复杂度路由，API 目标生成参数建议块
- 非英语提示词按原语言优化，评注跟随会话语言

## 适用场景

- 把粗糙提示词改写成适配 Claude Fable 5 的提示词
- 为 API 调用获取 effort/max_tokens/fallbacks 等参数建议
- 排查旧 4.x 提示习惯在 Fable 5 上的错误或拒答风险

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: A **claude.ai Project** that rewrites raw prompts for Claude Fable 5 (`claude-fable-5`) — Anthropic's Mythos-class 
> L62: 1. Open claude.ai and create a new **Project** (e.g., "Fable 5 Prompt Optimizer")
> L104: * 🎛️ **Adaptive target detection** — API prompts get a full `<parameters>` block; claude.ai chat prompts stay clea

## 星数曲线

```mermaid
xychart-beta
    title "CheswickDEV/claude-fable-5-prompt-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6b0f76bb0abf` · [字段定义](../../DATASET.md)*
