# lhupyn/motion-engine

⭐ 36 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/lhupyn/motion-engine) · [官网](https://lhupyn.github.io/motion-engine/) · 个人维护

**给 TalkingHead 虚拟形象做表情与肢体动作的决策库：按台词分类驱动**

面向 Web 虚拟形象开发者的动作引擎库：不要求主 LLM 在输出里加表情标记，而是把每句话送给一个决策模型（默认 Jev，经 OpenRouter 调用），按多选题形式选出表情、头部动作与手势并给出置信度，再由 director 层按阈值、冷却时间等规则过滤播放。表情以 ARKit blendshape 上的 FACS Action Unit 配方实现，说话时让位于口型。以 ES modules 提供，无构建步骤，仅契约测试对 TalkingHead 1.7 适配，自带表情与手势目录针对示例形象调校，其他形象可能需重调。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 决策模型按句分类表情/头部/手势，主 LLM 无需加标记
- director 规则层：置信度阈值、冷却、说话中抑制等，跳过原因可查
- FACS Action Unit 配方映射 ARKit blendshapes，说话时让位于口型
- 支持 Gemini Live、OpenAI Realtime、文本流等接入配方，以及浏览器内离线分类器

## 适用场景

- 让对话虚拟形象的表情和手势由台词自动决定，不改主 LLM 提示词
- 实时语音场景中让形象对用户发言做出倾听反应
- 通过 engine.face/body API 直接手动控制表情与手势

## 场景标签

 · 领域:对话式 AI/虚拟形象

## 证据(README 行号)

> L10: - **Jev decides.** Each sentence goes to Jev, TypeSafe's decision model, which picks an expression, a head movement
> L20: motion-engine gives that job to a decision model that answers multiple-choice questions instead of writing text, so
> L24: `feed()` → **segmenter** (sentences; a repeated final turn deduped; under two letters or only filler like `"mm"` dr

## 星数曲线

```mermaid
xychart-beta
    title "lhupyn/motion-engine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-25 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `26a6ca9fcb5c` · [字段定义](../../DATASET.md)*
