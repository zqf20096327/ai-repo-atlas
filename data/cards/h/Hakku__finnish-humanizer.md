# Hakku/finnish-humanizer

⭐ 21 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/Hakku/finnish-humanizer) · 个人维护

**去除芬兰语 AI 文本痕迹的技能包：27 个模式改写为自然文风**

面向 15 个 AI 平台（Claude Code、Claude.ai、Cursor、GitHub Copilot、ChatGPT、Gemini Gems 等）分发的提示词/skill 文件包：内置 27 个 AI 痕迹模式（12 个芬兰语特有 + 15 个通用）与 5 种风格标注，用户粘贴芬兰语文本后由所在平台的 AI 完成分析与改写，默认直接改写并附修改摘要，超过 500 词自动先分析；也支持仅分析不修改的模式。限制：仅适用于芬兰语文本，不改变内容实质，不替代人工编辑。各平台以从 dist/ 复制对应规则文件的方式安装。

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

- 27 个 AI 模式（12 芬兰语特有 + 15 通用）与 5 种风格标注
- 支持 15 个平台，含 Claude Code / Cursor / Copilot / ChatGPT / Gemini Gems
- 长文本（>500 词）自动先分析后改写，防止大幅重写
- 提供仅分析模式与修改摘要输出

## 适用场景

- 把 AI 生成的芬兰语文本改写得更像人写的
- 在 Claude Code 或 Cursor 中编辑芬兰语 .md/.txt 时自动应用
- 仅检测文本中的 AI 痕迹模式，自行决定修改哪些

## 场景标签

`提示工程` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L5: Platforms
> L9: Supports 15 platforms: Claude Code, Claude.ai, Cursor, GitHub Copilot, Windsurf, Cline, Continue, JetBrains AI, Chat
> L27: 27 AI-patternia (12 suomenkielistä + 15 universaalia) ja 5 tyylimerkintää. Näillä teksti muunnetaan luonnolliseksi 

## 星数曲线

```mermaid
xychart-beta
    title "Hakku/finnish-humanizer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `417de05fdbc7` · [字段定义](../../DATASET.md)*
