# Yeq6X/mazelingo

⭐ 27 · TypeScript · MIT · 推送 2026-08-25 · [GitHub](https://github.com/Yeq6X/mazelingo) · 个人维护

**给语言学习者：网页句子级双语混合显示的 Chrome 扩展**

MV3 架构的 Chrome 扩展，将网页文本按句（长句按从句）以可调比例替换为外语，形成两种语言逐句混排的阅读体验；点击可切换原文与译文，hover 显示对译、语法解说、词汇追踪与 TTS 朗读。翻译由用户自备的 LLM API key 驱动（OpenAI/Anthropic/Gemini/GLM/DeepSeek/OpenRouter），扩展自身无服务器，key 仅存于 Chrome Storage；支持按站点 opt-in、仅翻译可视区域与两层缓存。开发基于 WXT + TypeScript(strict)，Node 22.18 以上。

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

- 滑块控制外语替换比例，点击反转子句原文⇄译文
- hover 提供对译、语法解说、词汇追踪与 TTS
- 支持 OpenAI/Anthropic/Gemini/GLM/DeepSeek/OpenRouter 多家 API key，无自建服务器
- 基于 URL+正文种子的确定性混排，重访同页结果一致

## 适用场景

- 用母语和目标语言混合阅读网页来学习语言
- 阅读时随时查看句子的对译与语法解说
- 控制 API 消耗，只翻译正在看的页面部分

## 场景标签

 · 领域:语言学习/浏览器扩展

## 证据(README 行号)

> L3: Webページの文章を**文単位で英日(任意の2言語)ミックス表示**する語学学習向け拡張です。
> L13: - 翻訳はあなたの **LLM APIキー**で動きます(OpenAI / Anthropic / Gemini / GLM / DeepSeek / **OpenRouter**)。拡張側にサーバーはなく、キーは Chrome 

## 星数曲线

```mermaid
xychart-beta
    title "Yeq6X/mazelingo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `88ec72934432` · [字段定义](../../DATASET.md)*
