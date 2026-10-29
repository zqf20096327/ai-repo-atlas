# FURUYAN1234/nano-banana-pro

⭐ 19 · JavaScript · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/FURUYAN1234/nano-banana-pro) · [官网](https://furuyan1234.github.io/nano-banana-pro/) · 个人维护 · 中文 README

**调用 OpenAI/Gemini API 自动生成 4~8 格漫画的 Web 应用**

实验性 Web 应用：由 AI 完成漫画制作的话题调查、台本结构、演出、提示词构建、图像生成与质量检查四个步骤（STEP2 台本→STEP3 图像指示→STEP4 生成）。OpenAI 支持 4 格与 5–8 格两种模式并可全自动选择，Gemini 仅支持 4 格彩色/黑白。以 A4 竖版单页为制作单位，可注册角色的外见、性格与人物关系用于剧本与演出，支持自动图像修正（综合检查 1 次、重大修正最多 1 次）。声明生成质量不保证每次一致，图像模型可能漏掉指令。源码公开可免费使用，生成的自有作品可商业化，外部 API 费用自理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 4 步工作流：台本→图像指示→生成→检查
- OpenAI 支持 4 格/5–8 格双模式，全自动时由 AI 依内容选择格数
- 角色外见、性格与人物关系注册并反映到剧本与演出
- 按 A4 单页规划构图与外框留白，可选自动图像修正

## 适用场景

- 输入题材后让 AI 自动产出一页 4 格或 5–8 格漫画
- 使用自建角色资料维持跨格人物的一致演出
- 在 4 格与 5–8 格两种结构间按故事需要选择

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: An experimental web application in which AI handles topic research, story structure, direction, prompt construction,
> L48: OpenAIでは両モードを使えます。Geminiはカラー・白黒とも4コマ固定で、5～8コマへの切り替えはありません。以下のスイッチはOpenAI接続時だけ表示します。 / Both modes are available with

## 星数曲线

```mermaid
xychart-beta
    title "FURUYAN1234/nano-banana-pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8b1004a182c5` · [字段定义](../../DATASET.md)*
