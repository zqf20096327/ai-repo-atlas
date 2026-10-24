# Lyrcaxis/KokoroSharp

⭐ 248 · C# · MIT · 推送 2026-08-14 · [GitHub](https://github.com/Lyrcaxis/KokoroSharp) · 个人维护

**C#/.NET 本地 Kokoro TTS 推理库：多说话人多语言语音合成**

基于 ONNX runtime、以 C# 实现的 Kokoro TTS 推理引擎，通过即装即用的 NuGet 包集成到 .NET 项目中，内置 hexgrad 发布的全部语音及 Kokoro 82M v1.0 与 v1.1-zh 模型。支持文本分段流式合成、无限制数量语音混合、后台线程作业调度，覆盖美/英英语、中文、日语等 9 种语言。CPU 包开箱即用，GPU 支持、Android/iOS 运行另见专门文档；模型约 320MB，可本地路径加载或自动下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NuGet 包内置全部官方语音与 v1.0、v1.1-zh 模型
- 文本分段流式合成与无限制语音混合
- 支持 WAV 合成输出与逐音素时间戳（可用于口型同步）
- 后台线程作业调度，线程安全设计

## 适用场景

- 在 .NET 应用中集成离线语音合成
- 为游戏或应用角色提供多说话人多语言配音
- Android/iOS 移动端本地 TTS

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L7: KokoroSharp is a fully-featured inference engine for Kokoro TTS, built entirely in C# with ONNX runtime.
> L8: It enables developers to perform flexible and fast text-to-speech synthesis utilizing multiple speakers and language

## 星数曲线

```mermaid
xychart-beta
    title "Lyrcaxis/KokoroSharp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 247 --> 249
    line [248, 248]
```

2026-10-18 248 → 2026-10-24 248（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8612b89e283c` · [字段定义](../../DATASET.md)*
