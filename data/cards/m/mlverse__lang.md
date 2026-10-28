# mlverse/lang

⭐ 33 · R · NOASSERTION · 推送 2026-06-11 · [GitHub](https://github.com/mlverse/lang) · [官网](https://mlverse.github.io/lang/) · 组织维护

**用 LLM 实时翻译 R 函数帮助文档的包**

R 包，覆盖 R 会话中的 `?` 与 `help()` 函数，将函数帮助页实时翻译为目标语言，在 RStudio 或 Positron 的 Help 面板显示。通过 `lang_use()` 配置 LLM 连接（ellmer chat 对象或本地 Ollama）与目标语言（按 `.lang`、`LANGUAGE`、`LANG` 优先级确定）。翻译前先摘要英文全文作为上下文以保持各节一致性；结果默认缓存于临时目录，可指定固定目录跨会话复用。README 说明翻译质量取决于所用 LLM，且 R 强制的小节标题不会翻译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 `?`/`help()`，翻译结果直接显示在 RStudio/Positron Help 面板
- 支持 OpenAI（经 ellmer）与本地 Ollama 两种 LLM 后端
- 先生成英文摘要再逐节翻译以保持上下文一致性
- 翻译结果缓存，可指定固定目录跨会话复用

## 适用场景

- 阅读英文 R 文档困难时，用母语查看函数帮助
- 为团队统一配置 R 会话启动时的自动翻译
- 离线环境下用本地 Ollama 模型翻译帮助文档

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: Use an **LLM to translate a function’s help documentation on the fly**.
> L39: code shows how to use OpenAI’s GPT-4o model to translate `lm()`’s help

## 星数曲线

```mermaid
xychart-beta
    title "mlverse/lang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7cb141b92cd7` · [字段定义](../../DATASET.md)*
