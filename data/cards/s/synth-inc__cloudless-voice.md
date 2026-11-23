# synth-inc/cloudless-voice

⭐ 4 · Swift · GPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/synth-inc/cloudless-voice) · [官网](cloudless.so) · 组织维护

**Mac 本地离线语音听写工具，按键说话文字入任意应用**

面向 Mac 用户的本地听写应用（原名 Onit Dictate）：按全局快捷键说话，语音识别完全在本机运行，音频不上传，识别文本输入任意应用的文本框。支持 Pin 语音模型（Parakeet v3 默认，Whisper、Moonshine、Qwen3-ASR 等可选）、用自建修正转录对新模型做回测、自定义词典与智能格式化。官方提供签名安装包，也可从源码构建；Smart Cleanup 转录润色部分为闭源预编译库，可用脚本构建全开源版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音识别完全在设备本地运行，音频不上传
- 可切换并锁定语音模型（Parakeet v3/Whisper/Moonshine/Qwen3-ASR）
- 用自建修正转录对新模型回测
- BYOK 清理支持自带模型或 API key

## 适用场景

- 在 Mac 上按键说话、免账号不限量地语音输入文字
- 离线环境下对任意应用做语音听写
- 想固定本地语音模型、不被云端换模型影响
- 用自己的语料测试并挑选合适的语音识别模型

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L13: Press a shortcut (default ⌥Space), speak, and your words are typed into
> L14: whatever app you're using. Speech recognition runs entirely on your Mac.
> L19:  sent anywhere to be transcribed. Choose the model that fits your Mac: Parakeet v3,

## 星数曲线

```mermaid
xychart-beta
    title "synth-inc/cloudless-voice 星数(近 3 点)"
    x-axis ["2026-11-15", "2026-11-16", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-15 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `6ac205de58df` · [字段定义](../../DATASET.md)*
