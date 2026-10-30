# thevseprod/humanizer-ru

⭐ 45 · Python · MIT · 推送 2026-10-19 · [GitHub](https://github.com/thevseprod/humanizer-ru) · [官网](https://t.me/klimchenko_ai) · 个人维护

**去除 AI 文本痕迹的规则包：面向俄语，附 Claude Code 技能**

由 markdown 规则文件构成的无代码项目，用于改写神经网络生成的文本：识别并重写长破折号、官腔套话（“值得注意”）等俄语 AI 文本特征，同时保留原有事实与数字，另附英文规则集。使用方式有两种：将规则文件作为首条消息粘贴进任意对话工具（ChatGPT、Claude、Gemini、DeepSeek 等），或通过 `npx skills add` 命令将 `SKILL.md` 安装到 Claude Code、Cursor、Codex、Windsurf 等代理中。Claude Code 插件提供 `/humanize` 与 `/audit` 两条命令。包含基于 5-10 篇用户自身文本的校准机制。采用 MIT 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对俄语 AI 文本特征的规则集（另附英文版）
- 两轮处理：清除机器痕迹后校验事实是否留存
- 可单文件放入任意代理技能文件夹，或经 `npx skills` 一条命令安装
- Claude Code 插件提供 `/humanize`（改写）与 `/audit`（仅检查）命令

## 适用场景

- 我需要将 ChatGPT 生成的文案改写得更自然，同时保留事实与数据
- 我希望我的编码代理能自动避免在自身输出中套用 AI 文本模式
- 我希望根据自己过往的写作风格对技能进行校准

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: > Делает текст нейросети живым, как будто писал человек. Заточен под русский, есть и английская версия.
> L21: Кода нет, ставить ничего не нужно: это markdown-файл с правилами, который ты
> L58: Работает в ChatGPT, Claude, Gemini, DeepSeek - в любом чате.

## 星数曲线

```mermaid
xychart-beta
    title "thevseprod/humanizer-ru 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-30 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a981a169c8dc` · [字段定义](../../DATASET.md)*
