# ogunsakin01/laravel-video-demos

⭐ 3 · PHP · MIT · 推送 2026-11-11 · [GitHub](https://github.com/ogunsakin01/laravel-video-demos) · [官网](https://github.com/ogunsakin01/laravel-video-demos/wiki) · 个人维护

**为 Laravel 应用自动生成并维护 how-to/产品演示视频的包**

以 Laravel 包形式安装，开发者在 studio 中描述应用的一个操作流程，AI 模型读取应用代码生成逐步计划，Playwright 在真实浏览器中对样例数据录制视频，附带光标、字幕、标题卡与旁白配乐。计划随视频存储，UI 变更后可用 verify/refresh 命令免费重录，并提供 CI 预览、成本估算与每视频支出上限、可索引的帮助库与 Blade 嵌入组件。要求 PHP 8.3+、Laravel 12/13、Node.js 与 ffmpeg，仅在本地运行 studio。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 读代码规划流程，Playwright 在真实浏览器录制视频
- 计划随视频存储，UI 变更后重录无需 AI 成本
- 输出 GIF、方形/竖版副本及 Pest 浏览器测试代码
- 提供 MCP 服务器与 JSON 输出命令供编码 agent 使用

## 适用场景

- 为 Laravel 应用的帮助中心批量生成操作演示视频
- 应用改版后自动检测并重录受影响的视频
- 在 PR 中录制被改动流程的预览视频供评审观看
- 为同一视频生成多种语言的字幕与旁白

## 场景标签

`视频生成` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L12: Describe a flow in your Laravel app and get a recorded how-to video of it. An AI model (Claude by default, or OpenA
> L86: 5. **Playwright records the plan** on each screen you chose. If a step still fails, the AI fixes the plan and it tr
> L104: - **Any model**: Claude by default, or OpenAI, Gemini, Mistral, a local model with Ollama, and others through Pris

## 星数曲线

```mermaid
xychart-beta
    title "ogunsakin01/laravel-video-demos 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `fedf8711e6b6` · [字段定义](../../DATASET.md)*
