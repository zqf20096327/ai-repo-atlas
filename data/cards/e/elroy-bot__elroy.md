# elroy-bot/elroy

⭐ 59 · Python · Apache-2.0 · 推送 2026-06-03 · [GitHub](https://github.com/elroy-bot/elroy) · 个人维护

**带长期记忆与提醒功能的命令行 AI 个人助理**

可脚本化的记忆增强型 AI 个人助理，从命令行访问。提供对话长期记忆的自动召回、基于上下文与时间的提醒、记忆合并整理（冗余记忆后台整合）、Relevant Context 面板展示注入上下文，以及 ~/.elroy/contrib 插件目录（@tool 函数与自定义侧边栏）。支持 OpenAI、Anthropic、Google (Gemini) 及 OpenAI 兼容 API，按 API key 自动选型或环境变量显式配置。通过安装脚本、UV/pip、Docker 或源码安装，另提供 Claude Code 技能集成（/remember、/recall 等斜杠命令）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 长期记忆自动召回与冗余记忆后台合并整理
- 上下文相关与定时提醒工具
- contrib 插件目录：@tool 助手工具与自定义侧边栏
- 为 Claude Code 提供 /remember、/recall、/ingest 等记忆管理技能

## 适用场景

- 命令行日常 AI 助理，跨会话记住我的偏好与笔记
- 设置定时或基于上下文的提醒
- 把文档摄取进记忆供后续对话检索

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Elroy is a scriptable, memory augmented AI personal assistant, accessible from the command line. It features:
> L9: - **Long-term Memory**: Automatic memory recall of past conversations

## 星数曲线

```mermaid
xychart-beta
    title "elroy-bot/elroy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-28 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e398e10a80a` · [字段定义](../../DATASET.md)*
