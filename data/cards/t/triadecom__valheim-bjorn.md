# triadecom/valheim-bjorn

⭐ 12 · C# · MIT · 推送 2026-10-12 · [GitHub](https://github.com/triadecom/valheim-bjorn) · 个人维护

**Valheim 的 AI 维京伙伴 Mod：Claude 驱动，可对话、作战、采集**

基于 BepInEx 5 的 Valheim Mod，为游戏加入一个 NPC 伙伴「Бьёрн」。玩家通过聊天或按 R 语音下达自然语言（俄语）指令，Mod 将上下文摘要交给 Claude（默认 Haiku，可选 Sonnet），以 JSON 返回要说的内容、多步计划与要记忆的内容。伙伴可跟随、作战、弓箭狩猎、采集、伐木、挖矿、管理专属箱子、记忆地点并守卫基地；每个「世界+角色」有独立的三层长期记忆。语音识别（Parakeet MLX）与合成（Silero）本地运行，仅 LLM 调用云端。仅支持 macOS Apple Silicon；双进程架构因 HarmonyX 无法 patch arm64 而采用 Rosetta + 原生 arm64 桥接。LLM 不可用时可按关键字理解简单命令但不说话。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Haiku/Sonnet 生成对话、多步行动计划与记忆更新（JSON 流式输出）
- 每『世界+角色』独立的三层长期记忆（最近对话/事实/编年史）
- 本地语音链路：Parakeet TDT 0.6B v3 识别 + Silero/Piper 合成
- 对话、采集、狩猎、修筑、守卫等约 20 类游戏内行为

## 适用场景

- 单人 Valheim 游戏中带一个可用俄语对话和指挥的 NPC 伙伴
- 让 NPC 代为采集、狩猎、看守和修理基地
- 通过语音 push-to-talk 与游戏内伙伴实时对话

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **Напарник-NPC с мозгами от Claude: ходит за тобой, дерётся, охотится с луком, собирает травы, рубит лес, складывает
> L14: *English summary: a BepInEx mod for Valheim that adds an AI companion. The NPC follows you, fights (axe or bow), hu
> L79: Если мост с LLM недоступен, Бьёрн всё равно понимает простые команды по ключевым словам, но молчит.

## 星数曲线

```mermaid
xychart-beta
    title "triadecom/valheim-bjorn 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-02"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-19 12 → 2026-11-02 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `4b00367cc0e8` · [字段定义](../../DATASET.md)*
