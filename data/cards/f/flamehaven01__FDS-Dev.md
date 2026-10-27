# flamehaven01/FDS-Dev

⭐ 22 · Python · MIT · 推送 2025-12-09 · [GitHub](https://github.com/flamehaven01/FDS-Dev) · [官网](https://flamehaven.space/) · 个人维护

**面向非英语开发者的文档/注释 AI 翻译与结构化 lint CLI**

FDS-Dev 是一个 Python CLI 工具，包含两部分：结构感知的 lint（校验章节顺序、必需标题、断链）和将 Markdown、docstring、行内注释从韩语/中文/日语等翻译为英语的 AI 翻译器。通过 CodeCommentParser 解析代码结构以跳过代码块，用 TechnicalTermDatabase 保留 CamelCase/snake_case 标识符，并以 Omega 质量张量为翻译打分、低分自动重试或拒绝。默认后端为免配置的 py-googletrans（非官方 API，README 注明可能随时失效），可切换 DeepL、MyMemory 或自托管 LibreTranslate。面向希望产出英文文档的非英语开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结构感知 lint：章节顺序、必需标题、断链检查，并行执行并使用持久缓存
- AI 翻译保护代码块与标识符，仅改动散文部分
- Omega (Ω) 质量张量评分，低分翻译自动重试或拒绝
- 四种翻译后端可选，含自托管 LibreTranslate

## 适用场景

- 把母语写的 README 翻译成英文以便参与国际开源
- 对源码注释和 docstring 就地翻译为英文
- 在 CI 中对文档执行结构与断链检查

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L30: FDS-Dev is two tools in one:
> L33: 2. **An AI-Powered Translator:** Automatically translates your native-language docs and comments into fluent, natur

## 星数曲线

```mermaid
xychart-beta
    title "flamehaven01/FDS-Dev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0c53ff1bd25f` · [字段定义](../../DATASET.md)*
