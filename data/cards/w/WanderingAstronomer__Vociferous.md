# WanderingAstronomer/Vociferous

⭐ 16 · Python · AGPL-3.0 · 推送 2026-06-17 · [GitHub](https://github.com/WanderingAstronomer/Vociferous) · 个人维护

**本地优先的桌面语音听写转写系统，生成可检索的语音记录**

面向单人使用的桌面听写应用：录制麦克风语音（或导入音频），经本地 faster-whisper/CTranslate2 转写为持久化文本，并用本地 CTranslate2 小语言模型（默认 Qwen3 4B INT8）或可选外部提供方（LM Studio、Groq）精炼文本；原始转写不可变，编辑与精炼存为变体。提供标签、搜索、导出、崩溃后音频恢复与使用分析。数据默认留在本机 SQLite，外部提供方为显式选择启用。Linux/macOS/Windows 经脚本从源码安装，Docker 仅限 Linux。macOS 版作者声明未充分测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 faster-whisper/CTranslate2 转写，麦克风音频默认不出机器
- 原始转写不可变，编辑/精炼作为变体存储，含来源记录
- 崩溃/断电后可恢复持久化音频资产
- 可选接入 LM Studio / Groq 做转写或精炼（OpenAI 兼容端点）

## 适用场景

- 把口述内容快速转为可搜索、可编辑的 Markdown 转写记录
- 在没有高端 GPU 时将转写/精炼卸载到 LM Studio 或 Groq
- 对语音记录打标签、检索、导出并查看使用统计

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L12: Vociferous is a desktop dictation system for people who think faster than they type. It records one human voice at 
> L32: - Transcribes through local faster-whisper/CTranslate2 or optional Groq ASR.
> L33: - Refines text through local CTranslate2, LM Studio, or Groq.

## 星数曲线

```mermaid
xychart-beta
    title "WanderingAstronomer/Vociferous 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f09d83434528` · [字段定义](../../DATASET.md)*
