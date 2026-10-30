# sgfsd/game-russificator

⭐ 16 · Python · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/sgfsd/game-russificator) · [官网](https://t.me/TRAPYCHINO) · 个人维护 · 中文 README

**自动将 Unity/Ren'Py/RPG Maker 游戏俄化的桌面工具**

面向玩家的 Windows 桌面程序：自动识别游戏引擎，提取并翻译游戏文本为俄语，向字体补绘西里尔字母，并把翻译嵌回游戏文件，可一键回退；另提供覆盖任意游戏的屏幕实时翻译（OCR + 叠加译文）。三种翻译方式：离线 OPUS-MT 机器翻译、本地 LLM（Gemma 4 via llama.cpp，支持 NVIDIA/AMD/Intel Vulkan 或 CPU，可用自定义 .gguf）、或用户自有 API 密钥调用云端模型（Gemini/DeepSeek/OpenRouter/Ollama 等）。运行需 Windows 10/11 64 位，GPL v3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动检测引擎（Unity Mono/IL2CPP、Ren'Py、RPG Maker 全系）并嵌入翻译
- 向游戏字体按原字重补绘西里尔字母，避免乱码与字号错乱
- 本地 LLM 翻译：Gemma 4 经 llama.cpp，支持自定义 .gguf，NVIDIA/AMD/Intel/CPU
- 屏幕实时翻译：PP-OCRv5 识别任意游戏画面文字并原位叠加译文

## 适用场景

- 我想把没有俄文本地化的 PC 游戏一键翻成俄语
- 老电脑离线用机器翻译、有显卡或 API 密钥时用 LLM 翻译游戏
- 对不支持文件改动的游戏（Unreal/Godot/在线游戏）用屏幕实时翻译
- 为朋友打包带安装器的俄化补丁（自动定位 Steam/GOG/Epic 游戏）

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Автоматическая русификация PC-игр на Unity, Ren'Py и RPG Maker — и живой перевод поверх
> L73: |1|**Машинный переводчик** (OPUS-MT, офлайн)|любой, даже очень старый ПК|~245 МБ, 2 ГБ ОЗУ|черновое, дословное|
> L74: |2|**Нейросеть на компьютере** (Gemma 4 через llama.cpp)|ПК с 8+ ГБ ОЗУ или видеокартой|2,6–7 ГБ на диске|хорошее|
> L172: игра, распознавать **всё, что на нём написано**, и показывать перевод поверх оригинала:

## 星数曲线

```mermaid
xychart-beta
    title "sgfsd/game-russificator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 10 --> 17
    line [11, 13, 16]
```

2026-10-18 11 → 2026-10-30 16（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `df585033885b` · [字段定义](../../DATASET.md)*
