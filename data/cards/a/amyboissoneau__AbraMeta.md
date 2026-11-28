# amyboissoneau/AbraMeta

⭐ 4 · Python · MIT · 推送 2026-11-07 · [GitHub](https://github.com/amyboissoneau/AbraMeta) · [官网](https://youtu.be/KROD3jJd2P8) · 个人维护

**面向内容创作者的 AI 创作工作室，自动生成视频文案与评论回复**

基于 Meta Muse Model API 与 Claude 构建的创作者工作室应用，在 Meta 全球 AI 开发者马拉松期间完成。功能包括：上传视频后由 Muse Voice 转写、Claude 读帧、Muse Spark 生成标题/文案/话题标签、Muse Wonder 选择钩子；SAM 3.1 实现反应贴纸与主体跟踪裁剪；自动字幕烧录；三个角色（Nico/Sage/Koa）分别处理评论回复、内容工作室与收入记账。评论回复默认需创作者逐条批准后才发布。目前仅在 macOS 上运行过，Windows/Linux 尚未支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 调用五个 Muse 模型加 Claude：转写、文案、分析、图像、分割各绑定一个功能
- 视频→成帖流水线：转写、读帧、三选一标题、封面与最佳发布时段提议
- SAM 3.1 mask decoder 从 JavaScript 移植为纯 Python，配 PIL 合成字幕与贴纸
- SQLite 原子 claim-locking 与速率门控的并发回复机制

## 适用场景

- 上传视频后生成并审批完整的 Reel/Stories 帖子文案
- 让 AI 以创作者本人语气起草评论回复并逐条把关
- 查看观看时长、收入与 AI 花费的分析仪表盘

## 场景标签

`AI 写作` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L13: - Drop in a raw video and **Sage** opens the story inside it — the hook, the post, the Reel, the Stories (staged fo
> L46: |**Muse Wonder** (`muse-wonder-1.0`)|Analytics — "Sage's read"|Meta's flagship model reads the page's real watch-th
> L111: **Windows and Linux: not supported yet.** The project has only been run on macOS. Judges should use a Mac or the d

## 星数曲线

```mermaid
xychart-beta
    title "amyboissoneau/AbraMeta 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-28"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-28 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `469441c224a1` · [字段定义](../../DATASET.md)*
