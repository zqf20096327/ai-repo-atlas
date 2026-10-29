# stof-dorof/fretwise-listener

⭐ 56 · HTML · 推送 2026-10-28 · [GitHub](https://github.com/stof-dorof/fretwise-listener) · 个人维护

**实时吉他音高识别练习应用，把弹奏映射到指板可视化**

跨平台吉他练习应用：通过麦克风或音频接口采集音频，经分帧、频谱分析、谐波加权和时域平滑的流水线检测基频，再结合调弦配置推断弦与品，在实时指板画布上给出颜色反馈。内置找音、把位、音阶、音程、和弦音、盲弹六种练习模式，支持自定义练习、多种调弦预设与多语言界面。音频处理全部在本地进行，无云端依赖与遥测。以桌面应用下载形式提供，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时音高检测与弦/品自动推断（谐波加权流水线）
- 六种内置练习模式与可扩展练习引擎
- 本地离线运行，无云端依赖与遥测
- 多调弦预设（标准/drop/open/自定义）与本地会话历史

## 适用场景

- 练习时实时看到所弹音符在指板上的位置
- 通过找音、音阶、音程等训练建立指板直觉
- 离线环境下进行日常吉他练习并追踪进度

## 场景标签

 · 领域:音乐教育/音频分析

## 证据(README 行号)

> L36: - 🎧 **Real-time pitch detection** from microphone or audio interface input
> L56: 1. **Capture** — The audio interface or microphone delivers a stream of samples at a configurable rate.

## 星数曲线

```mermaid
xychart-beta
    title "stof-dorof/fretwise-listener 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b3273cf740a5` · [字段定义](../../DATASET.md)*
