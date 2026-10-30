# djethino/UnityGameTranslator

⭐ 26 · C# · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/djethino/UnityGameTranslator) · [官网](https://unitygametranslator.asymptomatikgames.com/) · 个人维护

**装进 Unity 游戏的实时翻译模组，支持本地 AI 与社区共享**

以 BepInEx/MelonLoader 模组形式装入任意 Unity 游戏（Mono 或 IL2CPP），在运行时翻译游戏文本，无需游戏本身或开发者支持。翻译后端可选：社区共享翻译、免费本地 AI（Ollama、LM Studio 等任何 OpenAI 兼容服务器）、在线服务（Google Translate、DeepL，用自带 key）。配套功能包括字体回退与提取、图像替换、UI 排除模式、H/V/A/S 翻译标签与 Main/Branch/Fork 协作体系，以及通过网站上传下载翻译。配套 Manager 工具可自动识别游戏类型并安装模组加载器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 运行时翻译，支持任何语言方向与所有书写系统
- 多后端：社区翻译、本地 LLM（Ollama/LM Studio，完全离线）、OpenAI 兼容在线服务、Google/DeepL
- H/V/A/S 翻译标签与 Main/Branch/Fork 社区协作、SSE 实时同步与三方合并
- 字体回退/提取、图像替换、UI 排除模式与游戏内编辑器

## 适用场景

- 玩不支持我语言的 Unity 游戏时实时翻译
- 用本地 Ollama 完全离线翻译，不花钱不用 API key
- 在社区上传/下载游戏翻译并协作改进
- 替换图片中嵌入的文字并保持游戏原字体观感

## 场景标签

 · 领域:游戏本地化/模组工具

## 证据(README 行号)

> L12: A mod that players install into any Unity game to play it in their language — the game doesn't need to support it, 
> L22: - **Multiple backends** — community downloads only, free local AI, or online services with your own key (OpenAI-com
> L32: |**AI (LLM)**|Any OpenAI-compatible server — local or cloud (Ollama, LM Studio, Groq, Gemini, OpenAI, OpenRouter, a

## 星数曲线

```mermaid
xychart-beta
    title "djethino/UnityGameTranslator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `61c53e869058` · [字段定义](../../DATASET.md)*
