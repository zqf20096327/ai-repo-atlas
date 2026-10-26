# joostvanwollingen/opencode-personality

⭐ 36 · TypeScript · MIT · 推送 2026-02-23 · [GitHub](https://github.com/joostvanwollingen/opencode-personality) · 个人维护

**为 OpenCode 助手配置多性格与心情状态的插件**

OpenCode 编辑器的第三方插件，通过 JSON 配置文件定义多个性格（名称、描述、emoji 使用、俚语强度），性格描述被注入提示词以影响助手回复风格。内置心情状态机：心情可随对话漂移，支持自定义心情（含提示词提示与数值分数）、心情变化的 toast 通知，以及 setMood/savePersonality 两个工具和 /mood、/personality 命令组。支持全局与项目级配置合并，旧版单性格配置自动迁移。以 npm 包形式经 opencode.json 配置安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多性格存储与切换，性格描述注入提示词
- 心情漂移状态机（可配置漂移幅度、确定性种子、toast 通知）
- 全局与项目级配置智能合并，项目条目覆盖同名全局项
- 旧单性格配置文件加载时自动检测并迁移，无数据丢失

## 适用场景

- 让 OpenCode 助手以不同性格风格回复
- 在对话中创建、编辑、切换多个性格配置
- 为助手设置会随对话演变的心情状态

## 场景标签

 · 领域:开发者工具/AI 助手定制

## 证据(README 行号)

> L5: The OpenCode Personality Plugin transforms your assistant from a generic text generator into a living, breathing cha
> L79: |`description`|string|`""`|Personality description injected into prompts|

## 星数曲线

```mermaid
xychart-beta
    title "joostvanwollingen/opencode-personality 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a8f7dd073c08` · [字段定义](../../DATASET.md)*
