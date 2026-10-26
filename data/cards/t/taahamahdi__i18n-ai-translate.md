# taahamahdi/i18n-ai-translate

⭐ 102 · TypeScript · GPL-3.0 · 推送 2026-09-06 · [GitHub](https://github.com/taahamahdi/i18n-ai-translate) · 个人维护

**用 AI 自动翻译 i18n 多语言资源文件的 CLI/Node 库/Action**

面向需要多语言维护的开发者：读取 i18next JSON、Gettext PO、Java .properties、iOS .strings、Rails YAML、JS/TS 模块及 ICU MessageFormat 目录文件，调用 ChatGPT、Claude、Gemini 或本地 Ollama 模型生成翻译并回写。机制上支持并行批次与共享限流、diff 模式仅重译变更键、check 模式校验现有翻译（可作 CI 门禁）、占位符保留、术语表与翻译缓存（缓存键与引擎无关）。以 npm 包、Node 库与 GitHub Action 三种形式提供，GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 i18next JSON/PO/.properties/.strings/YAML/JS-TS/ICU 共 7 类格式的无损往返
- 四种引擎可选：ChatGPT、Gemini、Claude、本地 Ollama
- diff 模式仅重译变更键，check 模式输出结构化报告并可作 CI 门禁
- 翻译缓存与术语表（doNotTranslate 与强制译法）

## 适用场景

- 应用新增语言时批量生成全部 locale 文件的翻译
- PR 中源文案变更后自动增量重译并提交
- CI 中检查现有翻译的漂移、缺失占位符等问题
- 用本地 Ollama 模型离线翻译资源文件

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L8: **Auto-translate i18n JSON and other locale files using AI.** Point it at one file or a whole directory and it machi
> L10: Works with **i18next-style JSON** out of the box, plus Gettext `.po`, Java `.properties`, iOS `.strings`, Rails YAM
> L118: |`-e, --engine`|chatgpt|chatgpt · gemini · claude · ollama|

## 星数曲线

```mermaid
xychart-beta
    title "taahamahdi/i18n-ai-translate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-26 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5f7ea6c84250` · [字段定义](../../DATASET.md)*
