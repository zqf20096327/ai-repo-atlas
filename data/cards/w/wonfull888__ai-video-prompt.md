# wonfull888/ai-video-prompt

⭐ 4 · Python · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/wonfull888/ai-video-prompt) · [官网](https://bestprompts.app) · 个人维护 · 中文 README

**为 AI 视频创作者从参考视频反向生成可复用提示词**

以 agent 技能/Python 脚本形式提供的 video-to-prompt 工具：输入 30 秒内的参考视频，由视觉模型逐镜头拆解（人物动作、镜头运动、表情），再由文本模型复核并翻译，产出双语 prompt.md、分镜表、证据帧与结构化 JSON。设计为在 Cursor/Codex 等代码 agent 中以一句话调用的技能，密钥仅存于环境变量。默认限 30 秒、每次运行约 6-10 次模型调用；仅限非商业使用，商业使用需书面许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视觉模型整片读取视频并按镜头拆解（人物/运镜/表情）
- 视觉与文本双模型分工：生成草稿后逐帧复核并翻译为中文
- 输出双语 prompt.md 及 structured.json、shots.md、证据帧画廊
- 提供 Seedance/Veo/Sora/Kling/Wan 等生成模型的适配说明

## 适用场景

- 从参考片段生成提示词以复刻同风格镜头与运镜
- 在 Cursor/Codex 中用一句话调用视频反推流程
- 为广告/短剧系列整理可复用的分镜级提示词资产

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Give it a reference video, get back a prompt that restores it as faithfully as possible — light editing and it's rea
> L14: - A vision model watches the whole video (not just screenshots): it splits shots, tracks who does what, how the cam
> L61: The agent invokes this skill and runs the pipeline for you. Under the hood it's one command (input: one video under

## 星数曲线

```mermaid
xychart-beta
    title "wonfull888/ai-video-prompt 星数(近 3 点)"
    x-axis ["2026-10-22", "2026-11-14", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-22 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7f5a9b032186` · [字段定义](../../DATASET.md)*
