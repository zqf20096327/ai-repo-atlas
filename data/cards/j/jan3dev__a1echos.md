# jan3dev/a1echos

⭐ 13 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/jan3dev/a1echos) · [官网](https://www.a1lab.com/echos) · 组织维护 · 中文 README

**端侧 AI 语音记录与转录应用**

基于 Expo / React Native 构建的端侧语音笔记应用：通过 sherpa-onnx 在本地完成实时流式与基于文件的转录，会话与转录文本本地存储，音频以 AES-GCM 加密。内置 Whisper Tiny 模型，其余模型（Whisper Base/Small、NeMo Parakeet V3、Qwen3 ASR）按需从 HuggingFace 下载。含主题、语言、ASR 模型选择与无痕模式等设置。需自行开发构建（Expo Go 不可用），支持 iOS/Android。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- sherpa-onnx 端侧实时流式与文件转录
- 本地存储，音频 AES-GCM 加密
- 内置 Whisper Tiny，其余模型按需下载（含 Qwen3 ASR 支持 22 种中文方言）
- 无痕模式、按模型语言设置等选项

## 适用场景

- 在手机上离线录音并实时转录为文字
- 管理语音笔记与转录文本且数据不出设备
- 按需切换不同语言的 ASR 模型

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L10: - **Record + transcribe**: real-time streaming and file-based transcription via sherpa-onnx
> L42: Transcription runs on-device via sherpa-onnx. Only Whisper Tiny is bundled; the rest are downloaded on demand from 

## 星数曲线

```mermaid
xychart-beta
    title "jan3dev/a1echos 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `dcd43ce32a9b` · [字段定义](../../DATASET.md)*
