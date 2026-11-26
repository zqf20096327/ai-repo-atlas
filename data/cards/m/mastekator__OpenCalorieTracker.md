# mastekator/OpenCalorieTracker

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/mastekator/OpenCalorieTracker) · 个人维护

**自托管 PWA 卡路里追踪：拍照识别菜品并记录饮食日记**

用户拍摄餐盘照片，由自选的视觉模型返回菜品名称、克数、热量与三大营养素，可手工修正后存入个人日记。AI 提供方可插拔：支持 Gemini、OpenAI、Anthropic、OpenRouter、Ollama 本地模型或任意 OpenAI 兼容端点，也可完全不用 AI 改为手动录入。数据保存在自托管服务器上，无遥测。以单个 Docker 容器部署，支持家庭服务器、NAS、树莓派或 VPS，支持邀请家人共用、Passkey 登录、公制/美制单位与离线 PWA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拍照后由视觉模型返回菜品克数、kcal 与蛋白质/脂肪/碳水
- AI 提供方可插拔：云模型、OpenRouter、Ollama 本地模型或 OpenAI 兼容端点
- 无 AI 模式：留空提供方后全部功能仍可手动使用
- 单 Docker 容器部署，数据留在自托管服务器，无遥测

## 适用场景

- 自托管记录每日饮食与体重数据
- 拍照快速估算餐盘菜品的热量与营养素
- 邀请家人各自拥有独立日记的共享部署
- 用本地模型避免照片数据外发

## 场景标签

 · 领域:健康/饮食追踪

## 证据(README 行号)

> L6: Take a photo of your plate. A vision model of your choice lists the dishes with grams, kcal, protein, fat and carbs.
> L54: Any model that reads images: Gemini, OpenAI, Anthropic, OpenRouter, or a local one through Ollama, or any OpenAI-co
> L34: |Free and open source, one Docker container|Ads, subscriptions or upsells|

## 星数曲线

```mermaid
xychart-beta
    title "mastekator/OpenCalorieTracker 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `3593f0cf5d58` · [字段定义](../../DATASET.md)*
